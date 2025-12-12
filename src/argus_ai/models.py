from enum import Enum

from pydantic import BaseModel, Field, JsonValue


class DefaultTaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"

class RetryConfig(BaseModel):
    max_attempts: int = Field(default=3, ge=1)
    initial_wait_seconds: float = Field(default=1.0, gt=0)
    backoff_multiplier: float = Field(default=2.0, gt=1.0)
    max_wait_seconds: float | None = Field(default=None, gt=0)
    jitter_ratio: float = Field(default=0.1, ge=0.0, le=1.0)

class Task(BaseModel):
    id: str
    instruction: str
    dependencies: list[str] = Field(default_factory=list)
    
    # Life-cycle state (user-definable Enum; default provided)
    status: Enum = Field(default_factory=lambda: DefaultTaskStatus.PENDING)
    
    # Resilience State
    retry_config: RetryConfig = Field(default_factory=RetryConfig)
    attempt_count: int = 0
    next_run_at: float | None = None
    last_error: str | None = None
    
    # Data
    result: JsonValue | None = None
    metadata: dict[str, JsonValue] = Field(default_factory=dict)

class ArgusState(BaseModel):
    user_request: str
    tasks: dict[str, Task] = Field(default_factory=dict)
    artifacts: dict[str, JsonValue] = Field(default_factory=dict)