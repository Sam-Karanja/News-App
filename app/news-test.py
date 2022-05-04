import unittest
from models import news
News = news.News
class NewsTest (unittest.TestCase):
    '''
    Test class to test the behaviour of the news class
    '''


    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = News("abc-news", "ABS News", "Your trusted sourcr for breaking news, analysis, exclusive interviews,headlines and videos ata ABC News.com",  "https://abcnews.go.com", "general", "en", "us")


  def test_instance(self):



        if __name__ == '__main__':
            uinittest.main()