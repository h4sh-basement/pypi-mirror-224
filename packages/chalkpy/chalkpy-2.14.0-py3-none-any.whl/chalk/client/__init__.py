from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Any, List, Literal, Mapping, Optional, Protocol, Sequence, Union, overload

import pandas as pd
import requests
from typing_extensions import TypeAlias

from chalk.client.exc import ChalkAuthException, ChalkBaseException
from chalk.client.models import (
    BranchDeployResponse,
    BranchIdParam,
    ChalkError,
    ChalkException,
    DatasetFilter,
    ErrorCode,
    ErrorCodeCategory,
    FeatureDropResponse,
    FeatureObservationDeletionResponse,
    FeatureResult,
    OfflineQueryContext,
    OnlineQuery,
    OnlineQueryContext,
    OnlineQueryResponse,
    QueryMeta,
    QueryStatus,
    ResolverRunResponse,
    ResolverTestResponse,
    WhoAmIResponse,
)
from chalk.features import DataFrame, Feature
from chalk.features.tag import BranchId, EnvironmentId
from chalk.parsed.branch_state import BranchGraphSummary

if TYPE_CHECKING:
    import polars as pl


class DatasetRevision(Protocol):
    """Class wrapper around revisions for Datasets."""

    revision_id: uuid.UUID
    """UUID for the revision job."""

    creator_id: str
    """UUID for the creator of the job."""

    outputs: List[str]
    """Output features for the dataset revision."""

    givens_uri: Optional[str]
    """Location of the givens stored for the dataset."""

    status: QueryStatus
    """Status of the revision job."""

    filters: DatasetFilter
    """Filters performed on the dataset."""

    num_partitions: int
    """Number of partitions for revision job."""

    output_uris: str
    """Location of the outputs stored fo the dataset."""

    output_version: int
    """Storage version of the outputs."""

    num_bytes: Optional[int] = None
    """Number of bytes of the output, updated upon success."""

    created_at: Optional[datetime] = None
    """Timestamp for creation of revision job."""

    started_at: Optional[datetime] = None
    """Timestamp for start of revision job."""

    terminated_at: Optional[datetime] = None
    """Timestamp for end of revision job."""

    dataset_name: Optional[str] = None
    """Name of revision, if given."""

    dataset_id: Optional[uuid.UUID] = None
    """ID of revision, if name is given."""

    def get_data_as_polars(
        self,
        output_id: bool = False,
        output_ts: bool = False,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the output.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pl.LazyFrame`.
        output_ts
            Whether to return the timestamp feature in a column
            named `__chalk__.CHALK_TS` in the resulting `pl.LazyFrame`.

        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query output data.
        """
        ...

    def get_data_as_pandas(
        self,
        output_id: bool = False,
        output_ts: bool = False,
    ) -> pd.DataFrame:
        """Loads a `pd.DataFrame` containing the output.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pd.DataFrame`.
        output_ts
            Whether to return the timestamp feature in a column
            named `__chalk__.CHALK_TS` in the resulting `pd.DataFrame`.

        Returns
        -------
        pd.DataFrame
            A `pd.DataFrame` materializing query output data.
        """
        ...

    def get_data_as_dataframe(
        self,
        output_id: bool = False,
        output_ts: bool = False,
    ) -> DataFrame:
        """Loads a Chalk `DataFrame` containing the output.


        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `DataFrame`.
        output_ts
            Whether to return the timestamp feature in a column
            named `__chalk__.CHALK_TS` in the resulting `DataFrame`.

        Returns
        -------
        DataFrame
            A `DataFrame` materializing query output data.
        """
        ...

    def download_data(
        self,
        path: str,
        output_id: bool = False,
        output_ts: bool = False,
        num_executors: Optional[int] = None,
    ) -> None:
        """Downloads output files pertaining to the revision to given path.

        Datasets are stored in Chalk as sharded Parquet files. With this
        method, you can download those raw files into a directory for processing
        with other tools.

        Parameters
        ----------
        path
            A directory where the Parquet files from the dataset will be downloaded.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `DataFrame`.
        output_ts
            Whether to return the timestamp feature in a column
            named `__chalk__.CHALK_TS` in the resulting `DataFrame`.
        num_executors
            Number of executors to use to download files in parallel.
        """
        ...

    def get_input_dataframe(
        self,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the inputs.

        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query input data.
        """
        ...

    def wait_for_completion(self, show_progress: bool = True) -> None:
        """Waits for the revision job to complete.

        offline_query() returns a `DatasetRevision` instance immediately after
        submitting the revision job. This method can be used to wait for the
        revision job to complete.

        Once the revision job is complete, the `status` attribute of the
        `DatasetRevision` instance will be updated to reflect the status of the
        revision job.

        If the revision job was successful, you can then use methods such as
        `get_data_as_pandas()` without having to wait for the revision job to
        complete.

        Parameters
        ----------
        show_progress
            Whether to display progress bars while waiting for the revision job
        """
        ...


class Dataset(Protocol):
    """Wrapper around Offline Query results.
    Datasets are obtained by invoking `ChalkClient.offline_query()`.
    `Dataset` instances store important metadata and enable the retrieval of
    offline query outputs.

    >>> from chalk.client import ChalkClient, Dataset
    >>> uids = [1, 2, 3, 4]
    >>> at = datetime.now()
    >>> dataset: Dataset = ChalkClient().offline_query(
    ...     input={
    ...         User.id: uids,
    ...         User.ts: [at] * len(uids),
    ...     },
    ...     output=[
    ...         User.id,
    ...         User.fullname,
    ...         User.email,
    ...         User.name_email_match_score,
    ...     ],
    ...     dataset_name='my_dataset'
    ... )
    >>> df = dataset.get_data_as_pandas()
    >>> df.recompute(features=[User.fraud_score], branch="feature/testing")
    """

    is_finished: bool
    """Whether the most recent `DatasetRevision` is finished or still pending."""

    version: int
    """Storage version number of outputs."""

    revisions: List[DatasetRevision]
    """A list of all `DatasetRevision` instances belonging to this dataset."""

    dataset_name: Optional[str]
    """The unique name for this dataset, if given."""

    dataset_id: Optional[uuid.UUID]
    """The unique UUID for this dataset."""

    errors: Optional[List[ChalkError]]
    """A list of errors in loading the dataset, if they exist."""

    explain_output: Optional[str]

    def get_data_as_polars(
        self,
        output_id: bool = False,
        output_ts: bool = False,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the output of the most recent revision.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pl.LazyFrame`.
        output_ts
            Whether to return the timestamp feature in a column
            named `__chalk__.CHALK_TS` in the resulting `pl.LazyFrame`.

        Returns
        -------
        pl.LazyFrame
            a `pl.LazyFrame` materializing query output data.
        """
        ...

    def get_data_as_pandas(
        self,
        output_id: bool = False,
        output_ts: bool = False,
    ) -> pd.DataFrame:
        """Loads a `pd.DataFrame` containing the output of the most recent revision.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `pd.DataFrame`.
        output_ts
            Whether to return the timestamp feature in a column
            named `__chalk__.CHALK_TS` in the resulting `pd.DataFrame`.

        Returns
        -------
        pd.DataFrame
            A `pd.DataFrame` materializing query output data.
        """
        ...

    def get_data_as_dataframe(
        self,
        output_id: bool = False,
        output_ts: bool = False,
    ) -> DataFrame:
        """Loads a Chalk `DataFrame` containing the output of the most recent revision.

        Other Parameters
        ----------
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `DataFrame`.
        output_ts
            Whether to return the timestamp feature in a column
            named `__chalk__.CHALK_TS` in the resulting `DataFrame`.

        Returns
        -------
        DataFrame
            A `DataFrame` materializing query output data.
        """
        ...

    def download_data(
        self,
        path: str,
        num_executors: Optional[int] = None,
    ) -> None:
        """Downloads output files pertaining to the revision to given path.

        Datasets are stored in Chalk as sharded Parquet files. With this
        method, you can download those raw files into a directory for processing
        with other tools.

        Parameters
        ----------
        path
            A directory where the Parquet files from the dataset will be downloaded.

        Other Parameters
        ----------
        num_executors
            Number of executors to use to download files in parallel.

        Examples
        ----------
        >>> from chalk.client import ChalkClient, Dataset
        >>> uids = [1, 2, 3, 4]
        >>> at = datetime.now()
        >>> dataset: Dataset = ChalkClient().offline_query(
        ...     input={
        ...         User.id: uids,
        ...         User.ts: [at] * len(uids),
        ...     },
        ...     output=[
        ...         User.id,
        ...         User.fullname,
        ...         User.email,
        ...         User.name_email_match_score,
        ...     ],
        ...     dataset_name='my_dataset'
        ... )
        >>> dataset.download_data('my_directory')
        """
        ...

    def get_input_dataframe(
        self,
    ) -> pl.LazyFrame:
        """Loads a `pl.LazyFrame` containing the inputs.

        Returns
        -------
        pl.LazyFrame
            A `pl.LazyFrame` materializing query input data.
        """
        ...

    def recompute(
        self,
        features: Optional[List[Union[Feature, Any]]] = None,
        branch: Optional[str] = None,
        wait: bool = False,
        show_progress: bool = False,
    ):
        """Creates a new revision of this dataset by recomputing the specified features.

        Carries out the new computation on the branch specified when constructing the client.

        Parameters
        ------
        features
            A list of specific features to recompute. Features that don't exist in the dataset will be added.
            If not provided, all the existing features in the dataset will be recomputed.
        branch
            If specified, Chalk will route your request to the relevant branch.
            If None, Chalk will route your request to a non-branch deployment.
            If not specified, Chalk will use the current client's branch info.
        wait
            If True, this method will block until recomputation is finished.
        show_progress
            If True, progress bars will be shown while recomputation is running.
            This flag will also be propogated to the methods of the resulting
            `Dataset`.

        Raises
        ------
        ValueError
            If no branch was provided to the Chalk Client.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> dataset = ChalkClient(branch="data_science").offline_query(...)
        >>> df = dataset.get_data_as_polars()
        >>> # make changes to resolvers in your project
        >>> dataset.recompute()
        >>> new_df = dataset.get_data_as_polars() # receive newly computed data
        """
        ...


FeatureReference: TypeAlias = Union[str, Any]


class OnlineQueryResult(Protocol):
    data: List[FeatureResult]
    """The output features and any query metadata."""

    errors: Optional[List[ChalkError]]
    """Errors encountered while running the resolvers.

    If no errors were encountered, this field is empty.
    """

    meta: Optional[QueryMeta]
    """
    Metadata about the query execution. Only present if `include_meta=True` is passed to the
    relevant query method.
    """

    def get_feature(self, feature: FeatureReference) -> Optional[FeatureResult]:
        """Convenience method for accessing feature result from the data response

        Parameters
        ----------
        feature
            The feature or its string representation.

        Returns
        -------
        FeatureResult | None
            The `FeatureResult` for the feature, if it exists.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> data = ChalkClient().query(...)
        >>> data.get_feature(User.name).ts
        datetime.datetime(2023, 2, 5, 23, 25, 26, 427605)
        >>> data.get_feature("user.name").meta.cache_hit
        False
        """
        ...

    def get_feature_value(self, feature: FeatureReference) -> Optional[Any]:
        """Convenience method for accessing feature values from the data response

        Parameters
        ----------
        feature
            The feature or its string representation.

        Returns
        -------
        Any
            The value of the feature.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> data = ChalkClient().query(...)
        >>> data.get_feature_value(User.name)
        "Katherine Johnson"
        >>> data.get_feature_value("user.name")
        "Katherine Johnson"
        """
        ...


class ChalkClient:
    """The `ChalkClient` is the primary interface for interacting with Chalk.

    You can use it to query data, trigger resolver runs, gather offline data, and more.
    """

    @overload
    def __init__(self, session: Optional[requests.Session] = None):
        """Create a `ChalkClient` with environment variables or credentials in `~/.chalk.yml`.

        The client will first check for the presence of the environment variables
        `CHALK_CLIENT_ID` and `CHALK_CLIENT_SECRET`. If they are present,
        `ChalkClient` will use those credentials, and optionally the API server
        and environment specified by `CHALK_API_SERVER` and `CHALK_ENVIRONMENT`.

        Otherwise, it will look for a `~/.chalk.yml` file, which is updated
        when you run `chalk login`. If a token for the specific project directory
        if found, that token will be used. Otherwise, the token under the key
        `default` will be used. When using the `~/.chalk.yml` file, you can still
        optionally override the API server and environment by setting the
        environment variables `CHALK_API_SERVER` and `CHALK_ENVIRONMENT`.

        Parameters
        ----------
        session
            A `requests.Session` to use for all requests. If not provided,
            a new session will be created.

        Raises
        ------
        ChalkAuthException
            If `client_id` or `client_secret` are not provided, there
            is no `~/.chalk.yml` file with applicable credentials,
            and the environment variables `CHALK_CLIENT_ID` and
            `CHALK_CLIENT_SECRET` are not set.
        """
        ...

    @overload
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        environment: Optional[EnvironmentId] = None,
        api_server: Optional[str] = None,
        branch: Optional[BranchId] = None,
        session: Optional[requests.Session] = None,
        query_server: Optional[str] = None,
        additional_headers: Optional[Mapping[str, str]] = None,
    ):
        """Create a `ChalkClient` with the given credentials.

        Parameters
        ----------
        client_id
            The client ID to use to authenticate. Can either be a
            service token id or a user token id.
        client_secret
            The client secret to use to authenticate. Can either be a
            service token secret or a user token secret.
        environment
            The ID or name of the environment to use for this client.
            Not necessary if your `client_id` and `client_secret`
            are for a service token scoped to a single environment.
            If not present, the client will use the environment variable
            `CHALK_ENVIRONMENT`.
        api_server
            The API server to use for this client. Required if you are
            using a Chalk Dedicated deployment. If not present, the client
            will check for the presence of the environment variable
            `CHALK_API_SERVER`, and use that if found.
        query_server
            The query server to use for this client. Required if you are
            using a standalone Chalk query engine deployment. If not present,
            the client will default to the value of api_server.
        branch
            If specified, Chalk will route all requests from this client
            instance to the relevant branch. Some methods allow you to
            override this instance-level branch configuration by passing
            in a `branch` argument.
        session
            A `requests.Session` to use for all requests. If not provided,
            a new session will be created.
        additional_headers
            A map of additional HTTP headers to pass with each request.

        Raises
        ------
        ChalkAuthException
            If `client_id` or `client_secret` are not provided, there
            is no `~/.chalk.yml` file with applicable credentials,
            and the environment variables `CHALK_CLIENT_ID` and
            `CHALK_CLIENT_SECRET` are not set.
        """
        ...

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        environment: Optional[EnvironmentId] = None,
        api_server: Optional[str] = None,
        branch: Optional[BranchId] = None,
        session: Optional[requests.Session] = None,
    ):
        """Create a `ChalkClient`. Clients can either be created
        explicitly, with environment variables, or using credentials
        in `~/.chalk.yml`.

        The `__init__` method specifies overloads for this purpose.
        See the overloaded methods for details.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient(branch="testing")
        >>> client.query(
        ...     input={
        ...         User.name: "Katherine Johnson"
        ...     },
        ...     output=[User.fico_score],
        ...     staleness={User.fico_score: "10m"},
        ... )
        """
        ...

    def query(
        self,
        input: Union[Mapping[FeatureReference, Any], Any],
        output: Sequence[FeatureReference],
        now: Optional[datetime] = None,
        staleness: Optional[Mapping[FeatureReference, str]] = None,
        context: Optional[OnlineQueryContext] = None,  # Deprecated.
        environment: Optional[EnvironmentId] = None,
        tags: Optional[List[str]] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[BranchId] = ...,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        include_meta: bool = False,
        meta: Optional[Mapping[str, str]] = None,
        explain: Union[bool, Literal["only"]] = False,
        store_plan_stages: bool = False,
    ) -> OnlineQueryResult:
        """Compute features values using online resolvers.
        See https://docs.chalk.ai/docs/query-basics for more information.

        Parameters
        ----------
        input
            The features for which there are known values, mapped to those values.
            For example, `{User.id: 1234}`
        output
            Outputs are the features that you'd like to compute from the inputs.
            For example, `[User.age, User.name, User.email]`
        staleness
            Maximum staleness overrides for any output features or intermediate features.
            See https://docs.chalk.ai/docs/query-caching for more information.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.
        query_name
            The semantic name for the query you're making for example, `"loan_application_model"`.
            Typically, each query that you make from your application should have a name.
            Chalk will present metrics and dashboard functionality grouped by 'query_name'.
        explain
            Log the query execution plan. Requests using `explain=True` will be slower
            than requests using `explain=False`. If "only", the query will not be executed,
            and only the query plan will be returned.

            If True, 'include_meta' will be set to True as well.
        store_plan_stages
            If `True`, the output of each of the query plan stages will be stored.
            This option dramatically impacts the performance of the query,
            so it should only be used for debugging.
        correlation_id
            You can specify a correlation ID to be used in logs and web interfaces. This should be
            globally unique, i.e. a `uuid` or similar. Logs generated during the execution of your query
            will be tagged with this correlation id.

        Other Parameters
        ----------------
        meta
            Arbitrary `key:value` pairs to associate with a query.
        context
            Deprecated in favor of `environment` and `tags`.

        Returns
        -------
        OnlineQueryResult
            The outputs features and any query metadata,
            plus errors encountered while running the resolvers.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().query(
        ...     input={
        ...         User.name: "Katherine Johnson"
        ...     },
        ...     output=[User.fico_score],
        ...     staleness={User.fico_score: "10m"},
        ... )
        """
        ...

    def multi_query(
        self,
        queries: list[OnlineQuery],
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[BranchId] = ...,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
        use_feather: Optional[bool] = True,
        compression: Optional[str] = "uncompressed",
    ):
        """
        Execute multiple queries (represented by 'queries') in a single request.
        """
        ...

    def query_many(
        self,
        input: Union[Mapping[FeatureReference, Sequence[Any]], Any],
        output: Sequence[FeatureReference],
        now: Optional[Sequence[datetime]] = None,
        staleness: Optional[Mapping[FeatureReference, str]] = None,
        context: Optional[OnlineQueryContext] = None,  # Deprecated.
        environment: Optional[EnvironmentId] = None,
        tags: Optional[List[str]] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[BranchId] = ...,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
    ) -> OnlineQueryResult:
        """Compute features values for many inputs using online resolvers.
        See https://docs.chalk.ai/docs/query-basics for more information.

        This endpoint is not available in all environments.

        Parameters
        ----------
        input
            The features for which there are known values, mapped to a list
            of the values.
        output
            Outputs are the features that you'd like to compute from the inputs.
        staleness
            Maximum staleness overrides for any output features or intermediate features.
            See https://docs.chalk.ai/docs/query-caching for more information.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.
        branch
            If specified, Chalk will route your request to the relevant branch.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.

        Other Parameters
        ----------------
        query_name
            The name for class of query you're making, for example, "loan_application_model".
        correlation_id
            A globally unique ID for the query, used alongside logs and
            available in web interfaces.
        meta
            Arbitrary `key:value` pairs to associate with a query.
        context
            Deprecated in favor of `environment` and `tags`.

        Returns
        -------
        OnlineQueryResult
            The outputs features and any query metadata,
            plus errors encountered while running the resolvers.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        ... ChalkClient().query(
        ...     input={User.name: ["Katherine Johnson", "Eleanor Roosevelt"]},
        ...     output=[User.fico_score],
        ...     staleness={User.fico_score: "10m"},
        ... )
        """
        ...

    def offline_query(
        self,
        input: Optional[Union[Mapping[FeatureReference, Any], pd.DataFrame, pl.DataFrame, DataFrame]] = None,
        input_times: Union[Sequence[datetime], datetime, None] = None,
        output: Sequence[Union[str, Feature, Any]] = (),
        required_output: Sequence[FeatureReference] = (),
        environment: Optional[EnvironmentId] = None,
        dataset_name: Optional[str] = None,
        branch: Optional[BranchId] = ...,
        max_samples: Optional[int] = None,
        wait: bool = False,
        show_progress: bool = True,
        recompute_features: Union[bool, List[FeatureReference]] = False,
        lower_bound: Optional[datetime] = None,
        upper_bound: Optional[datetime] = None,
        store_plan_stages: bool = False,
        explain: Union[bool, Literal["only"]] = False,
        tags: Optional[List[str]] = None,
    ) -> Dataset:
        """Compute feature values from the offline store.
        See `Dataset` for more information.

        Parameters
        ----------
        input
            The features for which there are known values.
            It can be a mapping of features to a list of values for each
            feature, or an existing `DataFrame`.
            Each element in the `DataFrame` or list of values represents
            an observation in line with the timestamp in `input_times`.
        input_times
            A list of the times of the observations from `input`.
        output
            The features that you'd like to sample, if they exist.
            If an output feature was never computed for a sample (row) in
            the resulting `DataFrame`, its value will be `None`.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        dataset_name
            A unique name that if provided will be used to generate and
            save a `Dataset` constructed from the list of features computed
            from the inputs.
        max_samples
            The maximum number of samples to include in the `DataFrame`.
            If not specified, all samples will be returned.
        branch
            If specified, Chalk will route your request to the relevant branch.
            If None, Chalk will route your request to a non-branch deployment.
            If not specified, Chalk will use the current client's branch info.
        wait
            If True, this method will block until the query is finished.
        show_progress
            If True, progress bars will be shown while the query is running.
            This flag will also be propogated to the methods of the resulting
            `Dataset`.
        recompute_features
            If True, all output features will be recomputed.
            If False, all output features will be sampled from the offline store.
            If a list, all output features in recompute_features will be recomputed,
            and all other output features will be sampled from the offline store.
        lower_bound
            If specified, the query will only be run on data observed after this timestamp
        upper_bound
            If specified, the query will only be run on data observed before this timestamp
        store_plan_stages
            If True, the output of each of the query plan stages will be stored
            in GCS. This will dramatically impact the performance of the query,
            so it should only be used for debugging.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.

        Other Parameters
        ----------------
        required_output
            The features that you'd like to sample and must exist
            in each resulting row. Rows where a `required_output`
            was never stored in the offline store will be skipped.
            This differs from specifying the feature in `output`,
            where instead the row would be included, but the feature
            value would be `None`.

        Returns
        -------
        Dataset
            A Chalk `Dataset`.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> uids = [1, 2, 3, 4]
        >>> at = datetime.now()
        >>> dataset = ChalkClient().offline_query(
        ...     input={
        ...         User.id: uids,
        ...         User.ts: [at] * len(uids),
        ...     },
        ...     output=[
        ...         User.id,
        ...         User.fullname,
        ...         User.email,
        ...         User.name_email_match_score,
        ...     ],
        ...     dataset_name='my_dataset'
        ... )
        >>> df = dataset.get_data_as_pandas()
        """
        ...

    def get_dataset(
        self,
        dataset_name: str,
        environment: Optional[EnvironmentId] = None,
    ) -> Dataset:
        """Get a Chalk `Dataset` containing data from a previously created dataset.

        If an offline query has been created with a dataset name, `.get_dataset` will
        return a Chalk `Dataset`.
        The `Dataset` wraps a lazily-loading Chalk `DataFrame` that enables us to analyze
        our data without loading all of it directly into memory.
        See https://docs.chalk.ai/docs/training-client for more information.

        Parameters
        ----------
        dataset_name
            The name of the `Dataset` to return.
            Previously, you must have supplied a dataset name upon an offline query.
            Dataset names are unique for each environment.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.

        Returns
        -------
        Dataset
            A `Dataset` that lazily loads your query data.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> uids = [1, 2, 3, 4]
        >>> at = datetime.now()
        >>> X = ChalkClient().offline_query(
        ...     input={
        ...         User.id: uids,
        ...         User.ts: [at] * len(uids),
        ...     },
        ...     output=[
        ...         User.id,
        ...         User.fullname,
        ...         User.email,
        ...         User.name_email_match_score,
        ...     ],
        ...     dataset='my_dataset_name'
        ... )

        Some time later...

        >>> dataset = ChalkClient().get_dataset(
        ...     dataset_name='my_dataset_name'
        ... )
        ...

        If memory allows:

        >>> df: pd.DataFrame = dataset.get_data_as_pandas()
        """
        ...

    def trigger_resolver_run(
        self,
        resolver_fqn: str,
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[BranchId] = ...,
    ) -> ResolverRunResponse:
        """Triggers a resolver to run.
        See https://docs.chalk.ai/docs/runs for more information.

        Parameters
        ----------
        resolver_fqn
            The fully qualified name of the resolver to trigger.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.
        branch

        Returns
        -------
        ResolverRunResponse
            Status of the resolver run and the run ID.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().trigger_resolver_run(
        ...     resolver_fqn="mymodule.fn"
        ... )
        """
        ...

    def get_run_status(
        self,
        run_id: str,
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        branch: Optional[BranchId] = ...,
    ) -> ResolverRunResponse:
        """Retrieves the status of a resolver run.
        See https://docs.chalk.ai/docs/runs for more information.

        Parameters
        ----------
        run_id
            ID of the resolver run to check.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        preview_deployment_id
            If specified, Chalk will route your request to the
            relevant preview deployment.
        branch

        Returns
        -------
        ResolverRunResponse
            Status of the resolver run and the run ID.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().get_run_status(
        ...     run_id="3",
        ... )
        ResolverRunResponse(
            id="3",
            status=ResolverRunStatus.SUCCEEDED
        )
        """
        ...

    def whoami(self) -> WhoAmIResponse:
        """Checks the identity of your client.

        Useful as a sanity test of your configuration.

        Returns
        -------
        WhoAmIResponse
            The identity of your client.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().whoami()
        WhoAmIResponse(user="44")
        """
        ...

    def delete_features(
        self,
        namespace: str,
        features: Optional[List[str]],
        tags: Optional[List[str]],
        primary_keys: List[str],
    ) -> FeatureObservationDeletionResponse:
        """Targets feature observation values for deletion and performs deletion online and offline.

        Parameters
        ----------
        namespace
            The namespace in which the target features reside.
        features
            An optional list of the feature names of the features that should be deleted
            for the targeted primary keys. Not specifying this and not specifying the "tags" field
            will result in all features being targeted for deletion for the specified primary keys.
            Note that this parameter and the "tags" parameter are mutually exclusive.
        tags
            An optional list of tags that specify features that should be targeted for deletion.
            If a feature has a tag in this list, its observations for the primary keys you listed
            will be targeted for deletion. Not specifying this and not specifying the "features"
            field will result in all features being targeted for deletion for the specified primary
            keys. Note that this parameter and the "features" parameter are mutually exclusive.
        primary_keys
            The primary keys of the observations that should be targeted for deletion.

        Returns
        -------
        FeatureObservationDeletionResponse
            Holds any errors (if any) that occurred during the drop request.
            Deletion of a feature may partially-succeed.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().delete_features(
        ...     namespace="user",
        ...     features=["name", "email", "age"],
        ...     primary_keys=[1, 2, 3]
        ... )
        """
        ...

    def drop_features(self, namespace: str, features: List[str]) -> FeatureDropResponse:
        """
        Performs a drop on features, which involves a deletes all their data
        (both online and offline). Once the feature is reset in this manner,
        its type can be changed.

        Parameters
        ----------
        namespace
            The namespace in which the target features reside.
        features
            A list of the feature names of the features that should be dropped.

        Returns
        -------
        FeatureDropResponse
            Holds any errors (if any) that occurred during the drop request.
            Dropping a feature may partially-succeed.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().drop_features(
        ...     namespace="user",
        ...     features=["name", "email", "age"],
        ... )
        """
        ...

    def upload_features(
        self,
        input: Mapping[FeatureReference, Any],
        branch: Optional[BranchId] = ...,
        environment: Optional[EnvironmentId] = None,
        preview_deployment_id: Optional[str] = None,
        correlation_id: Optional[str] = None,
        query_name: Optional[str] = None,
        meta: Optional[Mapping[str, str]] = None,
    ) -> Optional[List[ChalkError]]:
        """Upload data to Chalk for use in offline resolvers or to prime a cache.

        Parameters
        ----------
        input
            The features for which there are known values, mapped to those values.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        preview_deployment_id
            If specified, Chalk will route your request to the relevant preview deployment
        query_name
            Optionally associate this upload with a query name. See `.query` for more information.

        Other Parameters
        ----------------
        correlation_id
            A globally unique ID for this operation, used alongside logs and
            available in web interfaces.
        meta
            Arbitrary key:value pairs to associate with a query.
        branch

        Returns
        -------
        list[ChalkError] | None
            The errors encountered from uploading features.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().upload_features(
        ...     input={
        ...         User.id: 1,
        ...         User.name: "Katherine Johnson"
        ...     }
        ... )
        """
        ...

    def sample(
        self,
        output: Sequence[FeatureReference] = (),
        required_output: Sequence[FeatureReference] = (),
        output_id: bool = False,
        output_ts: bool = False,
        max_samples: Optional[int] = None,
        dataset: Optional[str] = None,
        branch: Optional[BranchId] = None,
        environment: Optional[EnvironmentId] = None,
        tags: Optional[List[str]] = None,
    ) -> pd.DataFrame:
        """Get the most recent feature values from the offline store.

        See https://docs.chalk.ai/docs/training-client for more information.

        Parameters
        ----------
        output
            The features that you'd like to sample, if they exist.
            If an output feature was never computed for a sample (row)
            in the resulting `DataFrame`, its value will be `None`.
        max_samples
            The maximum number of rows to return.
        environment
            The environment under which to run the resolvers.
            API tokens can be scoped to an environment.
            If no environment is specified in the query,
            but the token supports only a single environment,
            then that environment will be taken as the scope
            for executing the request.
        dataset
            The `Dataset` name under which to save the output.
        tags
            The tags used to scope the resolvers.
            See https://docs.chalk.ai/docs/resolver-tags for more information.

        Other Parameters
        ----------------
        required_output
            The features that you'd like to sample and must exist
            in each resulting row. Rows where a `required_output`
            was never stored in the offline store will be skipped.
            This differs from specifying the feature in `output`,
            where instead the row would be included, but the feature
            value would be `None`.
        output_ts
            Whether to return the timestamp feature in a column
            named `"__chalk__.CHALK_TS"` in the resulting `DataFrame`.
        output_id
            Whether to return the primary key feature in a column
            named `"__chalk__.__id__"` in the resulting `DataFrame`.
        branch

        Returns
        -------
        pd.DataFrame
            A `pandas.DataFrame` with columns equal to the names of the features in output,
            and values representing the value of the most recent observation.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> sample_df = ChalkClient().sample(
        ...     output=[
        ...         Account.id,
        ...         Account.title,
        ...         Account.user.full_name
        ...     ],
        ...     max_samples=10
        ... )
        """
        ...

    def create_branch(
        self,
        branch_name: str,
        create_only: bool = True,
        source_deployment_id: Optional[str] = None,
        environment: Optional[EnvironmentId] = None,
    ) -> BranchDeployResponse:
        """
        Create a new branch based off of a deployment from the server.
        By default, uses the latest live deployment.

        Parameters
        ----------
        branch_name
            The name of the new branch to create.
        create_only
            If create_only=True, will raise an error if a branch
            with the given name already exists. If create_only=False
            and the branch exists, then that branch will be deployed
            to.
        source_deployment_id
            (Optional) the specific deployment ID to use for the
            branch. If not specified, the latest live deployment on
            the server will be used. You can see which deployments
            are available by clicking on the 'Deployments' tab on
            the project page in the Chalk dashboard.
        environment
            The environment under which to create the branch. API
            tokens can be scoped to an environment. If no environment
            is specified in the query, the environment will be taken
            from the client's cached token.

        Returns
        -------
        BranchDeployResponse
            A response object containing metadata about the branch.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient()
        >>> client.create_branch("my-new-branch")
        >>> client.set_branch("my-new-branch")
        """
        ...

    def get_branches(self) -> List[str]:
        """Lists the current branches for this environment.

        Returns
        -------
        list[str]
            A list of the names of branches available on this environment.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> ChalkClient().get_branches()
        ["testing", "feat/new-feature"]
        """
        ...

    def get_branch(self) -> Optional[str]:
        """Displays the current branch this client is pointed at.

        If the current environment does not support branch deployments
        or no branch is set, this method returns `None`.

        Returns
        -------
        str | None
            The name of the current branch or `None`.

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient(branch="my-branch")
        >>> assert client.get_branch() == "my-branch"
        """
        ...

    def set_branch(self, branch_name: str):
        """Point the Chalk client at the given branch.

        If the branch does not exist or if branch deployments
        are not enabled for the current environment, this
        method raises an error.

        Parameters
        ----------
        branch_name
            The name of the branch to use

        Examples
        --------
        >>> from chalk.client import ChalkClient
        >>> client = ChalkClient()
        >>> client.create_branch("my-new-branch")
        >>> client.set_branch("my-new-branch")
        """
        ...

    def reset_branch(self, branch: BranchIdParam = ..., environment: Optional[EnvironmentId] = None):
        ...

    def branch_state(
        self,
        branch: Union[BranchId, Ellipsis] = ...,
        environment: Optional[EnvironmentId] = None,
    ) -> BranchGraphSummary:
        """
        Returns a `chalk.parsed.branch_state.BranchGraphSummary` object that contains the state of the branch server:
        Which resolver/features are defined, and the history of live notebook updates on the server.
        :param branch:
        :param environment:
        """
        ...

    def test_streaming_resolver(
        self,
        resolver_fqn: str,
        num_messages: Optional[int] = None,
        test_message_filepath: Optional[str] = None,
        test_message_keys: Optional[list[str]] = None,
        test_message_bodies: Optional[list[str]] = None,
        branch: Union[BranchId, Ellipsis] = ...,
        environment: Optional[EnvironmentId] = None,
    ) -> ResolverTestResponse:
        """
        Tests a streaming resolver and its ability to parse and resolve messages.

        Parameters
        ----------
        resolver_fqn
            The fqn of the streaming resolver
        num_messages
            The number of messages to digest from the stream source.
            As messages may not be incoming into the stream, this action may time out.
        test_message_filepath
            A filepath from which test messages will be ingested.
            This file should be newline delimited json as follows:
            >>> {"key": ..., "message_body": ...}
            >>> {"key": ..., "message_body": ...}
        test_message_keys
            Alternatively, keys can be supplied here along with the "test_message_bodies" argument.
        test_message_bodies
            Message bodies can be supplied here along with the "test_message_keys" argument.

        Other Parameters
        ----------
        branch
        environment

        Returns
        -------
        ResolverTestResponse
            A simple wrapper around a status and optional error message.
        """

    def __new__(cls, *args: Any, **kwargs: Any):
        from chalk.client.client_impl import ChalkAPIClientImpl

        return ChalkAPIClientImpl.__new__(cls, *args, **kwargs)


ChalkAPIClientProtocol: TypeAlias = ChalkClient
"""Deprecated. Use `ChalkClient` instead."""

__all__ = [
    "ChalkAPIClientProtocol",
    "ChalkBaseException",
    "ChalkClient",
    "ChalkAuthException",
    "ChalkError",
    "ChalkException",
    "Dataset",
    "DatasetRevision",
    "ErrorCode",
    "ErrorCodeCategory",
    "FeatureResult",
    "OfflineQueryContext",
    "OnlineQueryContext",
    "OnlineQueryResponse",
    "OnlineQueryResult",
    "QueryStatus",
    "ResolverRunResponse",
    "WhoAmIResponse",
]
