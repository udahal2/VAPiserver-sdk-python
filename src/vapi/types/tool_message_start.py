# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .condition import Condition
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ToolMessageStart(UniversalBaseModel):
    type: typing.Literal["request-start"] = pydantic.Field(default="request-start")
    """
    This message is triggered when the tool call starts.
    
    This message is never triggered for async tools.
    
    If this message is not provided, one of the default filler messages "Hold on a sec", "One moment", "Just a sec", "Give me a moment" or "This'll just take a sec" will be used.
    """

    content: str = pydantic.Field()
    """
    This is the content that the assistant says when this message is triggered.
    """

    conditions: typing.Optional[typing.List[Condition]] = pydantic.Field(default=None)
    """
    This is an optional array of conditions that the tool call arguments must meet in order for this message to be triggered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
