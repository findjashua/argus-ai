PYTHON ?= python3
RUFF ?= ruff
BASEDPYRIGHT ?= basedpyright

.PHONY: format format-check typecheck check

format:
	$(RUFF) format src

format-check:
	$(RUFF) format --check src

typecheck:
	$(BASEDPYRIGHT) --warnings

check: format-check typecheck
