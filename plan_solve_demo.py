from llm_client import HelloAgentsLLM
from plan_solve import PlanAndSolveAgent


if __name__ == "__main__":
    llm_client = HelloAgentsLLM()
    agent = PlanAndSolveAgent(llm_client)

    question = "一个水果店周一一共卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
    agent.run(question)
