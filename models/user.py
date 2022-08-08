#!/usr/bin/python3
''' module for a User class '''
from .base_model import BaseModel


class User(BaseModel):
    ''' User class '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
