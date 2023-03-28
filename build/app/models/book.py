#!/usr/bin/python3
""" Book Table """

from common.base import Base,myql_session
from sqlalchemy import Column, DateTime, Integer,String
from sqlalchemy import Integer
from sqlalchemy.sql import func

class Book(Base):
    __tablename__ = 'book'
    isbn_no = Column(String(60), primary_key=True)
    bk_title = Column(String(200), nullable=False)
    bk_authors = Column(String(1000), nullable=False)
    categories = Column(String(1000), nullable=True)
    thumbanail = Column(String(1000), nullable=True)
    description = Column(String(5000), nullable=True)
    year_published = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self,isbn_no, bk_title, bk_authors, categories, thumbanail, description, year_published):
        self.isbn_no = isbn_no
        self.bk_title = bk_title
        self.bk_authors = bk_authors
        self.categories = categories
        self.thumbanail = thumbanail
        self.description = description
        self.year_published = year_published

    def __repr__(self):
        return f"{self.bk_title}"

    def create_book(self):
        book = Book(
            self.isbn_no,
            self.bk_title,
            self.bk_authors,
            self.categories,
            self.thumbanail,
            self.description,
            self.year_published
        )
        myql_session.add(book)
        myql_session.commit()
        myql_session.close()

    @staticmethod
    def book_update(isbn_no, bk_title, bk_authors, category, thumbnail, description, year_published):
        book = myql_session.query(Book).filter_by(isbn_no=isbn_no).first()
        book.bk_title = bk_title
        book.bk_authors = bk_authors
        book.categories = category
        book.thumbanail = thumbnail
        book.description = description
        book.year_published = year_published

        myql_session.commit()
        myql_session.close()

    @staticmethod
    def book_delete(isbn_no):
        book = myql_session.query(Book).filter(Book.isbn_no==isbn_no).first()
        myql_session.delete(book)
        myql_session.commit()            
        myql_session.close()

    @classmethod
    def get_books(cls):
        """ Returns a list of all books """
        books = myql_session.query(Book).all()
        return [book for book in books]

    @classmethod
    def get_book_by_isbn(cls, isbn_no):
        """
        Args:
            isbn_no - book unique identify
        Return:
            Return book object
        """
        book = myql_session.query(Book).filter(Book.isbn_no==isbn_no).first()
        return {
            "isbn_no": book.isbn_no,
            "bk_title": book.bk_title,
            "bk_authors": book.bk_authors,
            "categories": book.categories,
            "thumbanail": book.thumbanail,
            "description": book.description,
            "year_published": book.year_published
        }

    @classmethod
    def get_books_by_year_published(cls, year_published: int) -> list:
        """
        Args:
            year_published - filter by year published
        Return:
            get list of books
        """
        books: list = myql_session.query(Book).filter(Book.year_published==year_published).all()
        return [book for book in books]

    @classmethod
    def get_books_by_title(cls, bk_title: str) -> list:
        """
        Args:
            bk_title - parameter to filter books by title
        Return:
            get list of books
        """
        books: list = myql_session.query(Book).filter(Book.bk_title==bk_title).all()
        return [book for book in books]

    @classmethod
    def get_books_by_category(cls, category: str) -> list:
        """
        Args:
            category - parameter to filter books by category
        Return:
            get list of books
        """
        books: list = myql_session.query(Book).filter(Book.categories==category).all()
        return [book for book in books]

    @classmethod
    def get_books_by_author(cls, bk_authors: str) -> list:
        """
        Args:
            bk_authors - parameter to filter books by bk_authors
        Return:
            get list of books or empty
        """
        books: list = myql_session.query(Book).filter(Book.bk_authors==bk_authors).all()
        return [book for book in books]

    @staticmethod
    def check_if_empty(lst: list) -> int:
        """
            Checks if list is empty
            Args:
                lst (List) - List to be checked
            Return:

        """
        if len(lst) == 0:
            return f"No results found"
        else:
            return lst   
