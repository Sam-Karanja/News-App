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
        self.new_news = News(1234, "Flask has evolved", "A thrilling article on the evolution of flask", "https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/PZDEVWWJ6QI6ZN7OOTYJ3AT4UY.jpg&w=1440" )


        if __name__ == '__main__':
            uinittest.main()