

class NewsSource:
    '''
    News class to define news objects
    '''

    def __init__(self,id, name, description, url, category, language, country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class NewsArticle:
    '''
    News articles class defines new articles objects
    '''

    def __init__(self, id, name, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.name = name
        self.title = title
        self.description = description,
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt