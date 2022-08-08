#!/usr/bin/python3
''' module for a Review class '''
from .base_model import BaseModel


class Review(BaseModel):
    ''' a Review class '''
    place_id = ''
    user_id = ''
    text = ''
