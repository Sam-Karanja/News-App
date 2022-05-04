from app import app 
import urllib.request, json
form .models import news
News = news.News

# Getting api key

apiKey = app.config['NEWS_API_KEY'] 

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    """
    function that gets the json request to out url request
    """
    get_news_url = base_url.format(category,apikey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
    get_news_response = json.loads(get_news_data)

    news_sources = None

    if get_news_response['sources']:
      news_sources_list = get_news_response['sources']
      news_sources = process_sources(news_sources_list)

  return news_sources


def process_sources(news_list):
  '''
  Function that processes the news sources results and transforms them to a list of Objects
  Args:
    news_list: A list of dictionaries that contain news details
  Returns:
    news_results: A list of news objects
  '''
  
  news_results = []
  for news_item in news_list:
    id = news_item.get('id')
    name = news_item.get("name")
    description = news_item.get("description")
    url = news_item.get("url")
    category = news_item.get("category")
    language = news_item.get("language")
    country = news_item.get("country")

    if description:
      news_object = News(id, name, description, url, category, language, country )
      news_results.append(news_object)

    return  news_results


