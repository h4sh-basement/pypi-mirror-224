# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal

from humanloop.type.chat_message import ChatMessage
from humanloop.type.model_config_tool_request import ModelConfigToolRequest
from humanloop.type.model_endpoints import ModelEndpoints
from humanloop.type.model_providers import ModelProviders

class RequiredProjectModelConfigRequest(TypedDict):
    # The model instance used. E.g. text-davinci-002.
    model: str

    # Unique project name. If it does not exist, a new project will be created.
    project: str

class OptionalProjectModelConfigRequest(TypedDict, total=False):
    # A description of the model config.
    description: str

    # A friendly display name for the model config. If not provided, a name will be generated.
    name: str

    # The company providing the underlying model service.
    provider: ModelProviders

    # The maximum number of tokens to generate. Provide max_tokens=-1 to dynamically calculate the maximum number of tokens to generate given the length of the prompt
    max_tokens: int

    # What sampling temperature to use when making a generation. Higher values means the model will be more creative.
    temperature: typing.Union[int, float]

    # An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass.
    top_p: typing.Union[int, float]

    # The string (or list of strings) after which the model will stop generating. The returned text will not contain the stop sequence.
    stop: typing.Union[str, typing.List[str]]

    # Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the generation so far.
    presence_penalty: typing.Union[int, float]

    # Number between -2.0 and 2.0. Positive values penalize new tokens based on how frequently they appear in the generation so far.
    frequency_penalty: typing.Union[int, float]

    # Other parameter values to be passed to the provider call.
    other: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # If specified, the model config will be added to this experiment. Experiments are used for A/B testing and optimizing hyperparameters.
    experiment: str

    # Prompt template that will take your specified inputs to form your final request to the provider model. NB: Input variables within the prompt template should be specified with syntax: {{INPUT_NAME}}.
    prompt_template: str

    # Messages prepended to the list of messages sent to the provider. These messages that will take your specified inputs to form your final request to the provider model. NB: Input variables within the prompt template should be specified with syntax: {{INPUT_NAME}}.
    chat_template: typing.List[ChatMessage]

    # Which of the providers model endpoints to use. For example Complete or Edit.
    endpoint: ModelEndpoints

    # Make tools available to OpenAIs chat model as functions.
    tools: typing.List[ModelConfigToolRequest]

class ProjectModelConfigRequest(RequiredProjectModelConfigRequest, OptionalProjectModelConfigRequest):
    pass
