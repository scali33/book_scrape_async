import logging
import re
from locators.book_atributes import BookAtributeloacator 

logger = logging.getLogger('scraping.bookparser')


class BookParser:
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    def __init__(self,elem):
        logger.debug(f'New book parser created from `{elem}`')
        self.parent = elem


    def __str__(self):
        return f'<Book {self.name} costing {self.price}$ with rating of ({self.rating} Stars>) avalible? [{self.instock.strip()}]\n'
    
    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookAtributeloacator.BOOK_NAME
        link = self.parent.select_one(locator)
        logger.debug(f'Book link is `{link}`')
        return link.attrs['href']


    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookAtributeloacator.BOOK_NAME      
        link =  self.parent.select_one(locator)
        logger.debug(f'Founded book `{link.attrs['title']}`')
        return link.attrs['title']
    
    
    @property
    def price(self):
        logger.info('fingin book price')
        locator = BookAtributeloacator.BOOK_PRICE
        price = self.parent.select_one(locator).string
        pattern = '£([0-9]+\\.[0-9]+)'
        matcher = re.search(pattern, price)
        price = float(matcher.group(1))
        logger.debug(f'Book price found `{price}`')
        return price
    
    
    @property
    def rating(self):
        logger.info('getting book rating...')
        locator = BookAtributeloacator.BOOK_RATING
        star = self.parent.select_one(locator)
        classes = star.attrs['class']
        rating_class = [elem for elem in classes if elem !='star-rating' ]
        bookRating = BookParser.RATINGS.get(rating_class[0])
        logger.debug(f'book rating found `{bookRating}`')
        return bookRating

    
    @property
    def instock(self):
        logger.info('finding if book is in stock..')
        locator = BookAtributeloacator.BOOK_INSTOCK
        avaliable = self.parent.select_one(locator).text
        logger.debug(f'information found {avaliable.strip()}')
        return avaliable
    
