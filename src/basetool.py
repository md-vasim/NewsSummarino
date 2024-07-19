from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from src.news_utility import fetch_news, fetch_latest_news

from typing import Type
from pydantic import BaseModel, Field
from langchain.tools import BaseTool


class FetchNewsInput(BaseModel):
    """Inputs for fetch_news"""

    topic: str = Field(description="Topic of news that should be collected")
    from_date: str = Field(description="Starting yyyy-mm-dd, from which the news sould be collected, if provided")
    to_date: str = Field(description="Ending yyyy-mm-dd, till which day the news should be collected, if provided")


class FetchNewsTool(BaseTool):
    name = "fetch_news"
    description = """
        Useful when you want to do the task related to the specific news with the specific time/days/dates.
        You should enter the given topic with dates provided  e.g., from, to.
        You should enter date using today's date for the news needs to be check.
        Remember, date format must be ISO 8601 format: yyyy-mm-dd
        """
    args_schema: Type[BaseModel] = FetchNewsInput

    def _run(self, topic: str, from_date: str, to_date: str):
        
        response = fetch_news(topic=topic, from_date=from_date, to_date=to_date)
        # print(f"Base tool error testing: {response}")
        return response

    def _arun(self, topic: str):
        raise NotImplementedError("fetch_news does not support async")


class FetchLatestNewsInput(BaseModel):
    """Inputs for fetch_latest_news"""

    topic: str = Field(description="Topic of latest news that should be collected")


class FetchLatestNewsTool(BaseTool):
    name = "fetch_latest_news"
    description = """
        Useful when you want to do the task related to the latest news.
        """
    args_schema: Type[BaseModel] = FetchLatestNewsInput

    def _run(self, topic: str):
        response = fetch_latest_news(topic)
        return response

    def _arun(self, topic: str):
        raise NotImplementedError("fetch_latest_news does not support async")


# tools = [FetchNewsTool()]