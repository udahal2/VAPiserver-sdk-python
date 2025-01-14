# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .update_azure_open_ai_credential_dto_region import UpdateAzureOpenAiCredentialDtoRegion
from .update_azure_open_ai_credential_dto_models_item import UpdateAzureOpenAiCredentialDtoModelsItem
import typing_extensions
from ..core.serialization import FieldMetadata
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateAzureOpenAiCredentialDto(UniversalBaseModel):
    region: typing.Optional[UpdateAzureOpenAiCredentialDtoRegion] = None
    models: typing.Optional[typing.List[UpdateAzureOpenAiCredentialDtoModelsItem]] = None
    open_ai_key: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="openAIKey")] = pydantic.Field(
        default=None
    )
    """
    This is not returned in the API.
    """

    ocp_apim_subscription_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ocpApimSubscriptionKey")
    ] = pydantic.Field(default=None)
    """
    This is not returned in the API.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of credential. This is just for your reference.
    """

    open_ai_endpoint: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="openAIEndpoint")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
