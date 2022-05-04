from flask import render_template
from app import app

# Views
@app.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  title = "Sam News App"
  return render_template('index.html', title = title)

@app.route('/news/<id>')
def news(id):
  '''
  View news page function that returns the news articles pages and its data
  '''

  return render_template('news.html', id=id) 