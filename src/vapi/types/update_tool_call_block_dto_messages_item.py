# This file was auto-generated by Fern from our API Definition.

import typing
from .block_start_message import BlockStartMessage
from .block_complete_message import BlockCompleteMessage

UpdateToolCallBlockDtoMessagesItem = typing.Union[BlockStartMessage, BlockCompleteMessage]
