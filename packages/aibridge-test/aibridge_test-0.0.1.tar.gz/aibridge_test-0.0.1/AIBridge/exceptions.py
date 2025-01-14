"""
Exception  handling
"""


class AIBridgeException(Exception):
    pass


class OpenAIException(AIBridgeException):
    pass


class ConfigException(AIBridgeException):
    pass


class ValidationException(AIBridgeException):
    pass


class PromptSaveException(AIBridgeException):
    pass


class VaribalesException(AIBridgeException):
    pass


class PromptCompletionException(AIBridgeException):
    pass


class AssignQueueException(AIBridgeException):
    pass


class ProcessMQException(AIBridgeException):
    pass


class AIResponseException(AIBridgeException):
    pass


class MessageQueueException(AIBridgeException):
    pass


class DatabaseException(AIBridgeException):
    pass


class ImageException(AIBridgeException):
    pass
