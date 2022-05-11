from flask import render_template,url_for
from . import main
from ..request import get_news, get_articles

# Views
@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''

  #Getting top-headlines news
  general = get_news('general')
  business = get_news('business')
  entertainment = get_news('entertainment')
  health = get_news('health')
  science = get_news('science')
  sports = get_news('sports')
  technology = get_news('technology')

  title = "Sam News App"
  return render_template('index.html', title = title, general = general, business = business, health = health , science = science, sports = sports)

@main.route('/article')
def news():
  '''
  View news page function that returns the articles   pages and its data
  '''
  news_article = get_articles()
  title = 'news_article'

  return render_template('news.html', title = title, news_article = news_article) 