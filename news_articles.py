import unittest
from app.models import NewsArticle

class NewsArticleTest(unittest.TestCase):
    '''
    Test case to test the behaviour of the News Clas
    '''


    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.new_news_article = NewsArticle(""bbc-news", "BBC Newss", "Jacky Hunt-Broersma: The cancer survivor who ran 104 marathons in 104 days", "Aged 26, "Aged 26, Jacky Hunt-Broersma lost her left leg to cancer - now she has set an unofficial world record.", "http://www.bbc.co.uk/news/world-us-canada-61299527", "https://ichef.bbci.co.uk/news/1024/branded_news/5D65/production/_124390932_jacky1.jpg", "2022-05-02T21:52:21.8015368Z")

    def test_instance(self):
    self.assertTrue(isinstance(self.new_news_article, NewsArticle))


  def test_init(self):
    '''
    test_init case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_news_article.id,"bbc-news")
    self.assertEqual(self.new_news_article.name, "BBC News")
    self.assertEqual(self.new_news_article.title, "Jacky Hunt-Broersma: The cancer survivor who ran 104 marathons in 104 days")
    self.assertEqual(self.new_news_article.description, "Aged 26, Jacky Hunt-Broersma lost her left leg to cancer - now she has set an unofficial world record.")
    self.assertEqual(self.new_news_article.url, "http://www.bbc.co.uk/news/world-us-canada-61299527")
    self.assertEqual(self.new_news_article.urlToImage, "https://ichef.bbci.co.uk/news/1024/branded_news/5D65/production/_124390932_jacky1.jpg")
    self.assertEqual(self.new_news_article.publishedAt, "2022-05-02T21:52:21.8015368Z")



