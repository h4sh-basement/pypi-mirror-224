import typing_extensions

from humanloop.apis.tags import TagValues
from humanloop.apis.tags.projects_api import ProjectsApi
from humanloop.apis.tags.testsets_api import TestsetsApi
from humanloop.apis.tags.experiments_api import ExperimentsApi
from humanloop.apis.tags.completions_api import CompletionsApi
from humanloop.apis.tags.chats_api import ChatsApi
from humanloop.apis.tags.evaluators_api import EvaluatorsApi
from humanloop.apis.tags.evaluations_api import EvaluationsApi
from humanloop.apis.tags.logs_api import LogsApi
from humanloop.apis.tags.sessions_api import SessionsApi
from humanloop.apis.tags.testcases_api import TestcasesApi
from humanloop.apis.tags.model_configs_api import ModelConfigsApi
from humanloop.apis.tags.feedback_api import FeedbackApi
from humanloop.apis.tags.authentication_api import AuthenticationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PROJECTS: ProjectsApi,
        TagValues.TESTSETS: TestsetsApi,
        TagValues.EXPERIMENTS: ExperimentsApi,
        TagValues.COMPLETIONS: CompletionsApi,
        TagValues.CHATS: ChatsApi,
        TagValues.EVALUATORS: EvaluatorsApi,
        TagValues.EVALUATIONS: EvaluationsApi,
        TagValues.LOGS: LogsApi,
        TagValues.SESSIONS: SessionsApi,
        TagValues.TESTCASES: TestcasesApi,
        TagValues.MODEL_CONFIGS: ModelConfigsApi,
        TagValues.FEEDBACK: FeedbackApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PROJECTS: ProjectsApi,
        TagValues.TESTSETS: TestsetsApi,
        TagValues.EXPERIMENTS: ExperimentsApi,
        TagValues.COMPLETIONS: CompletionsApi,
        TagValues.CHATS: ChatsApi,
        TagValues.EVALUATORS: EvaluatorsApi,
        TagValues.EVALUATIONS: EvaluationsApi,
        TagValues.LOGS: LogsApi,
        TagValues.SESSIONS: SessionsApi,
        TagValues.TESTCASES: TestcasesApi,
        TagValues.MODEL_CONFIGS: ModelConfigsApi,
        TagValues.FEEDBACK: FeedbackApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
    }
)
