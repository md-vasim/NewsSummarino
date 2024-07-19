import requests
import os 
import json
from datetime import datetime, timedelta
from langchain.schema import SystemMessage
from langchain.agents import AgentExecutor
from langchain.agents import OpenAIFunctionsAgent
from langchain.chat_models import ChatOpenAI
from src.basetool import FetchNewsTool, FetchLatestNewsTool
import openai
from src.prompt import (
    PREFIX,
    TASK,
    STEPS,
    FORMAT,
    RESPONSE
)
# from dotenv import load_dotenv
# load_dotenv()
# OPENAI_API = os.getenv("OPENAI_API_KEY")
# print(f"this is openai api type: {type(OPENAI_API)}")
# print(OPENAI_API)

# meer sir api
os.environ['OPENAI_API_KEY'] = ""

llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

tools = [FetchLatestNewsTool(), FetchNewsTool()]

template = f""" 
        {PREFIX}\
        
        Task: {TASK}\
        
        Steps: {STEPS}

        Format: {FORMAT}\

        Response: {RESPONSE}\
    """

def build_agent(llm=llm, template=template, tools=tools):

    system_message = SystemMessage(content=template)
    prompt = OpenAIFunctionsAgent.create_prompt(system_message=system_message)

    agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor

if __name__ == "__main__":
    agent = build_agent()
    question = input("News:\n")
    response = agent.run(question)
    print("\n", response)