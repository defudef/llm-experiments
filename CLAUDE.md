# CLAUDE.md

This document provides guidance for AI assistants working with the llm-experiments repository.

## Project Overview

This is an experimental repository for LLM (Large Language Model) experiments, including:
- Function calling with Google's FunctionGemma model
- Self-learning game experiments with LLM memory services
- MLflow integration for experiment tracking

## Tech Stack

- **Python**: 3.13 (specified in `.python-version`)
- **Package Manager**: uv (uses `pyproject.toml` and `uv.lock`)
- **Key Dependencies**:
  - `transformers` / `torch` / `accelerate` - HuggingFace model loading
  - `litellm` - Unified LLM API interface
  - `mlflow` - Experiment tracking
  - `wandb` / `weave` - Weights & Biases integration
  - `typer` - CLI framework
  - `python-dotenv` - Environment variable management

## Project Structure

```
llm-experiments/
├── main.py                    # Root entry point (minimal)
├── pyproject.toml             # Project dependencies and config
├── uv.lock                    # Lock file for reproducible installs
├── .env.example               # Required environment variables template
├── .python-version            # Python version (3.13)
│
├── function_gemma/            # FunctionGemma model experiments
│   ├── __init__.py
│   └── predict.py             # CLI for function calling with Gemma
│
└── self_learning/             # Self-learning game experiment
    ├── main.py                # Entry point for self-learning module
    ├── config.py              # Configuration (API keys, MLflow setup)
    ├── game/
    │   └── game.py            # Game logic (bulb puzzle)
    ├── services/
    │   └── llm_memory_service.py  # LLM memory service (stub)
    └── memory/                # Runtime memory storage directory
        └── .gitkeep
```

## Environment Setup

### Required Environment Variables

Create a `.env` file with the following keys (see `.env.example`):

```
CEREBRAS_API_KEY=<your-key>
WANDB_API_KEY=<your-key>
HUGGINGFACE_API_KEY=<your-key>
```

### Install Dependencies

```bash
uv sync
```

## Running Commands

### MLflow UI (Experiment Tracking)

```bash
uv run mlflow ui --port 5000
```

### FunctionGemma Prediction CLI

```bash
uv run python function_gemma/predict.py
```

This loads the `google/functiongemma-270m-it` model and runs interactive function-calling inference.

### Self-Learning Game

```bash
uv run python -m self_learning.main
```

## Code Conventions

### Style & Patterns

- **Type hints**: Use Python type annotations (see `game.py` for examples)
- **Async/await**: The self_learning module uses asyncio for async operations
- **CLI**: Use `typer` for command-line interfaces
- **Config**: Load environment variables via `python-dotenv` at module entry points
- **MLflow**: Auto-logging is enabled via `mlflow.litellm.autolog()` in config

### Module Organization

- Each experiment lives in its own directory (e.g., `function_gemma/`, `self_learning/`)
- Entry points use `if __name__ == "__main__":` pattern
- Configuration is centralized in `config.py` files within modules

### Environment Variables

- Always load via `dotenv.load_dotenv()` or `from dotenv import load_dotenv`
- Never hardcode API keys
- Reference keys from `os.environ` or `os.getenv()`

## Key Files Reference

| File | Purpose |
|------|---------|
| `function_gemma/predict.py` | FunctionGemma model inference with Typer CLI |
| `self_learning/config.py` | Cerebras API config, MLflow autolog setup |
| `self_learning/game/game.py` | Bulb puzzle game logic for self-learning experiments |
| `self_learning/services/llm_memory_service.py` | Placeholder for LLM memory service |

## Development Notes

- The project uses `uv` as the package manager - prefer `uv run` over direct `python` calls
- HuggingFace models require authentication via `HUGGINGFACE_API_KEY`
- MLflow runs are stored in `mlruns/` directory (gitignored)
- The `self_learning/memory/` directory stores runtime state files

## Testing

No formal test suite is currently configured. When adding tests, follow these conventions:
- Place tests in a `tests/` directory
- Use pytest as the test framework
- Run with `uv run pytest`
