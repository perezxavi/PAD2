"""
Definition of the Book class with attributes isbn, author, title, and number of pages.
"""

class Book:

    def __init__(self):
        """
        Constructor method called every time an object of this class is instantiated.
        In this example, we are only creating the (public) attributes. Prefixing 'self' is necessary to indicate that these
        belong to the instantiated object.
        """
        self.isbn = ''
        self.title = ''
        self.author = ''
        self.number_pages = 0

