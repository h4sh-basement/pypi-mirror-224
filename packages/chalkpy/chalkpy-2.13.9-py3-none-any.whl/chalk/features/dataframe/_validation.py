from __future__ import annotations

import datetime
import json
import warnings
from typing import TYPE_CHECKING, Union, cast

import dateutil.parser
import isodate

from chalk.features._encoding.missing_value import MissingValueStrategy
from chalk.features.feature_field import Feature, FeatureNotFoundException

if TYPE_CHECKING:
    import polars as pl

try:
    import zoneinfo
except ImportError:
    # Zoneinfo was introduced in python 3.9
    from backports import zoneinfo


def _polars_dtype_contains_struct(dtype: pl.PolarsDataType):
    """Returns whether the dtype contains a (potentially nested) struct"""
    import polars as pl

    if isinstance(dtype, pl.Struct) or (isinstance(dtype, type) and issubclass(dtype, pl.Struct)):
        return True
    if isinstance(dtype, pl.List):
        assert dtype.inner is not None
        return _polars_dtype_contains_struct(dtype.inner)
    return False


def _generate_empty_series_for_dtype(name: str, dtype: pl.PolarsDataType, length: int) -> pl.Series:
    """Safely generate a series of all null values for the specified datatype.

    Unlike the ``pl.Series`` constructor, this function can handle struct dtypes.
    """
    import polars as pl

    # if isinstance(dtype, pl.Struct):
    #     # Struct dtypes cannot be specified in the pl.Series constructor.
    #     # Instead, create a dataframe, then call .to_struct() on it
    #     # If recursing within a struct, it should have a length of zero
    #     data = {f.name: _generate_empty_series_for_dtype(f.name, f.dtype, length) for f in dtype.fields}
    #     temp_df = pl.DataFrame(data)
    #     return temp_df.to_struct(name)
    # if isinstance(dtype, pl.List) and isinstance(dtype.inner, pl.Struct):
    #     # The pl.Series constructor does not respect nested data types
    #     # So, we'll manually build a dataframe with the list set to the correct type,
    #     # set it to None, and then select just the list
    #     assert dtype.inner is not None
    #     data = {name: _generate_empty_series_for_dtype(name, dtype.inner, 0)}
    #     temp_df = pl.DataFrame(data)
    #     df_with_list = temp_df.select(pl.col(name).reshape((length, -1)))
    #     df_with_list = df_with_list.select(pl.when(True).then(None).otherwise(pl.col(name)).alias(name))
    #     list_of_struct_series = df_with_list.select(pl.col(name).reshape((length, -1))).get_column(name)
    #     return list_of_struct_series
    return pl.Series(name, dtype=dtype, values=([None] * length))


def _iso_parse(x: str, expected_tz: datetime.tzinfo | None) -> datetime.datetime:
    """This function converts the input into an expected timezone, and drops it, so we can cast it in polars with with_time_zone"""
    parsed = dateutil.parser.parse(x)
    if parsed.tzinfo is not None and expected_tz is not None:
        # Convert the timezone
        parsed = parsed.astimezone(expected_tz)
    # Now drop the timezone
    return parsed.replace(tzinfo=None)


