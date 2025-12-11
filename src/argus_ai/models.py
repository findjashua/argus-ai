from typing import Literal, Any
from pydantic import BaseModel, Field

class RetryConfig(BaseModel):
    max_attempts: int = 3
    backoff_strategy: Literal["fixed", "exponential"] = "exponential"
    initial_wait_seconds: float = 1.0

class Task(BaseModel):
    id: str
    instruction: str
    dependencies: list[str] = Field(default_factory=list)
    
    # Life-cycle state
    status: Literal["pending", "running", "completed", "failed", "retrying"] = "pending"
    
    # Resilience State
    retry_config: RetryConfig = Field(default_factory=RetryConfig)
    attempt_count: int = 0
    next_run_at: float | None = None
    last_error: str | None = None
    
    # Data
    result: Any = None
    metadata: dict[str, Any] = Field(default_factory=dict)

class ArgusState(BaseModel):
    user_request: str
    tasks: dict[str, Task] = Field(default_factory=dict)
    artifacts: dict[str, Any] = Field(default_factory=dict)