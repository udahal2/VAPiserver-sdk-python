# Reference
## Calls
<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.calls.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This will return calls with the specified assistantId.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.calls.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the call. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This is the assistant that will be used for the call. To use a transient assistant, use `assistant` instead.
    
</dd>
</dl>

<dl>
<dd>

**assistant:** `typing.Optional[CreateAssistantDto]` — This is the assistant that will be used for the call. To use an existing assistant, use `assistantId` instead.
    
</dd>
</dl>

<dl>
<dd>

**assistant_overrides:** `typing.Optional[AssistantOverrides]` — These are the overrides for the `assistant` or `assistantId`'s settings and template variables.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the squad that will be used for the call. To use a transient squad, use `squad` instead.
    
</dd>
</dl>

<dl>
<dd>

**squad:** `typing.Optional[CreateSquadDto]` — This is a squad that will be used for the call. To use an existing squad, use `squadId` instead.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` 

This is the phone number that will be used for the call. To use a transient number, use `phoneNumber` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `typing.Optional[ImportTwilioPhoneNumberDto]` 

This is the phone number that will be used for the call. To use an existing number, use `phoneNumberId` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` 

This is the customer that will be called. To call a transient customer , use `customer` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**customer:** `typing.Optional[CreateCustomerDto]` 

This is the customer that will be called. To call an existing customer, use `customerId` instead.

Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.calls.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.calls.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.calls.<a href="src/vapi/calls/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.calls.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the call. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Assistants
<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.assistants.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.assistants.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcriber:** `typing.Optional[CreateAssistantDtoTranscriber]` — These are the options for the assistant's transcriber.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[CreateAssistantDtoModel]` — These are the options for the assistant's LLM.
    
</dd>
</dl>

<dl>
<dd>

**voice:** `typing.Optional[CreateAssistantDtoVoice]` — These are the options for the assistant's voice.
    
</dd>
</dl>

<dl>
<dd>

**first_message_mode:** `typing.Optional[CreateAssistantDtoFirstMessageMode]` 

This is the mode for the first message. Default is 'assistant-speaks-first'.

Use:

- 'assistant-speaks-first' to have the assistant speak first.
- 'assistant-waits-for-user' to have the assistant wait for the user to speak first.
- 'assistant-speaks-first-with-model-generated-message' to have the assistant speak first with a message generated by the model based on the conversation state. (`assistant.model.messages` at call start, `call.messages` at squad transfer points).

@default 'assistant-speaks-first'
    
</dd>
</dl>

<dl>
<dd>

**hipaa_enabled:** `typing.Optional[bool]` — When this is enabled, no logs, recordings, or transcriptions will be stored. At the end of the call, you will still receive an end-of-call-report message to store on your server. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**client_messages:** `typing.Optional[typing.Sequence[CreateAssistantDtoClientMessagesItem]]` — These are the messages that will be sent to your Client SDKs. Default is conversation-update,function-call,hang,model-output,speech-update,status-update,transcript,tool-calls,user-interrupted,voice-input. You can check the shape of the messages in ClientMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**server_messages:** `typing.Optional[typing.Sequence[CreateAssistantDtoServerMessagesItem]]` — These are the messages that will be sent to your Server URL. Default is conversation-update,end-of-call-report,function-call,hang,speech-update,status-update,tool-calls,transfer-destination-request,user-interrupted. You can check the shape of the messages in ServerMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**silence_timeout_seconds:** `typing.Optional[float]` 

How many seconds of silence to wait before ending the call. Defaults to 30.

@default 30
    
</dd>
</dl>

<dl>
<dd>

**max_duration_seconds:** `typing.Optional[float]` 

This is the maximum number of seconds that the call will last. When the call reaches this duration, it will be ended.

@default 600 (10 minutes)
    
</dd>
</dl>

<dl>
<dd>

**background_sound:** `typing.Optional[CreateAssistantDtoBackgroundSound]` — This is the background sound in the call. Default for phone calls is 'office' and default for web calls is 'off'.
    
