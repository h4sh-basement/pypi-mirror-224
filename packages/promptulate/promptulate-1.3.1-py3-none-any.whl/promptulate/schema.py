from abc import abstractmethod
from enum import Enum
from typing import List, Dict, Callable, Any, Optional

from pydantic import BaseModel, Field

__all__ = [
    "LLMType",
    "BaseMessage",
    "CompletionMessage",
    "SystemMessage",
    "UserMessage",
    "AssistantMessage",
    "MessageSet",
    "init_chat_message_history",
]


class BaseMessage(BaseModel):
    """Message basic object."""

    content: str
    additional_kwargs: dict = Field(default_factory=dict)

    @property
    @abstractmethod
    def type(self) -> str:
        """Type of the message, used for serialization."""


class CompletionMessage(BaseMessage):
    """Type of completion message. Used in OpenAI currently"""

    @property
    def type(self) -> str:
        return "completion"


class SystemMessage(BaseMessage):
    """Type of message that is a system message. Currently used in OpenAI."""

    @property
    def type(self) -> str:
        """Type of the message, used for serialization."""
        return "system"


class UserMessage(BaseMessage):
    """Type of message that is a user message. Currently used in OpenAI."""

    @property
    def type(self) -> str:
        return "user"


class AssistantMessage(BaseMessage):
    """Type of message that is an assistant message. Currently used in OpenAI."""

    @property
    def type(self) -> str:
        return "assistant"


MESSAGE_TYPE = {
    "completion": CompletionMessage,
    "system": SystemMessage,
    "user": UserMessage,
    "assistant": AssistantMessage,
}


class LLMType(str, Enum):
    """All LLM type here"""

    OpenAI = "OpenAI"
    ChatOpenAI = "ChatOpenAI"


class MessageSet(BaseModel):
    """MessageSet can be used in Memory, LLMs, Framework and some else.
    It's a universal chat message format in promptulate.
    """

    messages: List[BaseMessage] = []
    conversation_id: Optional[str] = None
    """Used to memory"""

    @classmethod
    def from_listdict_data(cls, value: List[Dict]) -> "MessageSet":
        """initialize MessageSet from a List[Dict] data

        Args:
            value(List[Dict]): the example is as follow:
                [
                    {"type": "user", "content": "This is a message1."},
                    {"type": "assistant", "content": "This is a message2."}
                ]

        Returns:
            initialized MessageSet
        """
        messages: List[BaseMessage] = [
            MESSAGE_TYPE[item["role"]](content=item["content"]) for item in value
        ]
        return cls(messages=messages)

    @property
    def listdict_messages(self) -> List[Dict]:
        converted_messages = []
        for message in self.messages:
            converted_messages.append(
                {"role": message.type, "content": message.content}
            )
        return converted_messages

    @property
    def memory_messages(self) -> List[Dict]:
        return self.listdict_messages

    def to_llm_prompt(self, llm_type: LLMType) -> Any:
        """Convert the MessageSet messages to specified llm prompt"""
        if not llm_type:
            ValueError(
                "Missing llm_type, you should pass a llm_type if you want to use llm_prompt"
            )
        return _to_llm_prompt[llm_type](self)

    @property
    def string_messages(self) -> str:
        """Convert the message to a string type, it can be used as a prompt for OpenAI completion."""
        string_result = ""
        for message in self.messages:
            string_result += f"{message.content}\n"
        return string_result

    def add_completion_message(self, message: str) -> None:
        self.messages.append(CompletionMessage(content=message))

    def add_system_message(self, message: str) -> None:
        self.messages.append(SystemMessage(content=message))

    def add_user_message(self, message: str) -> None:
        self.messages.append(UserMessage(content=message))

    def add_ai_message(self, message: str) -> None:
        self.messages.append(AssistantMessage(content=message))


def init_chat_message_history(system_content, user_content) -> MessageSet:
    messages = [
        SystemMessage(content=system_content),
        UserMessage(content=user_content),
    ]
    return MessageSet(messages=messages)


def _to_openai_llm_prompt(message_set: MessageSet) -> str:
    return message_set.string_messages


def _to_chat_openai_llm_prompt(message_set: MessageSet) -> List[Dict]:
    return message_set.listdict_messages


_to_llm_prompt: Dict[LLMType, Callable] = {
    LLMType.OpenAI: _to_openai_llm_prompt,
    LLMType.ChatOpenAI: _to_chat_openai_llm_prompt,
}
