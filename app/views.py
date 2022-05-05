from flask import render_template
from app import app
from.request import get_news, get_articles

# Views
@app.route('/')
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
  return render_template('index.html', title = title,top_headlines = top_headlines)

@app.route('/article/<id>')
def news(id):
  '''
  View news page function that returns the articles   pages and its data
  '''
news_article = get_articles(id)
title - f'{news_article.title}'

  return render_template('news.html', title = title, news_article = news_article) 