def validate_df_schema(underlying: Union[pl.DataFrame, pl.LazyFrame]):
    # This is called from within DataFrame.__init__, which validates that polars is installed
    import polars as pl

    for root_fqn, actual_dtype in underlying.schema.items():
        feature = Feature.from_root_fqn(root_fqn)
        if feature.is_has_one or feature.is_has_many:
            continue
        expected_dtype = feature.converter.polars_dtype
        if actual_dtype == expected_dtype:
            continue
        if isinstance(underlying, pl.LazyFrame):
            underlying = underlying.collect()
        if len(underlying) == underlying.get_column(root_fqn).null_count() and actual_dtype != expected_dtype:
            # If all values are null, then replace with a null series of the correct datatype
            # It's quite possible that the original column will have an incorrect dtype if all values are null,
            # since there was no data to infer the correct dtype from
            underlying = underlying.with_columns(
                _generate_empty_series_for_dtype(root_fqn, expected_dtype, len(underlying))
            )
        elif isinstance(expected_dtype, pl.List) and actual_dtype == pl.Utf8:
            cast_expr = pl.col(root_fqn).apply(lambda x: None if x is None else json.loads(x))
            col = cast_expr.alias(root_fqn)
            try:
                underlying = underlying.with_columns(col)
            except Exception as e:
                raise TypeError(
                    f"Values for list feature `{root_fqn}` could not be deserialized from a JSON string to dtype `{expected_dtype}`."
                ) from e

            try:
                deser_actual_dtype = underlying[root_fqn].dtype
                assert deser_actual_dtype == expected_dtype
            except AssertionError as e:
                raise TypeError(
                    f"Values for list feature `{root_fqn}` could not be deserialized from a JSON string to dtype `{expected_dtype}`. Found type {deser_actual_dtype}, instead."
                ) from e
        elif _polars_dtype_contains_struct(expected_dtype):
            # Cannot cast to a struct type. Instead, will error, so the user can ensure the underlying
            # dictionaries / dataclasses are of the correct type
            col = pl.col(root_fqn).cast(expected_dtype)
            try:
                underlying = underlying.with_columns(underlying.select(col))
            except (pl.ComputeError, pl.PolarsPanicError) as e:
                try:
                    underlying = underlying.with_columns(
                        pl.from_arrow(
                            underlying.select(pl.col(root_fqn))
                            .to_arrow()[root_fqn]
                            .cast(feature.converter.pyarrow_dtype)
                        ).alias(root_fqn)
                    )
                except:
                    raise TypeError(
                        f"Expected struct field '{root_fqn}' to have dtype `{expected_dtype}`; got dtype `{actual_dtype}. Attempted to automatically coerce to the correct dtype, but failed with error: {e}`"
                    ) from e
        else:
            try:
                if actual_dtype == pl.Utf8:
                    if isinstance(expected_dtype, pl.Datetime):
                        # tzinfo = None if expected_dtype.time_zone is None else zoneinfo.ZoneInfo(expected_dtype.time_zone)
                        underlying = underlying.with_columns(pl.col(root_fqn).str.strptime(pl.Datetime).alias(root_fqn))
                        if cast(pl.Datetime, underlying.schema[root_fqn]).time_zone is not None:
                            cast_expr = pl.col(root_fqn).dt.convert_time_zone(expected_dtype.time_zone)
                    elif expected_dtype == pl.Date:
                        cast_expr = pl.col(root_fqn).apply(
                            lambda x: None if x is None else isodate.parse_date(x),
                        )
                    elif expected_dtype == pl.Time:
                        cast_expr = pl.col(root_fqn).apply(
                            lambda x: None if x is None else isodate.parse_time(x),
                        )
                    elif expected_dtype == pl.Duration:
                        cast_expr = pl.col(root_fqn).apply(
                            lambda x: None if x is None else isodate.parse_duration(x),
                        )
                    else:
                        cast_expr = pl.col(root_fqn).cast(expected_dtype)
                    col = cast_expr.alias(root_fqn)
                else:
                    col = pl.col(root_fqn).cast(expected_dtype)
                underlying = underlying.with_columns(col)
            except pl.ComputeError as e:
                raise TypeError(
                    f"Values for feature `{root_fqn}` with type '{feature.typ}' could not be converted "
                    f"to dtype `{expected_dtype}`. Found type {actual_dtype}, instead."
                ) from e

    return underlying


def validate_nulls(
    underlying: Union[pl.DataFrame, pl.LazyFrame],
    missing_value_strategy: MissingValueStrategy,
    tolerate_missing_features: bool = False,
) -> pl.DataFrame:
    """Validate that any null values are in columns that support nullable values"""
    # This is called from within DataFrame.__init__, which validates that polars is installed
    import polars as pl

    if isinstance(underlying, pl.LazyFrame):
        underlying = underlying.collect()
    schema = underlying.schema
    null_count_rows = underlying.null_count().to_dicts()
    if len(null_count_rows) == 0:
        return underlying  # Empty dataframe
    assert len(null_count_rows) == 1
    null_counts = null_count_rows[0]
    for col_name, null_count in null_counts.items():
        try:
            feature = Feature.from_root_fqn(col_name)
        except FeatureNotFoundException:
            if tolerate_missing_features:
                continue
            raise
        if null_count > 0 and not feature.typ.is_nullable and not isinstance(schema[col_name], pl.Struct):
            if missing_value_strategy == "allow":
                warnings.warn(
                    UserWarning(
                        f"Allowing missing value for feature '{col_name}' with type '{feature.typ}' strategy "
                        f"'default_or_allow'"
                    )
                )
            elif missing_value_strategy == "error":
                raise TypeError(
                    f"Feature '{col_name}' with type '{feature.typ}' has missing values, but the feature is non-nullable"
                )
            elif missing_value_strategy in ("default_or_error", "default_or_allow"):
                if feature.converter.has_default:
                    underlying = underlying.with_columns(
                        [pl.col(col_name).fill_null(feature.converter.primitive_default)]
                    )
                elif missing_value_strategy == "default_or_error":
                    raise TypeError(
                        f"Feature '{col_name}' with type '{feature.typ}' has missing values, "
                        f"but the feature does not have a default"
                    )
                else:
                    warnings.warn(
                        UserWarning(
                            f"Allowing missing value for feature '{col_name}' with type '{feature.typ}' "
                            f"with strategy 'default_or_allow'"
                        )
                    )
            else:
                raise ValueError(
                    (
                        f"Unsupported missing value strategy '{missing_value_strategy}'. "
                        "Allowed options are 'allow', 'error', and 'default_or_error'."
                    )
                )
    return underlying
