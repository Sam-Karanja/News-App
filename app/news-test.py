import unittest
form app.models import  NewsSource

class NewsTest (unittest.TestCase):
    '''
    Test class to test the behaviour of the news class
    '''


    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = NewsSource("abc-news", "ABS News", "Your trusted sourcr for breaking news, analysis, exclusive interviews,headlines and videos ata ABC News.com",  "https://abcnews.go.com", "general", "en", "us")


    def test_instance(self):
      self.assertTrue(isinstance(self.news_news, NewsSource))

    def test_init(self):
        '''
        test init case to test if the object is initialized properly
        '''
            self.assertEqual(self.new_news.id, "abc-news")
    self.assertEqual(self.new_news.name, "ABC News")
    self.assertEqual(self.new_news.description, "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")
    self.assertEqual(self.new_news.url, "https://abcnews.go.com")
    self.assertEqual(self.new_news.category, "general")
    self.assertEqual(self.new_news.language, "en")
    self.assertEqual(self.new_news.country, "us")




