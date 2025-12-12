from typing import Callable

from pydantic import BaseModel, Field, JsonValue

from .protocols import Decomposer, Dispatcher, Router, UpdateHandler


class Orchestrator(BaseModel):
    """
    The Port (Interface).
    Defines the shape of any Orchestrator implementation.
    """

    # Strategy Components
    decomposer: Decomposer
    router: Router
    dispatcher: Dispatcher
    update_handler: UpdateHandler

    registry: dict[str, Callable[..., JsonValue]] = Field(default_factory=dict)

    class Config:
        arbitrary_types_allowed: bool = True

    def register(self, name: str, func: Callable[..., JsonValue]) -> None:
        self.registry[name] = func

    def run(self, request: str) -> dict[str, JsonValue]:
        """Execute the orchestration logic."""
        raise NotImplementedError(
            f"Subclasses must implement the `run` method to process {request}."
        )
