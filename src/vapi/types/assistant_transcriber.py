# This file was auto-generated by Fern from our API Definition.

import typing
from .assembly_ai_transcriber import AssemblyAiTranscriber
from .azure_speech_transcriber import AzureSpeechTranscriber
from .custom_transcriber import CustomTranscriber
from .deepgram_transcriber import DeepgramTranscriber
from .gladia_transcriber import GladiaTranscriber
from .talkscriber_transcriber import TalkscriberTranscriber

AssistantTranscriber = typing.Union[
    AssemblyAiTranscriber,
    AzureSpeechTranscriber,
    CustomTranscriber,
    DeepgramTranscriber,
    GladiaTranscriber,
    TalkscriberTranscriber,
]
