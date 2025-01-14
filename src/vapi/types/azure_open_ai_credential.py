# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .azure_open_ai_credential_region import AzureOpenAiCredentialRegion
from .azure_open_ai_credential_models_item import AzureOpenAiCredentialModelsItem
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AzureOpenAiCredential(UniversalBaseModel):
    provider: typing.Literal["azure-openai"] = "azure-openai"
    region: AzureOpenAiCredentialRegion
    models: typing.List[AzureOpenAiCredentialModelsItem]
    open_ai_key: typing_extensions.Annotated[str, FieldMetadata(alias="openAIKey")] = pydantic.Field()
    """
    This is not returned in the API.
    """

    ocp_apim_subscription_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ocpApimSubscriptionKey")
    ] = pydantic.Field(default=None)
    """
    This is not returned in the API.
    """

    id: str = pydantic.Field()
    """
    This is the unique identifier for the credential.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this credential belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the credential was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the assistant was last updated.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of credential. This is just for your reference.
    """

    open_ai_endpoint: typing_extensions.Annotated[str, FieldMetadata(alias="openAIEndpoint")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
