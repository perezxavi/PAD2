"""
Testing the Book class.

Date: 1/9/2023.
"""
from book import Book

book1 = Book()  # instantiate an object of the Book class
book1.isbn = '9788467016901'
book1.title = 'The Ingenious Gentleman Don Quixote of La Mancha (Part 1 of Don Quixote)'
book1.author = 'Miguel de Cervantes Saavedra'
book1.number_pages = 920

print('Created a "Book" object with data:')
print('ISBN:', book1.isbn)
print('Title:', book1.title)
print('Author:', book1.author)
print('Number of pages:', book1.number_pages, '\n')

book2 = Book()  # instantiate another object of the Book class
book2.isbn = '9788415973621'
book2.title = 'The Ingenious Knight Don Quixote of La Mancha (Part 2 of Don Quixote)'
book2.author = 'Miguel de Cervantes Saavedra'
book2.number_pages = 736

print('Created a "Book" object with data:')
print('ISBN:', book2.isbn)
print('Title:', book2.title)
print('Author:', book2.author)
print('Number of pages:', book2.number_pages)