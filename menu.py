import logging
from main import books


loger = logging.getLogger('loggin.menu')

USER_CHOICE = """ Enter one of the following
-'b' to look at 5-star books
-'c' to look at the cheapest books
-'n' to just get the next avaliable book on the catlogue
-'q' to exit
"""

def print_best_books():
    loger.info('printing best books')
    best_books = sorted(books, key=lambda x: x.rating *-1)[:5]
    for book in best_books:
        print(book)
def prin_cheapest_books():
    loger.info('printing all cheapests books')
    chep_books = sorted(books, key=lambda x: x.price)[:10]
    for book in chep_books:
        print(book)

book_generator = (x for x in books)

def get_next_book():
    loger.info('getting neext book')
    print(next(book_generator))

option = {
    'b': print_best_books,
    'c': prin_cheapest_books,
    'n': get_next_book
}

while True:
    user_input = input(USER_CHOICE).lower()
    if user_input in option.keys():
        option[user_input]()
    elif user_input == 'q':
        break
    else:
        print('please put the following choices!!! ')
print('good bye') 