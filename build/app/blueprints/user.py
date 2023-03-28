#!/usr/bin/env python3

from flask import (Blueprint, render_template, request, session,
                abort, url_for, redirect, flash)
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models.issued import Issued
from flask_login import login_required

user_blueprint  = Blueprint('user_blueprint', __name__)

has_account = False

@login_required
@user_blueprint.route("/profile")
def profile():
    if session['email'] is not None:
        email = session['email']
        user = User.get_by_email(email)

        acronymes = User.get_acronymes(user["full_name"])

        user_id = User.get_id_by_email(email)
        books_borrowed = Issued.get_book_borrowed_by_user_id(user_id)

        return render_template('profile.html',
            user=user,
            books=books_borrowed,
            acronymes=acronymes
        )
    else:
        return redirect(url_for('user_blueprint.login_template'))

@user_blueprint.route("/account")
def signup_template():
    return render_template('account.html', has_account=False)

@user_blueprint.route("/login")
def login_template():
    return render_template('login.html')

@user_blueprint.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']       
        password = request.form['password']
        user = User.get_by_email(email)

        if user:
            user_pass = user["password"]

            if not user or not check_password_hash(user_pass, password):
                flash(f"Wrong Email or Password")
                return redirect(url_for('user_blueprint.login_template'))
            else:
                session['email'] = email
            return redirect(url_for('user_blueprint.profile'))
        else:
            flash(f"Wrong Email or Password")
            return redirect(url_for('user_blueprint.login_template'))

@user_blueprint.route("/logout")
def logout():
    User.logout()
    return redirect(url_for('main.home'))

@user_blueprint.route("/user/new", methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        return render_template('account.html', has_account=False)
    else:
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        confrim_password = request.form['confirm_password']        
        if password == confrim_password:
            new_user = User(full_name, email, phone, generate_password_hash(password, method='sha256'))
            new_user.create_user()
            return redirect(url_for('user_blueprint.login_template'))
        else:
            return "Passwords are not the same"

@user_blueprint.route("/user/update/<int:user_id>", methods=['GET', 'POST'])
def user_update(user_id):
    if request.method == 'GET':
        user = User.get_by_id(user_id)
        if user is not None:
            return render_template(
                'account.html',
                user=user,
                has_account=True,
                user_id=user_id
            )
    else:
        full_name = request.form['full_name']
        email_address = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        update_user = User(full_name, email_address, phone, generate_password_hash(password))
        update_user.create_user()
        return render_template('login.html')

@user_blueprint.route("/user/delete/<int:user_id>")
def user_delete(user_id):
    User.delete_user(user_id)
    return redirect(url_for('user_blueprint.signup_template'))
