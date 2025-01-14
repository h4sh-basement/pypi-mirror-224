# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChatMessageRole(str, enum.Enum):
    """
    * `SYSTEM` - System
    * `ASSISTANT` - Assistant
    * `USER` - User
    * `FUNCTION` - Function
    """

    SYSTEM = "SYSTEM"
    ASSISTANT = "ASSISTANT"
    USER = "USER"
    FUNCTION = "FUNCTION"

    def visit(
        self,
        system: typing.Callable[[], T_Result],
        assistant: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
        function: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMessageRole.SYSTEM:
            return system()
        if self is ChatMessageRole.ASSISTANT:
            return assistant()
        if self is ChatMessageRole.USER:
            return user()
        if self is ChatMessageRole.FUNCTION:
            return function()
