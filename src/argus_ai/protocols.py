from typing import Protocol, Any
from .models import Task

class Decomposer(Protocol):
    def plan(self, request: str, context: dict[str, Any]) -> list[Task]:
        """
        Decomposes a user request into a list of Tasks with dependencies.
        """
        ...

class Router(Protocol):
    def route(self, task: Task, context: dict[str, Any], registry: list[str]) -> str:
        """
        Selects the appropriate agent name from the registry based on task & context.
        """
        ...

class Dispatcher(Protocol):
    def format_payload(self, task: Task, context: dict[str, Any]) -> Any:
        """
        Formats the input payload required by the specific agent function.
        """
        ...

class UpdateHandler(Protocol):
    def handle(self, task: Task, raw_result: Any) -> dict[str, Any]:
        """
        Processes the raw result from an agent, handles retry logic,
        and returns a state update dictionary.
        """
        ...