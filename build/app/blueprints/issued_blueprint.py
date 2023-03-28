#!/usr/bin/env python3

from flask import (Blueprint, render_template, request, session,
                abort, url_for, redirect)
from models.issued import Issued
from models.user import User
from models.librarian import Librarian

issued_blueprint  = Blueprint('issued_blueprint', __name__)
issued_id = 0

is_returned = {
        "Yes": "Yes",
        "No": "No"
    }


@issued_blueprint.route('/issued')
def books_issued():
    issued = Issued.get_books_borrowed()
    return render_template('borrowed.html', issued=issued)

@issued_blueprint.route('/books_returned', strict_slashes=False)
def list_returned_books():
    returned_books = Issued.get_books_returned()
    return render_template('books_returned.html', returned_books=returned_books)

@issued_blueprint.route('/borrowed/more_details/<int:issued_id>')
def more_borrowed_details(issued_id):
    more_details = Issued.get_book_borrowed_by_issued_id(issued_id)
    return render_template('more_details_on_book_borrowed.html',
        more_details=more_details,
        issued_id=issued_id
    )

@issued_blueprint.route('/return_book/<int:issued_id>', methods = ['POST'])
def return_book(issued_id):
    if request.method == 'POST':
        more_details = Issued.get_book_borrowed_by_issued_id(issued_id)
        if more_details.is_returned == False:
            Issued.update_is_returned(issued_id)
            return redirect(url_for('issued_blueprint.list_returned_books'))
        else:
            pass


# @issued_blueprint.route('/borrowed/return_bk/<int:issued_id>', methods=['POST'], strict_slashes=False)
# def update_is_returned(issued_id):
#     Issued.update_is_returned(issued_id)
#     return redirect(url_for('issued_blueprint.list_returned_books'))
