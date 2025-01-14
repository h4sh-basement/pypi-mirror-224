from typing import Any, List, Optional, Union

from pydantic import BaseModel

from chalk.integrations.named import load_integration_variable
from chalk.streams.base import StreamSource
from chalk.utils.duration import Duration


class KinesisSource(StreamSource, BaseModel, frozen=True):
    stream_name: Optional[Union[str, List[str]]] = None
    """The name of your stream. Either this or the stream_arn must be specified"""

    stream_arn: Optional[Union[str, List[str]]] = None
    """The ARN of your stream. Either this or the stream_name must be specified"""

    region_name: Optional[str] = None
    """
    AWS region string, e.g. "us-east-2"
    """

    name: Optional[str] = None
    """
    The name of the integration, as configured in your Chalk Dashboard.
    """

    late_arrival_deadline: Duration = "infinity"
    """
    Messages older than this deadline will not be processed.
    """

    dead_letter_queue_stream_name: Optional[str] = None
    """
    Kinesis stream name to send messages when message processing fails
    """

    aws_access_key_id: Optional[str] = None
    """
    AWS access key id credential
    """

    aws_secret_access_key: Optional[str] = None
    """
    AWS secret access key credential
    """

    aws_session_token: Optional[str] = None
    """
    AWS access key id credential
    """

    endpoint_url: Optional[str] = None
    """
    optional endpoint to hit Kinesis server
    """

    consumer_role_arn: Optional[str] = None
    """
    Optional role ARN for the consumer to assume
    """

    def __init__(
        self,
        *,
        region_name: str,
        stream_name: Optional[str] = None,
        stream_arn: Optional[str] = None,
        late_arrival_deadline: Duration = "infinity",
        dead_letter_queue_stream_name: Optional[str] = None,
        name: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        consumer_role_arn: Optional[str] = None,
    ):
        if stream_name is None and stream_arn is None:
            raise ValueError(f"Kinesis source {name} must have either a stream name or stream ARN specified.")
        super(KinesisSource, self).__init__(
            name=name,
            stream_name=stream_name
            or load_integration_variable(name="KINESIS_STREAM_NAME", integration_name=name)
            or KinesisSource.__fields__.get("stream_name").default,
            stream_arn=stream_arn
            or load_integration_variable(name="KINESIS_STREAM_ARN", integration_name=name)
            or KinesisSource.__fields__.get("stream_arn").default,
            late_arrival_deadline=late_arrival_deadline
            or load_integration_variable(name="KINESIS_LATE_ARRIVAL_DEADLINE", integration_name=name)
            or KinesisSource.__fields__.get("late_arrival_deadline").default,
            dead_letter_queue_stream_name=dead_letter_queue_stream_name
            or load_integration_variable(name="KINESIS_DEAD_LETTER_QUEUE_STREAM_NAME", integration_name=name)
            or KinesisSource.__fields__.get("dead_letter_queue_stream_name").default,
            aws_access_key_id=aws_access_key_id
            or load_integration_variable(name="KINESIS_AWS_ACCESS_KEY_ID", integration_name=name)
            or KinesisSource.__fields__.get("aws_access_key_id").default,
            aws_secret_access_key=aws_secret_access_key
            or load_integration_variable(name="KINESIS_AWS_SECRET_ACCESS_KEY", integration_name=name)
            or KinesisSource.__fields__.get("aws_secret_access_key").default,
            aws_session_token=aws_session_token
            or load_integration_variable(name="KINESIS_AWS_SESSION_TOKEN", integration_name=name)
            or KinesisSource.__fields__.get("aws_session_token").default,
            region_name=region_name
            or load_integration_variable(name="KINESIS_REGION_NAME", integration_name=name)
            or KinesisSource.__fields__.get("region_name").default,
            endpoint_url=endpoint_url
            or load_integration_variable(name="KINESIS_ENDPOINT_URL", integration_name=name)
            or KinesisSource.__fields__.get("endpoint_url").default,
            consumer_role_arn=consumer_role_arn
            or load_integration_variable(name="KINESIS_CONSUMER_ROLE_ARN", integration_name=name)
            or KinesisSource.__fields__.get("consumer_role_arn").default,
        )
        self.registry.append(self)

    def _config_to_json(self) -> Any:
        return self.json()

    @property
    def streaming_type(self) -> str:
        return "kinesis"

    @property
    def dlq_name(self) -> Union[str, None]:
        return self.dead_letter_queue_stream_name
