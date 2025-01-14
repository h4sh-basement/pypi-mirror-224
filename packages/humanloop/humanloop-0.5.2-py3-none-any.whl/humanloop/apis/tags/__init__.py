# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from humanloop.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PROJECTS = "Projects"
    TESTSETS = "Testsets"
    EXPERIMENTS = "Experiments"
    COMPLETIONS = "Completions"
    CHATS = "Chats"
    EVALUATORS = "Evaluators"
    EVALUATIONS = "Evaluations"
    LOGS = "Logs"
    SESSIONS = "Sessions"
    TESTCASES = "Testcases"
    MODEL_CONFIGS = "Model Configs"
    FEEDBACK = "Feedback"
    AUTHENTICATION = "Authentication"