</dd>
</dl>

<dl>
<dd>

**backchanneling_enabled:** `typing.Optional[bool]` 

This determines whether the model says 'mhmm', 'ahem' etc. while user is speaking.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**background_denoising_enabled:** `typing.Optional[bool]` 

This enables filtering of noise and background speech while the user is talking.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**model_output_in_messages_enabled:** `typing.Optional[bool]` 

This determines whether the model's output is used in conversation history rather than the transcription of assistant's speech.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**transport_configurations:** `typing.Optional[typing.Sequence[TransportConfigurationTwilio]]` — These are the configurations to be passed to the transport providers of assistant's calls, like Twilio. You can store multiple configurations for different transport providers. For a call, only the configuration matching the call transport provider is used.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

This is the name of the assistant.

This is required when you want to transfer between assistants in a call.
    
</dd>
</dl>

<dl>
<dd>

**first_message:** `typing.Optional[str]` 

This is the first message that the assistant will say. This can also be a URL to a containerized audio file (mp3, wav, etc.).

If unspecified, assistant will wait for user to speak and use the model to respond once they speak.
    
</dd>
</dl>

<dl>
<dd>

**voicemail_detection:** `typing.Optional[TwilioVoicemailDetection]` 

These are the settings to configure or disable voicemail detection. Alternatively, voicemail detection can be configured using the model.tools=[VoicemailTool].
This uses Twilio's built-in detection while the VoicemailTool relies on the model to detect if a voicemail was reached.
You can use neither of them, one of them, or both of them. By default, Twilio built-in detection is enabled while VoicemailTool is not.
    
</dd>
</dl>

<dl>
<dd>

**voicemail_message:** `typing.Optional[str]` 

This is the message that the assistant will say if the call is forwarded to voicemail.

If unspecified, it will hang up.
    
</dd>
</dl>

<dl>
<dd>

**end_call_message:** `typing.Optional[str]` 

This is the message that the assistant will say if it ends the call.

If unspecified, it will hang up without saying anything.
    
</dd>
</dl>

<dl>
<dd>

**end_call_phrases:** `typing.Optional[typing.Sequence[str]]` — This list contains phrases that, if spoken by the assistant, will trigger the call to be hung up. Case insensitive.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — This is for metadata you want to store on the assistant.
    
</dd>
</dl>

<dl>
<dd>

**server_url:** `typing.Optional[str]` 

This is the URL Vapi will communicate with via HTTP GET and POST Requests. This is used for retrieving context, function calling, and end-of-call reports.

All requests will be sent with the call object among other things relevant to that message. You can find more details in the Server URL documentation.

This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: tool.server.url > assistant.serverUrl > phoneNumber.serverUrl > org.serverUrl
    
</dd>
</dl>

<dl>
<dd>

**server_url_secret:** `typing.Optional[str]` 

This is the secret you can set that Vapi will send with every request to your server. Will be sent as a header called x-vapi-secret.

Same precedence logic as serverUrl.
    
</dd>
</dl>

<dl>
<dd>

**analysis_plan:** `typing.Optional[AnalysisPlan]` — This is the plan for analysis of assistant's calls. Stored in `call.analysis`.
    
</dd>
</dl>

<dl>
<dd>

**artifact_plan:** `typing.Optional[ArtifactPlan]` 

This is the plan for artifacts generated during assistant's calls. Stored in `call.artifact`.

Note: `recordingEnabled` is currently at the root level. It will be moved to `artifactPlan` in the future, but will remain backwards compatible.
    
</dd>
</dl>

<dl>
<dd>

**message_plan:** `typing.Optional[MessagePlan]` 

This is the plan for static predefined messages that can be spoken by the assistant during the call, like `idleMessages`.

Note: `firstMessage`, `voicemailMessage`, and `endCallMessage` are currently at the root level. They will be moved to `messagePlan` in the future, but will remain backwards compatible.
    
</dd>
</dl>

<dl>
<dd>

