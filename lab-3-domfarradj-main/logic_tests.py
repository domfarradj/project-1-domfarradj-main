import unittest
from logic import *

class TestCases(unittest.TestCase):

	def test_is_even_1(self):
		self.assertTrue(is_even(6))

	def test_is_even_2(self):
		self.assertFalse(is_even(7))

	def test_in_an_interval_1(self):
		self.assertTrue(in_an_interval(2))

	def test_in_an_interval_2(self):
		self.assertFalse(in_an_interval(9))




      
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

