# coding: utf-8
"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.0
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from humanloop.client_custom import ClientCustom
from humanloop.configuration import Configuration
from humanloop.api_client import ApiClient
from humanloop.type_util import copy_signature
from humanloop.apis.tags.chats_api import ChatsApi
from humanloop.apis.tags.completions_api import CompletionsApi
from humanloop.apis.tags.evaluations_api import EvaluationsApi
from humanloop.apis.tags.evaluators_api import EvaluatorsApi
from humanloop.apis.tags.experiments_api import ExperimentsApi
from humanloop.apis.tags.feedback_api import FeedbackApi
from humanloop.apis.tags.logs_api import LogsApi
from humanloop.apis.tags.model_configs_api import ModelConfigsApi
from humanloop.apis.tags.projects_api import ProjectsApi
from humanloop.apis.tags.sessions_api import SessionsApi
from humanloop.apis.tags.testcases_api import TestcasesApi
from humanloop.apis.tags.testsets_api import TestsetsApi

from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.chat_message import ChatMessage
from humanloop.type.chat_request import ChatRequest
from humanloop.type.chat_response import ChatResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.model_config_chat_request import ModelConfigChatRequest
from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.chat_message import ChatMessage
from humanloop.type.chat_deployed_request import ChatDeployedRequest
from humanloop.type.chat_response import ChatResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.chat_message import ChatMessage
from humanloop.type.chat_experiment_request import ChatExperimentRequest
from humanloop.type.chat_response import ChatResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.chat_model_config_request import ChatModelConfigRequest
from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.chat_message import ChatMessage
from humanloop.type.chat_response import ChatResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.model_config_completion_request import ModelConfigCompletionRequest
from humanloop.type.completion_request import CompletionRequest
from humanloop.type.completion_response import CompletionResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.completion_deployed_request import CompletionDeployedRequest
from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.completion_response import CompletionResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.completion_experiment_request import CompletionExperimentRequest
from humanloop.type.completion_response import CompletionResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.completion_model_config_request import CompletionModelConfigRequest
from humanloop.type.completion_response import CompletionResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.feedback_submit_request import FeedbackSubmitRequest
from humanloop.type.feedback_type import FeedbackType
from humanloop.type.feedback_submit_response import FeedbackSubmitResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.feedback import Feedback
from humanloop.type.chat_message import ChatMessage
from humanloop.type.agent_config_request import AgentConfigRequest
from humanloop.type.generic_config_request import GenericConfigRequest
from humanloop.type.tool_config_request import ToolConfigRequest
from humanloop.type.model_config_request import ModelConfigRequest
from humanloop.type.logs_log_response import LogsLogResponse
from humanloop.type.log_datapoint_request import LogDatapointRequest
from humanloop.type.http_validation_error import HTTPValidationError


