#!/usr/bin/python3
''' Module for a state tests '''
from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from models.state import State


class TestState(TestCase):
    ''' State class '''
    def test_9(self):
        ''' task 9 tests '''
        self.assertTrue(issubclass(State, BaseModel))
        self.assertEqual(State.name, '')
