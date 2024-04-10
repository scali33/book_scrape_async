import re
import logging

from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')


logger = logging.getLogger('scraping')

logger.info('Booting book list...')

from locators.book import Book_location
from parsers.bookparser import BookParser

class BookPage:
    def __init__(self,page):
        logger.debug('parsing page content with beatifulsoup html parser')
        self.soup = BeautifulSoup(page,'html.parser')
    @property
    def books(self):
        locator = Book_location.BOOKS
        logger.debug(f'fiding all books in the page using"{locator}.')
        books_tags = self.soup.select(locator)
        return [BookParser(book) for book in books_tags]
    @property
    def page_count(self):
        logger.debug('finding all number of catalogue pages avaliable...')
        content = self.soup.select_one(Book_location.PAGER).string
        logger.info(f'found number of catalogues pages avalible: {content}')
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern,content)
        pages = int(matcher.group(1))
        logger.debug(f'extracted number of pages as integer: `{pages}`')
        return pages