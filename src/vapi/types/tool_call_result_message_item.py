# This file was auto-generated by Fern from our API Definition.

import typing
from .tool_message_complete import ToolMessageComplete
from .tool_message_failed import ToolMessageFailed

ToolCallResultMessageItem = typing.Union[ToolMessageComplete, ToolMessageFailed]
