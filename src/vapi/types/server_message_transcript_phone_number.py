# This file was auto-generated by Fern from our API Definition.

import typing
from .create_byo_phone_number_dto import CreateByoPhoneNumberDto
from .create_twilio_phone_number_dto import CreateTwilioPhoneNumberDto
from .create_vonage_phone_number_dto import CreateVonagePhoneNumberDto
from .create_vapi_phone_number_dto import CreateVapiPhoneNumberDto

ServerMessageTranscriptPhoneNumber = typing.Union[
    CreateByoPhoneNumberDto, CreateTwilioPhoneNumberDto, CreateVonagePhoneNumberDto, CreateVapiPhoneNumberDto
]
