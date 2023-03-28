#!/usr/bin/python3

from . book import Book
from . librarian import Librarian
from . user import User
from common.base import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer,String
from sqlalchemy import Enum, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import func
from common.base import myql_session

class Issued(Base):
    __tablename__ = 'issued'
    issued_id = Column(Integer, primary_key=True)
    issued_date = Column(DateTime(timezone=True), default=func.now())
    is_returned = Column(Boolean, unique=False, default=False)
    book_isbn = Column(String(60), ForeignKey('book.isbn_no'), nullable=False)
    librarian_id = Column(Integer, ForeignKey('librarian.librarian_id'), nullable=False)
    borrower_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    book = relationship(Book)
    librarian = relationship(Librarian)
    borrower = relationship(User)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, book_isbn, librarian_id, borrower_id, is_returned=False):
        self.book_isbn = book_isbn
        self.librarian_id = librarian_id
        self.borrower_id = borrower_id
        self.is_returned = is_returned

    def __repr__(self):
        return f"Borrowed {self.book_isbn}"

    def create_issued(self):
        issued = Issued(self.book_isbn, self.librarian_id, self.borrower_id, self.is_returned)
        myql_session.add(issued)
        myql_session.commit()
        myql_session.close()
    
    @classmethod
    def get_books_borrowed(cls):
        """
            List of borrowed books
        """
        books_borrowed = myql_session.query(Issued, Book, Librarian, User).join(
                Book, Issued.book_isbn == Book.isbn_no
            ).join(
                Librarian, Issued.librarian_id == Librarian.librarian_id
            ).join(
                User, Issued.borrower_id == User.user_id
            ).all()
        return [book for book in books_borrowed]
    
    @classmethod
    def get_book_borrowed_by_issued_id(cls, issued_id):
        """
        Parameters
        ----------
        issued_id (int) - Unique identifier
        ------
        Return
        ------
        Return an object of a book
        """
        book_borrowed = myql_session.query(
                Issued, Book, Librarian, User
            ).join(
                Book, Issued.book_isbn == Book.isbn_no
            ).join(
                Librarian, Issued.librarian_id == Librarian.librarian_id
            ).join(
                User, Issued.borrower_id == User.user_id
            ).filter(
                Issued.issued_id==issued_id
            ).first()
        return book_borrowed

    @classmethod
    def get_book_borrowed_by_user_id(cls, user_id):
        """
        Parameters
        ----------
        user_id (int) - Unique identifier
        ------
        Return
        ------
        Return an object of a book
        """
        books_borrowed = myql_session.query(
                Issued, Book, Librarian, User
            ).join(
                Book, Issued.book_isbn == Book.isbn_no
            ).join(
                Librarian, Issued.librarian_id == Librarian.librarian_id
            ).join(
                User, Issued.borrower_id == User.user_id
            ).filter(
                Issued.borrower_id==user_id
            ).all()
        
        return [book for book in books_borrowed]
    
    @staticmethod
    def get_issued_by_id(issue_id):
        """
        Parameters
        ----------
        issued_id (int) - Unique identifier
        ------
        Return
        ------
        Return an object of a book
        """
        issued = myql_session.query(Issued).filter(Issued.issued_id==issue_id).first()
        return issued

    @staticmethod
    def update_is_returned(issue_id, is_returned=True):
        """
        Parameters
        ----------
        issued_id (int) - int to identify issue
        is_returned (bool) - boolean, initialized to True
        ------
        Return
        ------
        Return updated issue
        """
        bk_issued = Issued.get_issued_by_id(issue_id)
        print(bk_issued)
        # book_isbn, librarian_id, borrower_id
        bk_issued.book_isbn = bk_issued.book_isbn
        bk_issued.librarian_id = bk_issued.librarian_id
        bk_issued.borrower_id = bk_issued.borrower_id
        bk_issued.is_returned = is_returned
        myql_session.commit()
        myql_session.close()

    @staticmethod
    def get_books_returned():
        """
        Parameters
        ----------
        ------
        Return
        ------
        Return books list
        """
        returned_books = myql_session.query(
                Issued, Book
            ).join(
                Book, Issued.book_isbn == Book.isbn_no
            ).filter(
                Issued.is_returned==True
            ).all()
        
        return [book for book in returned_books]