**start_speaking_plan:** `typing.Optional[StartSpeakingPlan]` 

This is the plan for when the assistant should start talking.

You should configure this if you're running into these issues:

- The assistant is too slow to start talking after the customer is done speaking.
- The assistant is too fast to start talking after the customer is done speaking.
- The assistant is so fast that it's actually interrupting the customer.
    
</dd>
</dl>

<dl>
<dd>

**stop_speaking_plan:** `typing.Optional[StopSpeakingPlan]` 

This is the plan for when assistant should stop talking on customer interruption.

You should configure this if you're running into these issues:

- The assistant is too slow to recognize customer's interruption.
- The assistant is too fast to recognize customer's interruption.
- The assistant is getting interrupted by phrases that are just acknowledgments.
- The assistant is getting interrupted by background noises.
- The assistant is not properly stopping -- it starts talking right after getting interrupted.
    
</dd>
</dl>

<dl>
<dd>

**monitor_plan:** `typing.Optional[MonitorPlan]` 

This is the plan for real-time monitoring of the assistant's calls.

Usage:

- To enable live listening of the assistant's calls, set `monitorPlan.listenEnabled` to `true`.
- To enable live control of the assistant's calls, set `monitorPlan.controlEnabled` to `true`.

Note, `serverMessages`, `clientMessages`, `serverUrl` and `serverUrlSecret` are currently at the root level but will be moved to `monitorPlan` in the future. Will remain backwards compatible
    
</dd>
</dl>

<dl>
<dd>

**credential_ids:** `typing.Optional[typing.Sequence[str]]` — These are the credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can provide a subset using this.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.assistants.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.assistants.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assistants.<a href="src/vapi/assistants/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.assistants.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transcriber:** `typing.Optional[UpdateAssistantDtoTranscriber]` — These are the options for the assistant's transcriber.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[UpdateAssistantDtoModel]` — These are the options for the assistant's LLM.
    
</dd>
</dl>

<dl>
<dd>

**voice:** `typing.Optional[UpdateAssistantDtoVoice]` — These are the options for the assistant's voice.
    
</dd>
</dl>

<dl>
<dd>

**first_message_mode:** `typing.Optional[UpdateAssistantDtoFirstMessageMode]` 

This is the mode for the first message. Default is 'assistant-speaks-first'.

Use:
- 'assistant-speaks-first' to have the assistant speak first.
- 'assistant-waits-for-user' to have the assistant wait for the user to speak first.
- 'assistant-speaks-first-with-model-generated-message' to have the assistant speak first with a message generated by the model based on the conversation state. (`assistant.model.messages` at call start, `call.messages` at squad transfer points).

@default 'assistant-speaks-first'
    
</dd>
</dl>

<dl>
<dd>

**hipaa_enabled:** `typing.Optional[bool]` — When this is enabled, no logs, recordings, or transcriptions will be stored. At the end of the call, you will still receive an end-of-call-report message to store on your server. Defaults to false.
    
</dd>
</dl>

<dl>
<dd>

**client_messages:** `typing.Optional[typing.Sequence[UpdateAssistantDtoClientMessagesItem]]` — These are the messages that will be sent to your Client SDKs. Default is conversation-update,function-call,hang,model-output,speech-update,status-update,transcript,tool-calls,user-interrupted,voice-input. You can check the shape of the messages in ClientMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**server_messages:** `typing.Optional[typing.Sequence[UpdateAssistantDtoServerMessagesItem]]` — These are the messages that will be sent to your Server URL. Default is conversation-update,end-of-call-report,function-call,hang,speech-update,status-update,tool-calls,transfer-destination-request,user-interrupted. You can check the shape of the messages in ServerMessage schema.
    
</dd>
</dl>

<dl>
<dd>

**silence_timeout_seconds:** `typing.Optional[float]` 

How many seconds of silence to wait before ending the call. Defaults to 30.

@default 30
    
</dd>
</dl>

<dl>
<dd>

**max_duration_seconds:** `typing.Optional[float]` 

