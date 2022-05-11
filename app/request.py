from .models.news import NewsArticle, NewsSource
import urllib.request,json


# Getting api key

apiKey = None 


#Getting base urls
base_url = None
news_base_url = None
apikey =  None

def configure_request(app):
  global apiKey, base_url, news_base_url
  apiKey = app.config['NEWS_API_KEY']
  base_url = app.config['NEWS_API_BASE_URL']
  news_base_url = app.config['NEWS_ARTICLES_BASE_URL']

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

      return news_sources()

def get_articles(id):
  '''
  Function that gets the json response to our url request
  '''
  get_news_articles_url = news_base_url.format(id, apiKey)

  with urllib.request.urlopen(get_news_articles_url) as url:

    get_news_articles_data = url.read()
    get_news_articles_response = json.loads(get_news_articles_data)

    news_articles = None

    if get_news_articles_response['articles']:
      news_articles_list = get_news_articles_response['articles']
      news_articles = process_articles(news_articles_list)

  return news_articles





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
      news_object = NewsSource(id, name, description, url, category, language, country )
      news_results.append(news_object)

  return news_results


def process_articles(news_articles_list):
  '''
  Function that processes the news articles results and transforms them to a list of Objects
  Args:
    news_articles_list: A list of dictionaries that contain news articles details
  Returns:
    news_articles_results: A list of news articles objects
  '''

  news_articles_results = []

  for news_article in news_articles_list:
    id = news_article.get("sourc.id")
    name = news_article.get("source.name")
    title = news_article.get("title")
    description = news_article.get("description")
    url = news_article.get("url")
    urlToImage = news_article.get("urlToImage")
    publishedAt = news_article.get("publishedAt")

    if urlToImage:
      news_article_object = NewsArticle(id, name, title, description, url, urlToImage, publishedAt)
      news_articles_results.append(news_article_object)

  return news_articles_results 


