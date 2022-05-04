from flask import render_template
from app import app
from.request import get_news

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

@app.route('/news/<id>')
def news(id):
  '''
  View news page function that returns the news  pages and its data
  '''


  return render_template('news.html', id=id) 