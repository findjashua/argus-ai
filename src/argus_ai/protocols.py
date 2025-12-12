from typing import Protocol

from .models import Task
from .types import JsonValue

class Decomposer(Protocol):
    def plan(self, request: str, context: dict[str, JsonValue]) -> list[Task]:
        """
        Decomposes a user request into a list of Tasks with dependencies.
        """
        ...

class Router(Protocol):
    def route(self, task: Task, context: dict[str, JsonValue], registry: list[str]) -> str:
        """
        Selects the appropriate agent name from the registry based on task & context.
        """
        ...

class Dispatcher(Protocol):
    def format_payload(self, task: Task, context: dict[str, JsonValue]) -> JsonValue:
        """
        Formats the input payload required by the specific agent function.
        """
        ...

class UpdateHandler(Protocol):
    def handle(self, task: Task, raw_result: JsonValue) -> dict[str, JsonValue]:
        """
        Processes the raw result from an agent, handles retry logic,
        and returns a state update dictionary.
        """
        ...