This is the maximum number of seconds that the call will last. When the call reaches this duration, it will be ended.

@default 600 (10 minutes)
    
</dd>
</dl>

<dl>
<dd>

**background_sound:** `typing.Optional[UpdateAssistantDtoBackgroundSound]` — This is the background sound in the call. Default for phone calls is 'office' and default for web calls is 'off'.
    
</dd>
</dl>

<dl>
<dd>

**backchanneling_enabled:** `typing.Optional[bool]` 

This determines whether the model says 'mhmm', 'ahem' etc. while user is speaking.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**background_denoising_enabled:** `typing.Optional[bool]` 

This enables filtering of noise and background speech while the user is talking.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**model_output_in_messages_enabled:** `typing.Optional[bool]` 

This determines whether the model's output is used in conversation history rather than the transcription of assistant's speech.

Default `false` while in beta.

@default false
    
</dd>
</dl>

<dl>
<dd>

**transport_configurations:** `typing.Optional[typing.Sequence[TransportConfigurationTwilio]]` — These are the configurations to be passed to the transport providers of assistant's calls, like Twilio. You can store multiple configurations for different transport providers. For a call, only the configuration matching the call transport provider is used.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 

This is the name of the assistant.

This is required when you want to transfer between assistants in a call.
    
</dd>
</dl>

<dl>
<dd>

**first_message:** `typing.Optional[str]` 

This is the first message that the assistant will say. This can also be a URL to a containerized audio file (mp3, wav, etc.).

If unspecified, assistant will wait for user to speak and use the model to respond once they speak.
    
</dd>
</dl>

<dl>
<dd>

**voicemail_detection:** `typing.Optional[TwilioVoicemailDetection]` 

These are the settings to configure or disable voicemail detection. Alternatively, voicemail detection can be configured using the model.tools=[VoicemailTool].
This uses Twilio's built-in detection while the VoicemailTool relies on the model to detect if a voicemail was reached.
You can use neither of them, one of them, or both of them. By default, Twilio built-in detection is enabled while VoicemailTool is not.
    
</dd>
</dl>

<dl>
<dd>

**voicemail_message:** `typing.Optional[str]` 

This is the message that the assistant will say if the call is forwarded to voicemail.

If unspecified, it will hang up.
    
</dd>
</dl>

<dl>
<dd>

**end_call_message:** `typing.Optional[str]` 

This is the message that the assistant will say if it ends the call.

If unspecified, it will hang up without saying anything.
    
</dd>
</dl>

<dl>
<dd>

**end_call_phrases:** `typing.Optional[typing.Sequence[str]]` — This list contains phrases that, if spoken by the assistant, will trigger the call to be hung up. Case insensitive.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — This is for metadata you want to store on the assistant.
    
</dd>
</dl>

<dl>
<dd>

**server_url:** `typing.Optional[str]` 

This is the URL Vapi will communicate with via HTTP GET and POST Requests. This is used for retrieving context, function calling, and end-of-call reports.

All requests will be sent with the call object among other things relevant to that message. You can find more details in the Server URL documentation.

This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: tool.server.url > assistant.serverUrl > phoneNumber.serverUrl > org.serverUrl
    
</dd>
</dl>

<dl>
<dd>

**server_url_secret:** `typing.Optional[str]` 

This is the secret you can set that Vapi will send with every request to your server. Will be sent as a header called x-vapi-secret.

Same precedence logic as serverUrl.
    
</dd>
</dl>

<dl>
<dd>

**analysis_plan:** `typing.Optional[AnalysisPlan]` — This is the plan for analysis of assistant's calls. Stored in `call.analysis`.
    
</dd>
</dl>

<dl>
<dd>

**artifact_plan:** `typing.Optional[ArtifactPlan]` 

This is the plan for artifacts generated during assistant's calls. Stored in `call.artifact`.

Note: `recordingEnabled` is currently at the root level. It will be moved to `artifactPlan` in the future, but will remain backwards compatible.
    
