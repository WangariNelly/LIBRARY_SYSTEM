#!/usr/bin/env python3

from faker import Faker
import random

def generate_password(firstname: str, lastname: str) -> list:
    """
    Args:
        firstname (string) - firstname of a user
        lastname (string) - lastname of a user
    Return:
        List of Passwords
    """
    number = random.randint(1001, 9999)
    password = "".join([firstname[0],lastname.lower(),str(number)])
    return password

def generate_users(number: int) -> list:
    """
    Args:
        number (int) - Number of users to be generated
    Return:
        List of lists of users
    """
    fk = Faker()
    firstName = ""
    lastName = ""
    email_address = []
    full_name = []
    phone_number = []
    passwords = []
    
    for _ in range(number):
        firstName = fk.first_name()
        lastName = fk.last_name()
        full_name.append(" ".join([firstName, lastName]))
        email_address.append(fk.email(firstName, lastName))
        phone_number.append(fk.phone_number())
        passwords.append(generate_password(firstName, lastName))
    
    user = zip(full_name, email_address, phone_number,passwords)
    return list(user)
