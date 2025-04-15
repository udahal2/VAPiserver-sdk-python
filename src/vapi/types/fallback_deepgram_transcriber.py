# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .deepgram_transcriber_model import DeepgramTranscriberModel
from .deepgram_transcriber_language import DeepgramTranscriberLanguage
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FallbackDeepgramTranscriber(UncheckedBaseModel):
    provider: typing.Literal["deepgram"] = pydantic.Field(default="deepgram")
    """
    This is the transcription provider that will be used.
    """

    model: typing.Optional[DeepgramTranscriberModel] = pydantic.Field(default=None)
    """
    This is the Deepgram model that will be used. A list of models can be found here: https://developers.deepgram.com/docs/models-languages-overview
    """

    language: typing.Optional[DeepgramTranscriberLanguage] = pydantic.Field(default=None)
    """
    This is the language that will be set for the transcription. The list of languages Deepgram supports can be found here: https://developers.deepgram.com/docs/models-languages-overview
    """

    smart_format: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="smartFormat")] = (
        pydantic.Field(default=None)
    )
    """
    This will be use smart format option provided by Deepgram. It's default disabled because it can sometimes format numbers as times but it's getting better.
    """

    code_switching_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="codeSwitchingEnabled")
    ] = pydantic.Field(default=None)
    """
    This automatically switches the transcriber's language when the customer's language changes. Defaults to false.
    
    Usage:
    - If your customers switch languages mid-call, you can set this to true.
    
    Note:
    - To detect language changes, Vapi uses a custom trained model. Languages supported (X = limited support):
      1. Arabic
      2. Bengali
      3. Cantonese
      4. Chinese
      5. Chinese Simplified (X)
      6. Chinese Traditional (X)
      7. English
      8. Farsi (X)
      9. French
      10. German
      11. Haitian Creole (X)
      12. Hindi
      13. Italian
      14. Japanese
      15. Korean
      16. Portuguese
      17. Russian
      18. Spanish
      19. Thai
      20. Urdu
      21. Vietnamese
    - To receive `language-change-detected` webhook events, add it to `assistant.serverMessages`.
    
    @default false
    """

    mip_opt_out: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="mipOptOut")] = pydantic.Field(
        default=None
    )
    """
    If set to true, this will add mip_opt_out=true as a query parameter of all API requests. See https://developers.deepgram.com/docs/the-deepgram-model-improvement-partnership-program#want-to-opt-out
    
    This will only be used if you are using your own Deepgram API key.
    
    @default false
    """

    numerals: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If set to true, this will cause deepgram to convert spoken numbers to literal numerals. For example, "my phone number is nine-seven-two..." would become "my phone number is 972..."
    
    @default false
    """

    confidence_threshold: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="confidenceThreshold")
    ] = pydantic.Field(default=None)
    """
    Transcripts below this confidence threshold will be discarded.
    
    @default 0.4
    """

    keywords: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    These keywords are passed to the transcription model to help it pick up use-case specific words. Anything that may not be a common word, like your company name, should be added here.
    """

    keyterm: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Keyterm Prompting allows you improve Keyword Recall Rate (KRR) for important keyterms or phrases up to 90%.
    """

    endpointing: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the timeout after which Deepgram will send transcription on user silence. You can read in-depth documentation here: https://developers.deepgram.com/docs/endpointing.
    
    Here are the most important bits:
    - Defaults to 10. This is recommended for most use cases to optimize for latency.
    - 10 can cause some missing transcriptions since because of the shorter context. This mostly happens for one-word utterances. For those uses cases, it's recommended to try 300. It will add a bit of latency but the quality and reliability of the experience will be better.
    - If neither 10 nor 300 work, contact support@vapi.ai and we'll find another solution.
    
    @default 10
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
