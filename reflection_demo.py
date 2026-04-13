from llm_client import HelloAgentsLLM
from reflection import ReflectionAgent


if __name__ == "__main__":
    llm_client = HelloAgentsLLM()
    agent = ReflectionAgent(llm_client, max_iterations=2)

    task = "编写一个Python函数，找出1到n之间所有的素数（prime numbers）。"
    agent.run(task)
