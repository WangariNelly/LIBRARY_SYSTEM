#!/usr/bin/python3

from common.base import Base, engine
from models.book import Book
from models.user import User
from utils.books_to_list import csv_to_list
from utils.generate_users import generate_users
from werkzeug.security import generate_password_hash

books_path = "/home/nelly/Downloads/library_management_system/build/data/books.csv"

Base.metadata.create_all(engine)

def add_books(path):
    """
    Args:
        path (csv) - Path for csv file
    Return:
        void
    """
    books_lst = csv_to_list(path)
    for bk in books_lst:
        try:
            book = Book(bk[0], bk[1], bk[2], bk[3], bk[4], bk[5], bk[6])
            book.create_book()
        except:
            print(f"Error Adding Book!")

def add_users(num):
    """ 
        Adds automatically generated users to database
        Args:
            num (int) - number of users to be added in the database
        Return:
            void
    """
    users = generate_users(num)
    for user in users:
        try:
            password = user[3]
            new_user = User(user[0], user[1], user[2], generate_password_hash(password, method='sha256'))
            new_user.create_user()
        except:
            print(f"Error Adding User!")

if __name__ == "__main__":
    add_books(books_path) # Replace Path with your own
    add_users(100) # Replace 100 with number of users you want
