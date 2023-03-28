#!/usr/bin/python3
""" User Table """

from common.base import Base, myql_session
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from flask import session
from flask_login import UserMixin

class User(Base, UserMixin, object):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    email_address = Column(String(60), nullable=False, unique=True)
    phone = Column(String(30), nullable=True)
    password = Column(String(3000), nullable=False)
    created_at = Column(DateTime(timezone=True), default=func.now())

    def __init__(self, full_name, email_address, phone, password):
        self.full_name = full_name
        self.email_address = email_address
        self.phone = phone
        self.password = password

    def __repr__(self):
        return f"Name {self.full_name}"

    def create_user(self):
        """
        Args:
            full_name (string) - Names of the user
            email_address (string) - Email of the user
            phone (string) - Phone Number of the user
            is_admin (bool) - whether the user is admin or not
            pass1 (string) - Password to be used by the user when they are logging in
            pass2 (string) - Confirm password
        """
        user = User.get_by_email(self.email_address)
        if user is None:
            new_user = User(self.full_name, self.email_address, self.phone, self.password)
            myql_session.add(new_user)
            myql_session.commit()
            myql_session.close()

        else:
            id = User.get_id_by_email(self.email_address)

            new_user_data = {
                "full_name": self.full_name,
                "email_address": self.email_address,
                "phone": self.phone,
                "password": self.password
            }

            myql_session.query(User).filter(
                User.user_id == id
            ).update(new_user_data)
            myql_session.commit()
            myql_session.flush()
            myql_session.close()

    @staticmethod
    def delete_user(user_id):
        """
        Delete user by id
        Args:
            user_id - user id to use for deleting
        """
        user = myql_session.query(User).filter(User.user_id==user_id).first()
        myql_session.delete(user)
        myql_session.commit()            
        myql_session.close()
    
    @classmethod
    def get_by_email(cls, email_address):
        """
        Args:
            email_address - get user object
        Return:
            User object
        """
        user = myql_session.query(User).filter(
            User.email_address==email_address).first()
        if user is not None:
            return {
                "user_id": user.user_id,
                "full_name": user.full_name,
                "email_address": user.email_address,
                "phone": user.phone,
                "password": user.password
            }

    @classmethod
    def get_by_id(cls, user_id):
        """
        Args:
            user_id - get user object
        Return:
            User object
        """
        user = myql_session.query(User).filter(
            User.user_id==user_id).first()
        return {
                "user_id": user.user_id,
                "full_name": user.full_name,
                "email_address": user.email_address,
                "phone": user.phone,
                "password": user.password
            }   

    @classmethod
    def get_id_by_email(cls, email_address):
        user_id = User.get_by_email(email_address)['user_id']
        if user_id is not None:
            return user_id
        else:
            return False

    @classmethod
    def is_logins_valid(cls, email_address, password):
        user = User.get_by_email(email_address)
        if user is not None:
            return user.password == password
        else:
            return False
    
    @staticmethod
    def login(email_address):
        session['email_address'] = email_address
    
    @staticmethod
    def logout():
        session['email_address'] = None

    @staticmethod
    def update_user(user_id, full_name, email_address, phone, password):
        """
        Updates User
        """
        user = User.get_by_id(user_id)
        user.full_name = full_name
        user.email_address = email_address
        user.phone = phone
        user.password = password

        myql_session.commit()
        myql_session.close()

    @staticmethod
    def get_acronymes(fullname):
        """
        Parameters
        ----------
        fullname - pass fullname of the user
        Return
        ------
        Acronymes of in caps
        """
        acronyme = ""

        if ' ' in fullname:
            names = fullname.split()
            first_acronyme = names[0][0]
            second_acronyme = names[1][0]
            acronyme = f"{first_acronyme}{second_acronyme}"
            return acronyme.upper()
        else:
            acronyme = fullname[0]
            return acronyme.upper()
