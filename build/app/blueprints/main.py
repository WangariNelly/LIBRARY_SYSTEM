#!/usr/bin/env python3

import os
from flask import Blueprint, render_template, request, session, abort, url_for, redirect
from models.user import User
from models.book import Book
from models.librarian import Librarian
from models.issued import Issued
from flask_login import login_required


# template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# TEMPLATES_DIR = os.path.join(template_dir, 'build/frontend/templates')
# STATIC_DIR = os.path.join(template_dir, 'build/frontend/static')

# print(TEMPLATES_DIR)
# , template_folder="../../frontend/templates/", static_folder="../../frontend/static/

main = Blueprint('main',__name__)

has_account = False
book_exists = False

filters = {
        "author": "Author",
        "categories": "Category",
        "isbn_no": "ISBN NO",
        "bk_title": "Title",
        "year_published": "Year Published"
    }

book_to_issue = {}

@main.route("/")
def home():
    return render_template('index.html', filters=filters)

@main.route("/book/search/", methods=['GET', 'POST'])
def book_search():
    if request.method == 'GET':
        return redirect(url_for("main.home"))
    else:
        selected = request.form['search-filter']
        search_filter = request.form['filter_value']
        if selected == 'author':
            books = Book.get_books_by_author(search_filter)
            books = Book.check_if_empty(books)
            return render_template('search_results.html',
                books=books,
                filter_res=filters[selected]
            )
        elif selected == 'categories':
            books = Book.get_books_by_category(search_filter)
            books = Book.check_if_empty(books)
            return render_template('search_results.html',
                books=books,
                filter_res=filters[selected]
            )
        elif selected == 'isbn_no':
            book = Book.get_book_by_isbn(search_filter)
            return render_template('search_results.html',
                books=book,
                filter_res=filters[selected]
            )
        elif selected == 'bk_title':
            books = Book.get_books_by_title(search_filter)
            books = Book.check_if_empty(books)
            return render_template('search_results.html',
                books=books,
                filter_res=filters[selected]
            )
        else:
            books = Book.get_books_by_year_published(int(search_filter))
            books = Book.check_if_empty(books)
            return render_template('search_results.html', books=books)

@login_required
@main.route("/books/new", methods=['GET', 'POST'], strict_slashes=False)
def new_book():
    book_exists=False
    if request.method == 'GET':
        return render_template('edit_book.html', book_exists=book_exists)
    else:
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        thumbnail = request.form['thumbnail']
        description = request.form['description']
        year_published = request.form['year_published']

        book = Book(isbn, title, author, category, thumbnail, description, year_published)
        book.create_book()
        return redirect(url_for('main.books'))

@login_required
@main.route("/book/update/<string:isbn_no>", methods=['GET', 'POST'])
def update_book(isbn_no):
    book_exists = True
    if request.method == 'GET':
        book = Book.get_book_by_isbn(isbn_no)
        return render_template('edit_book.html', book=book, book_exists=book_exists, isbn_no=isbn_no)
    else:
        isbn = request.form['isbn']
        title = request.form['title']
        author = request.form['author']
        category = request.form['category']
        thumbnail = request.form['thumbnail']
        description = request.form['description']
        year_published = request.form['year_published']

        Book.book_update(isbn, title, author, category, thumbnail, description, year_published)
        return redirect(url_for("main.books"))

@login_required
@main.route("/book/delete/<string:isbn_no>")
def delete_book(isbn_no):
    Book.book_delete(isbn_no)
    return redirect(url_for('main.books'))


@main.route("/books", strict_slashes=False)
def books():
    books = Book.get_books()
    return render_template('books_list.html', books=books)

@main.route("/book_details/<string:isbn_no>", strict_slashes=False)
def book_details(isbn_no):
    book = Book.get_book_by_isbn(isbn_no)
    if 'email' not in session:
        return redirect(url_for('user_blueprint.login'))        
    else:
        user_email = session['email']
        user_id = User.get_id_by_email(user_email)

        librarians = Librarian.get_libarians() # Get librarians

        # Check if there is a librarian, create if none
        if len(librarians) == 0:
            new_librarian = Librarian()
            new_librarian.create_librarian()
        else:
            librarian_id = Librarian.get_id_by_email('nellywangari30@gmail.com')

        book_to_issue['book_isbn'] = isbn_no
        book_to_issue['librarian_id'] = librarian_id
        book_to_issue['user_id'] = user_id
        book_to_issue['is_returned'] = False

        return render_template(
            'book_details.html',
            book = book,
            isbn_no = isbn_no,
            user_id = user_id,
            librarian_id = librarian_id,
            is_returned = False
        )

@main.route("/book/borrow", methods=['GET','POST'], strict_slashes=False)
def book_borrow():
    if request.method == 'GET':
        return render_template('issued.html', new_issue=book_to_issue)

    else:
        isbn = request.form['book_isbn']
        librarian_id = request.form['librarian_id']
        user_id = request.form['user_id']
        new_issued = Issued(
            isbn, librarian_id, user_id, is_returned=False
        )
        new_issued.create_issued()
        return redirect(url_for('issued_blueprint.books_issued'))
