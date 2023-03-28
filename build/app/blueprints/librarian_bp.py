#!/usr/bin/env python3

from flask import (Blueprint, render_template, request, session,
                abort, url_for, redirect, flash)
from werkzeug.security import generate_password_hash, check_password_hash
from models.librarian import Librarian

librarian_blueprint  = Blueprint('librarian_blueprint', __name__)

@librarian_blueprint.route('/librarians', strict_slashes=False)
def libarians():
    librarians = Librarian.get_libarians()
    return render_template('list_librarians.html', librarians=librarians)

@librarian_blueprint.route('/librarian/new', methods=['GET','POST'])
def new_librarian():
    if request.method == 'GET':
        return render_template('librarian.html')
    else:
        full_name = request.form['full_name']
        email_address = request.form['email_address']
        secret_key = request.form['secret_key']
        librarian = Librarian.get_librarian_by_email(email_address)
        if librarian is None:
            new_librarian = Librarian(full_name, email_address, generate_password_hash(secret_key, method='sha256'))
            new_librarian.create_librarian()
            return redirect(url_for('main.home'))
        else:
            flash(f"{email_address} Already exists")
            return render_template('librarian.html')