class Humanloop(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.chats: ChatsApi = ChatsApi(api_client)
        self.completions: CompletionsApi = CompletionsApi(api_client)
        self.evaluations: EvaluationsApi = EvaluationsApi(api_client)
        self.evaluators: EvaluatorsApi = EvaluatorsApi(api_client)
        self.experiments: ExperimentsApi = ExperimentsApi(api_client)
        self.feedback_api: FeedbackApi = FeedbackApi(api_client)
        self.logs: LogsApi = LogsApi(api_client)
        self.model_configs: ModelConfigsApi = ModelConfigsApi(api_client)
        self.projects: ProjectsApi = ProjectsApi(api_client)
        self.sessions: SessionsApi = SessionsApi(api_client)
        self.testcases: TestcasesApi = TestcasesApi(api_client)
        self.testsets: TestsetsApi = TestsetsApi(api_client)

    @copy_signature(ChatsApi.acreate)
    async def achat(
        self,
        messages: typing.List[ChatMessage],
        model_config: ModelConfigChatRequest,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
    ):
        return await self.chats.acreate(
            messages=messages,
            model_config=model_config,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
        )

    @copy_signature(ChatsApi.create)
    def chat(
        self,
        messages: typing.List[ChatMessage],
        model_config: ModelConfigChatRequest,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
    ):
        return self.chats.create(
            messages=messages,
            model_config=model_config,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
        )

    @copy_signature(ChatsApi.acreate_deployed)
    async def achat_deployed(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ):
        return await self.chats.acreate_deployed(
            messages=messages,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
            environment=environment,
        )

    @copy_signature(ChatsApi.create_deployed)
    def chat_deployed(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ):
        return self.chats.create_deployed(
            messages=messages,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
            environment=environment,
        )

    @copy_signature(ChatsApi.acreate_experiment)
    async def achat_experiment(
        self,
        messages: typing.List[ChatMessage],
        experiment_id: str,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
    ):
        return await self.chats.acreate_experiment(
            messages=messages,
            experiment_id=experiment_id,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
        )

    @copy_signature(ChatsApi.create_experiment)
    def chat_experiment(
        self,
        messages: typing.List[ChatMessage],
        experiment_id: str,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
    ):
        return self.chats.create_experiment(
            messages=messages,
            experiment_id=experiment_id,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
        )

    @copy_signature(ChatsApi.acreate_model_config)
    async def achat_model_config(
        self,
        messages: typing.List[ChatMessage],
        model_config_id: str,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
    ):
        return await self.chats.acreate_model_config(
            messages=messages,
            model_config_id=model_config_id,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
        )

    @copy_signature(ChatsApi.create_model_config)
    def chat_model_config(
        self,
        messages: typing.List[ChatMessage],
        model_config_id: str,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
    ):
        return self.chats.create_model_config(
            messages=messages,
            model_config_id=model_config_id,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
        )

    @copy_signature(CompletionsApi.acreate)
    async def acomplete(
        self,
        model_config: ModelConfigCompletionRequest,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
    ):
        return await self.completions.acreate(
            model_config=model_config,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
        )

    @copy_signature(CompletionsApi.create)
    def complete(
        self,
        model_config: ModelConfigCompletionRequest,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
    ):
        return self.completions.create(
            model_config=model_config,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
        )

    @copy_signature(CompletionsApi.acreate_deployed)
    async def acomplete_deployed(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ):
        return await self.completions.acreate_deployed(
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
            environment=environment,
        )

    @copy_signature(CompletionsApi.create_deployed)
    def complete_deployed(
        self,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        environment: typing.Optional[str] = None,
    ):
        return self.completions.create_deployed(
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
            environment=environment,
        )

    @copy_signature(CompletionsApi.acreate_experiment)
    async def acomplete_experiment(
        self,
        experiment_id: str,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
    ):
        return await self.completions.acreate_experiment(
            experiment_id=experiment_id,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
        )

    @copy_signature(CompletionsApi.create_experiment)
    def complete_experiment(
        self,
        experiment_id: str,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
    ):
        return self.completions.create_experiment(
            experiment_id=experiment_id,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
        )

    @copy_signature(CompletionsApi.acreate_model_config)
    async def acomplete_model_configuration(
        self,
        model_config_id: str,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
    ):
        return await self.completions.acreate_model_config(
            model_config_id=model_config_id,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
        )

    @copy_signature(CompletionsApi.create_model_config)
    def complete_model_configuration(
        self,
        model_config_id: str,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        logprobs: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        suffix: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
    ):
        return self.completions.create_model_config(
            model_config_id=model_config_id,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            user=user,
        )

    @copy_signature(FeedbackApi.afeedback)
    async def afeedback(
        self,
        body: typing.Optional[FeedbackSubmitRequest] = None,
        type: typing.Optional[typing.Union[FeedbackType, str]] = None,
        value: typing.Optional[str] = None,
        data_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        unset: typing.Optional[bool] = None,
    ):
        return await self.feedback_api.afeedback(
            body=body,
            type=type,
            value=value,
            data_id=data_id,
            user=user,
            created_at=created_at,
            unset=unset,
        )

    @copy_signature(FeedbackApi.feedback)
    def feedback(
        self,
        body: typing.Optional[FeedbackSubmitRequest] = None,
        type: typing.Optional[typing.Union[FeedbackType, str]] = None,
        value: typing.Optional[str] = None,
        data_id: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        unset: typing.Optional[bool] = None,
    ):
        return self.feedback_api.feedback(
            body=body,
            type=type,
            value=value,
            data_id=data_id,
            user=user,
            created_at=created_at,
            unset=unset,
        )

    @copy_signature(LogsApi.alog)
    async def alog(
        self,
        body: typing.Optional[LogDatapointRequest] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        reference_id: typing.Optional[str] = None,
        trial_id: typing.Optional[str] = None,
        messages: typing.Optional[typing.List[ChatMessage]] = None,
        output: typing.Optional[str] = None,
        config: typing.Optional[typing.Union[ModelConfigRequest, ToolConfigRequest, GenericConfigRequest, AgentConfigRequest]] = None,
        feedback: typing.Optional[typing.Union[Feedback, typing.List[Feedback]]] = None,
        created_at: typing.Optional[datetime] = None,
        error: typing.Optional[str] = None,
        duration: typing.Optional[typing.Union[int, float]] = None,
    ):
        return await self.logs.alog(
            body=body,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            reference_id=reference_id,
            trial_id=trial_id,
            messages=messages,
            output=output,
            config=config,
            feedback=feedback,
            created_at=created_at,
            error=error,
            duration=duration,
        )

    @copy_signature(LogsApi.log)
    def log(
        self,
        body: typing.Optional[LogDatapointRequest] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        reference_id: typing.Optional[str] = None,
        trial_id: typing.Optional[str] = None,
        messages: typing.Optional[typing.List[ChatMessage]] = None,
        output: typing.Optional[str] = None,
        config: typing.Optional[typing.Union[ModelConfigRequest, ToolConfigRequest, GenericConfigRequest, AgentConfigRequest]] = None,
        feedback: typing.Optional[typing.Union[Feedback, typing.List[Feedback]]] = None,
        created_at: typing.Optional[datetime] = None,
        error: typing.Optional[str] = None,
        duration: typing.Optional[typing.Union[int, float]] = None,
    ):
        return self.logs.log(
            body=body,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            reference_id=reference_id,
            trial_id=trial_id,
            messages=messages,
            output=output,
            config=config,
            feedback=feedback,
            created_at=created_at,
            error=error,
            duration=duration,
        )
