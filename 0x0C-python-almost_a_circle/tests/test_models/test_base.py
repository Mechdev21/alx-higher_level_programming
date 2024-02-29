#!/usr/bin/python3
"""Base test module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Base Test"""

    def setUp(self):
        '''setup method'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''cleanup aftyer each test'''
        pass

    def test_Base__nb_objects(self):
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_Base_value(self):
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_A_Instance_creation(self):
        """Creating an instance"""
        b1 = Base()
        self.assertTrue(b1.id == 1)
        self.assertEqual(b1.__dict__, {"id":1})
        self.assertTrue(hasattr(b1, "id"))
        self.assertTrue(isinstance(b1, Base))

    def test_B_constructor(self):
        '''testing constructor'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_C_Constructor_2(self):
        '''testing if multiple args passd'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "__init__() takes from 1 to 2 positional argument but 3\
                were given"
        self.assertTrue(str(e.exception), msg)

    def test_D_sync(self):
        '''test to see the value'''
        b = Base()
        self.assertEqual(Base._Base__nb_objects, b.id)

    def test_E_Continiuty(self):
        '''Test for increment in nb_objects'''
        b1 = Base()
        b3 = Base(12)
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_str(self):
        b = Base()
        b3 = Base(98)
        b4 = Base("favour")
        b5 = Base()
        self.assertEqual(b5.id, Base._Base__nb_objects)
