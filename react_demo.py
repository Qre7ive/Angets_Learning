from llm_client import HelloAgentsLLM
from react import ReActAgent
from tools import create_default_tool_executor, search


if __name__ == "__main__":
    llm_client = HelloAgentsLLM()
    tool_executor = create_default_tool_executor(search)
    agent = ReActAgent(llm_client=llm_client, tool_executor=tool_executor, max_steps=5)

    question = "华为最新手机型号及主要卖点是什么"
    final_answer = agent.run(question)

    if final_answer is None:
        print("测试结束: agent 未返回最终答案。")