</dd>
</dl>

<dl>
<dd>

**message_plan:** `typing.Optional[MessagePlan]` 

This is the plan for static predefined messages that can be spoken by the assistant during the call, like `idleMessages`.

Note: `firstMessage`, `voicemailMessage`, and `endCallMessage` are currently at the root level. They will be moved to `messagePlan` in the future, but will remain backwards compatible.
    
</dd>
</dl>

<dl>
<dd>

**start_speaking_plan:** `typing.Optional[StartSpeakingPlan]` 

This is the plan for when the assistant should start talking.

You should configure this if you're running into these issues:
- The assistant is too slow to start talking after the customer is done speaking.
- The assistant is too fast to start talking after the customer is done speaking.
- The assistant is so fast that it's actually interrupting the customer.
    
</dd>
</dl>

<dl>
<dd>

**stop_speaking_plan:** `typing.Optional[StopSpeakingPlan]` 

This is the plan for when assistant should stop talking on customer interruption.

You should configure this if you're running into these issues:
- The assistant is too slow to recognize customer's interruption.
- The assistant is too fast to recognize customer's interruption.
- The assistant is getting interrupted by phrases that are just acknowledgments.
- The assistant is getting interrupted by background noises.
- The assistant is not properly stopping -- it starts talking right after getting interrupted.
    
</dd>
</dl>

<dl>
<dd>

**monitor_plan:** `typing.Optional[MonitorPlan]` 

This is the plan for real-time monitoring of the assistant's calls.

Usage:
- To enable live listening of the assistant's calls, set `monitorPlan.listenEnabled` to `true`.
- To enable live control of the assistant's calls, set `monitorPlan.controlEnabled` to `true`.

Note, `serverMessages`, `clientMessages`, `serverUrl` and `serverUrlSecret` are currently at the root level but will be moved to `monitorPlan` in the future. Will remain backwards compatible
    
</dd>
</dl>

<dl>
<dd>

