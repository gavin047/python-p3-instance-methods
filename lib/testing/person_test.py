#!/usr/bin/env python3

from person import Person

import io
import sys
import types

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person"'''
        guido = Person()
        assert(type(guido) == Person)

    def test_talk_is_method(self):
        '''talk() is an instance method'''
        guido = Person()
        assert(type(guido.talk) == types.MethodType)

    def test_talk_prints_hello_world(self):
        '''talk() prints "Hello World!"'''
        guido = Person()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.talk()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello World!\n")

    def test_walk_is_method(self):
        '''walk() is an instance method'''
        guido = Person()
        assert(type(guido.walk) == types.MethodType)

    def test_walk_prints_the_person_is_walking(self):
        '''walk() prints "The person is walking."'''
        guido = Person()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        guido.walk()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The person is walking.\n")