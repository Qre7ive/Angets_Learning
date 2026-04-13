from typing import Any, Callable, Dict


SEARCH_DESCRIPTION = (
    "A web search engine tool. Use it when you need up-to-date facts, recent events, "
    "or information not present in the model's own knowledge."
)


class ToolExecutor:
    """
    Simple registry used to manage and expose tools to the agent loop.
    """

    def __init__(self) -> None:
        self.tools: Dict[str, Dict[str, Any]] = {}

    def registerTool(self, name: str, description: str, func: Callable[..., str]) -> None:
        if name in self.tools:
            print(f"Warning: tool '{name}' already exists and will be overwritten.")
        self.tools[name] = {"description": description, "func": func}
        print(f"Tool '{name}' registered.")

    def getTool(self, name: str) -> Callable[..., str] | None:
        return self.tools.get(name, {}).get("func")

    def getAvailableTools(self) -> str:
        return "\n".join(
            f"- {name}: {info['description']}" for name, info in self.tools.items()
        )


def create_default_tool_executor(search_func: Callable[..., str]) -> ToolExecutor:
    executor = ToolExecutor()
    executor.registerTool("Search", SEARCH_DESCRIPTION, search_func)
    return executor