**credential_ids:** `typing.Optional[typing.Sequence[str]]` — These are the credentials that will be used for the assistant calls. By default, all the credentials are available for use in the call but you can provide a subset using this.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PhoneNumbers
<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.phone_numbers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.phone_numbers import PhoneNumbersCreateRequest_Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.phone_numbers.create(
    request=PhoneNumbersCreateRequest_Vapi(
        sip_uri="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PhoneNumbersCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.phone_numbers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.phone_numbers.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vapi/phone_numbers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.phone_numbers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fallback_destination:** `typing.Optional[UpdatePhoneNumberDtoFallbackDestination]` 

This is the fallback destination an inbound call will be transferred to if:
1. `assistantId` is not set
2. `squadId` is not set
3. and, `assistant-request` message to the `serverUrl` fails

If this is not set and above conditions are met, the inbound call is hung up with an error message.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the phone number. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` 

This is the assistant that will be used for incoming calls to this phone number.

If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` 

This is the squad that will be used for incoming calls to this phone number.

If neither `assistantId` nor `squadId` is set, `assistant-request` will be sent to your Server URL. Check `ServerMessage` and `ServerMessageResponse` for the shape of the message and response that is expected.
    
</dd>
</dl>

<dl>
<dd>

**server_url:** `typing.Optional[str]` 

This is the server URL where messages will be sent for calls on this number. This includes the `assistant-request` message.

You can see the shape of the messages sent in `ServerMessage`.

This overrides the `org.serverUrl`. Order of precedence: tool.server.url > assistant.serverUrl > phoneNumber.serverUrl > org.serverUrl.
    
</dd>
</dl>

<dl>
<dd>

**server_url_secret:** `typing.Optional[str]` 

This is the secret Vapi will send with every message to your server. It's sent as a header called x-vapi-secret.

Same precedence logic as serverUrl.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Squads
<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.squads.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import SquadMemberDto, Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.squads.create(
    members=[SquadMemberDto()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**members:** `typing.Sequence[SquadMemberDto]` 

This is the list of assistants that make up the squad.

The call will start with the first assistant in the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the squad.
    
</dd>
</dl>

<dl>
<dd>

**members_overrides:** `typing.Optional[AssistantOverrides]` 

This can be used to override all the assistants' settings and provide values for their template variables.

Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.squads.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.squads.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.squads.<a href="src/vapi/squads/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import SquadMemberDto, Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.squads.update(
    id="id",
    members=[SquadMemberDto()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**members:** `typing.Sequence[SquadMemberDto]` 

This is the list of assistants that make up the squad.

The call will start with the first assistant in the list.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the squad.
    
</dd>
</dl>

<dl>
<dd>

**members_overrides:** `typing.Optional[AssistantOverrides]` 

This can be used to override all the assistants' settings and provide values for their template variables.

Both `membersOverrides` and `members[n].assistantOverrides` can be used together. First, `members[n].assistantOverrides` is applied. Then, `membersOverrides` is applied as a global override.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Blocks
<details><summary><code>client.blocks.<a href="src/vapi/blocks/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.blocks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/vapi/blocks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.blocks import BlocksCreateRequest_Workflow

client = Vapi(
    token="YOUR_TOKEN",
)
client.blocks.create(
    request=BlocksCreateRequest_Workflow(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `BlocksCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/vapi/blocks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.blocks.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/vapi/blocks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.blocks.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.blocks.<a href="src/vapi/blocks/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.blocks.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.Sequence[UpdateBlockDtoMessagesItem]]` — These are the pre-configured messages that will be spoken to the user while the block is running.
    
</dd>
</dl>

<dl>
<dd>

**input_schema:** `typing.Optional[JsonSchema]` 

This is the input schema for the block. This is the input the block needs to run. It's given to the block as `steps[0].input`

These are accessible as variables:
- ({{input.propertyName}}) in context of the block execution (step)
- ({{stepName.input.propertyName}}) in context of the workflow
    
</dd>
</dl>

<dl>
<dd>

**output_schema:** `typing.Optional[JsonSchema]` 

This is the output schema for the block. This is the output the block will return to the workflow (`{{stepName.output}}`).

These are accessible as variables:
- ({{output.propertyName}}) in context of the block execution (step)
- ({{stepName.output.propertyName}}) in context of the workflow (read caveat #1)
- ({{blockName.output.propertyName}}) in context of the workflow (read caveat #2)

Caveats:
1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.output.propertyName}} will reference the latest usage of the step.
2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.output.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.
    
</dd>
</dl>

<dl>
<dd>

**tool:** `typing.Optional[UpdateBlockDtoTool]` — This is the tool that the block will call. To use an existing tool, use `toolId`.
    
</dd>
</dl>

<dl>
<dd>

**steps:** `typing.Optional[typing.Sequence[UpdateBlockDtoStepsItem]]` — These are the steps in the workflow.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the block. This is just for your reference.
    
</dd>
</dl>

<dl>
<dd>

**instruction:** `typing.Optional[str]` 

This is the instruction to the model.

You can reference any variable in the context of the current block execution (step):
- "{{input.your-property-name}}" for the current step's input
- "{{your-step-name.output.your-property-name}}" for another step's output (in the same workflow; read caveat #1)
- "{{your-step-name.input.your-property-name}}" for another step's input (in the same workflow; read caveat #1)
- "{{your-block-name.output.your-property-name}}" for another block's output (in the same workflow; read caveat #2)
- "{{your-block-name.input.your-property-name}}" for another block's input (in the same workflow; read caveat #2)
- "{{workflow.input.your-property-name}}" for the current workflow's input
- "{{global.your-property-name}}" for the global context

This can be as simple or as complex as you want it to be.
- "say hello and ask the user about their day!"
- "collect the user's first and last name"
- "user is {{input.firstName}} {{input.lastName}}. their age is {{input.age}}. ask them about their salary and if they might be interested in buying a house. we offer {{input.offer}}"

Caveats:
1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.output/input.propertyName}} will reference the latest usage of the step.
2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.output/input.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow with steps.
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `typing.Optional[str]` — This is the id of the tool that the block will call. To use a transient tool, use `tool`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tools
<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.tools.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi
from vapi.tools import ToolsCreateRequest_Output

client = Vapi(
    token="YOUR_TOKEN",
)
client.tools.create(
    request=ToolsCreateRequest_Output(
        async_=False,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ToolsCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.tools.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.tools.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.<a href="src/vapi/tools/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.tools.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[bool]` 

This determines if the tool is async.

If async, the assistant will move forward without waiting for your server to respond. This is useful if you just want to trigger something on your server.

If sync, the assistant will wait for your server to respond. This is useful if want assistant to respond with the result from your server.

Defaults to synchronous (`false`).
    
</dd>
</dl>

<dl>
<dd>

**messages:** `typing.Optional[typing.Sequence[UpdateToolDtoMessagesItem]]` 

These are the messages that will be spoken to the user as the tool is running.

For some tools, this is auto-filled based on special fields like `tool.destinations`. For others like the function tool, these can be custom configured.
    
</dd>
</dl>

<dl>
<dd>

**function:** `typing.Optional[OpenAiFunction]` 

This is the function definition of the tool.

For `endCall`, `transferCall`, and `dtmf` tools, this is auto-filled based on tool-specific fields like `tool.destinations`. But, even in those cases, you can provide a custom function definition for advanced use cases.

An example of an advanced use case is if you want to customize the message that's spoken for `endCall` tool. You can specify a function where it returns an argument "reason". Then, in `messages` array, you can have many "request-complete" messages. One of these messages will be triggered if the `messages[].conditions` matches the "reason" argument.
    
</dd>
</dl>

<dl>
<dd>

**server:** `typing.Optional[Server]` 

This is the server that will be hit when this tool is requested by the model.

All requests will be sent with the call object among other things. You can find more details in the Server URL documentation.

This overrides the serverUrl set on the org and the phoneNumber. Order of precedence: highest tool.server.url, then assistant.serverUrl, then phoneNumber.serverUrl, then org.serverUrl.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/vapi/files/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.files.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/vapi/files/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.files.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/vapi/files/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.files.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/vapi/files/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.files.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/vapi/files/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.files.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — This is the name of the file. This is just for your own reference.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Analytics
<details><summary><code>client.analytics.<a href="src/vapi/analytics/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import AnalyticsOperation, AnalyticsQuery, Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
client.analytics.get(
    queries=[
        AnalyticsQuery(
            name="name",
            operations=[
                AnalyticsOperation(
                    operation="sum",
                    column="id",
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**queries:** `typing.Sequence[AnalyticsQuery]` — This is the list of metric queries you want to perform.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Logs
<details><summary><code>client.logs.<a href="src/vapi/logs/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN",
)
response = client.logs.get()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**org_id:** `typing.Optional[str]` — This is the unique identifier for the org that this log belongs to.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[LogsGetRequestType]` — This is the type of the log.
    
</dd>
</dl>

<dl>
<dd>

**assistant_id:** `typing.Optional[str]` — This is the ID of the assistant.
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` — This is the ID of the phone number.
    
</dd>
</dl>

<dl>
<dd>

**customer_id:** `typing.Optional[str]` — This is the ID of the customer.
    
</dd>
</dl>

<dl>
<dd>

**squad_id:** `typing.Optional[str]` — This is the ID of the squad.
    
</dd>
</dl>

<dl>
<dd>

**call_id:** `typing.Optional[str]` — This is the ID of the call.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[float]` — This is the page number to return. Defaults to 1.
    
</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[LogsGetRequestSortOrder]` — This is the sort order for pagination. Defaults to 'ASC'.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[float]` — This is the maximum number of items to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**created_at_le:** `typing.Optional[dt.datetime]` — This will return items where the createdAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_ge:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**updated_at_le:** `typing.Optional[dt.datetime]` — This will return items where the updatedAt is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

