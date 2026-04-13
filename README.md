# Agents Learning

This repository is a personal learning project for experimenting with different agent patterns built on top of an LLM client.

## Current modules

- `react/`: ReAct-style agent workflow
- `plan_solve/`: Plan-and-Solve agent workflow
- `reflection/`: Reflection-based agent workflow
- `tools/`: shared tool implementations
- `llm_client.py`: reusable LLM client

## Demos

Run the demos from the project root:

```bash
python3 react_demo.py
python3 plan_solve_demo.py
python3 reflection_demo.py
```

## Notes

- This repo is for learning and experimentation.
- Environment variables are stored locally in `.env` and are not tracked by git.
