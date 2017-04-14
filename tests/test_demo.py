import unittest

import demo

class TestDemo(unittest.TestCase):
    def test_say_hello(self):
        expected = 'Hello foo!'
        self.assertEqual(expected, demo.say_hello('foo'))

    def test_check_code(self):
        self.assertTrue(demo.check_code())
