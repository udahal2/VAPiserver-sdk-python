# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateS3CredentialDto(UniversalBaseModel):
    aws_access_key_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="awsAccessKeyId")] = (
        pydantic.Field(default=None)
    )
    """
    AWS access key ID.
    """

    aws_secret_access_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="awsSecretAccessKey")
    ] = pydantic.Field(default=None)
    """
    AWS access key secret. This is not returned in the API.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    AWS region in which the S3 bucket is located.
    """

    s_3_bucket_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="s3BucketName")] = (
        pydantic.Field(default=None)
    )
    """
    AWS S3 bucket name.
    """

    s_3_path_prefix: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="s3PathPrefix")] = (
        pydantic.Field(default=None)
    )
    """
    The path prefix for the uploaded recording. Ex. "recordings/"
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of credential. This is just for your reference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
