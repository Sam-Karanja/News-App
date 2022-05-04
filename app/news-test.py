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
        self.new_news = News(1234, "Flask", "Flask Author", "The Evolution of Flask", "The Story of how Flask Evolved", "https://www.spiegel.de/wirtschaft/unternehmen/adler-group-aktie-von-immobilienkonzern-stuerzt-ab-pruefer-verweigern-testat-a-1f3d36b6-3772-44d8-b5c7-87eaedd4a301", "https://cdn.prod.www.spiegel.de/images/5a0e3272-55fa-43b3-b2bd-93a14b246bc8_w1280_r1.77_fpx50.67_fpy50.jpg", "2022-05-02T08:48:58Z")


  def test_instance(self):



        if __name__ == '__main__':
            uinittest.main()