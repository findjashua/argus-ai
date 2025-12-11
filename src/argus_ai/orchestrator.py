from typing import Callable, Any
from pydantic import BaseModel, Field

from .protocols import Decomposer, Router, Dispatcher, UpdateHandler

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
    
    registry: dict[str, Callable[..., Any]] = Field(default_factory=dict)
    
    class Config:
        arbitrary_types_allowed: bool = True

    def register(self, name: str, func: Callable[..., Any]) -> None:
        self.registry[name] = func

    def run(self, request: str) -> dict[str, Any]:
        """Execute the orchestration logic."""
        raise NotImplementedError(f"Subclasses must implement the `run` method to process {request}.")