import requests
from datetime import datetime
from src.utils import remove_stopwords

# date = month/day/year
def fetch_news(topic: str, from_date: str, to_date: str):
    """ 
    Function to collect news data using api. Using today date, previously related news duration can be estimated.
    """
    today = datetime.today()
    from_date = datetime.strptime(from_date, "%Y-%m-%d").date()
    to_date = datetime.strptime(to_date, "%Y-%m-%d").date()
    apikey = ""
    url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=popularity&pageSize=30&apiKey={apikey}"

    response = requests.get(url)
    response = response.json()

    articles = response['articles']
    
    raw_news = []

    for article in articles:
        title = article['title']
        description = article['description']
        url = article['url']
        date = article['publishedAt']
        raw_news.append({
            "title": title,
            "description": description,
            # "source url": url,
            "date": date,
        })

    print(f"Total news are: {len(raw_news)}")

    news = []
    keywords = remove_stopwords(topic)
    keywords = keywords.split()
    print(f"Keywords: {keywords}")

    for item in raw_news:
        title = item.get('title', '').lower()  # Get the title, convert to lowercase
        description = item.get('description', '').lower()  # Get the description, convert to lowercase
        # print(f"Title: {title}\n")
        
        # Check if any of the keywords are in the title or description
        if any(keyword.lower() in title or keyword.lower() in description for keyword in keywords):
            # print(f"Each dict: {item}\n")
            news.append(item)

    print(f"Relevant news are: {len(news)}")

    return news


def fetch_latest_news(topic: str):
    """ 
    Function to collect news data using api. Using today date, previously related news duration can be estimated.
    """
    today = datetime.today()
    apikey = ""
    newsapi = f"https://newsapi.org/v2/everything?q={topic}&sortBy=relevancy,popularity&pageSize=30&apiKey={apikey}"

    response = requests.get(newsapi)
    response = response.json()

    articles = response['articles']
    raw_news = []

    for article in articles:
        title = article['title']
        description = article['description']
        url = article['url']
        date = article['publishedAt']
        raw_news.append({
            "title": title,
            "description": description,
            # "source url": url,
            "date": date,
        })

    print(f"Total news are: {len(raw_news)}")

    news = []
    keywords = remove_stopwords(topic)
    keywords = keywords.split()
    print(f"Keywords: {keywords}")

    for item in raw_news:
        title = item.get('title', '').lower()  # Get the title, convert to lowercase
        description = item.get('description', '').lower()  # Get the description, convert to lowercase
        # print(f"Title: {title}\n")
        
        # Check if any of the keywords are in the title or description
        if any(keyword.lower() in title or keyword.lower() in description for keyword in keywords):
            # print(f"Each dict: {item}\n")
            news.append(item)

    print(f"Relevant news are: {len(news)}")

    return news