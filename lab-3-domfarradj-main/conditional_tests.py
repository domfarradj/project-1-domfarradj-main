import unittest
from conditional import *

class TestCases(unittest.TestCase):

   # This test here to make sure you named your functions correctly.
   # Any other tests you add should only have one assert per function.
   def test_max_101_1(self):
      self.assertEqual(max_101(5,3), 5)

   def test_max_101_2(self):
      self.assertEqual(max_101(7,8), 8)


   def test_max_of_three_1(self):
   	  self.assertEqual(max_of_three(3,4,5), 5)

   def test_max_of_three_2(self):
   	  self.assertEqual(max_of_three(6,7,8), 8)

   def test_rental_late_fee_1(self):
      self.assertEqual(rental_late_fee(12), 7)

   def test_rental_late_fee_2(self):
      self.assertEqual(rental_late_fee(24), 19)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

