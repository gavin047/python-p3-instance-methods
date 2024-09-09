#!/usr/bin/env python3

from dog import Dog

import io
import sys
import types

class TestDog:
    '''Dog in dog.py'''

    def test_is_class(self):
        '''is a class with the name "Dog"'''
        fido = Dog()
        assert(type(fido) == Dog)

    def test_sit_is_method(self):
        '''sit() is an instance method'''
        fido = Dog()
        assert(type(fido.sit) == types.MethodType)

    def test_sit_prints_the_dog_is_sitting(self):
        '''sit() prints "The dog is sitting."'''
        fido = Dog()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.sit()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "The dog is sitting.\n")

class TestBark:
    '''Dog.bark() in dog.py'''

    def test_is_method(self):
        '''is an instance method'''
        fido = Dog()
        assert(type(fido.bark) == types.MethodType)

    def test_prints_woof(self):
        '''prints "Woof!"'''
        fido = Dog()
        captured_out = io.StringIO()
        sys.stdout = captured_out
        fido.bark()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Woof!\n")