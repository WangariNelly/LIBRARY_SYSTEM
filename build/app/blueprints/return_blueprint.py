#!/usr/bin/env python3

# import os
# from flask import Blueprint, render_template, request, url_for, redirect
# from models.bk_return import BK_Return

# return_blueprint = Blueprint('return_blueprint',__name__)

# @return_blueprint.route("/bk_return/new/", methods=['GET','POST'])
# def new_book_return():
#     if request.method == 'GET':
#         return redirect(url_for('issued_blueprint.get_bk_to_return'))
#     else:
#         issued_id = request.form['issued_id']
#         returned = request.form['is_returned']
        
#         new_return = BK_Return(issued_id, returned)
#         new_return.create_bk_return()

#         return redirect(url_for('books_returned.html'))
