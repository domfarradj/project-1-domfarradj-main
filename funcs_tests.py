import unittest
from funcs import *

class TestCases(unittest.TestCase):
	def test_poundsToKG_1(self):
		self.assertAlmostEqual(poundsToKG(20), 9.07184)
	def test_poundsToKG_2(self):
		self.assertAlmostEqual(poundsToKG(100), 45.3592) 
	def test_getMassObject_1(self):
		self.assertEqual(getMassObject('t'), 0.1)
	def test_getMassObject_2(self):
		self.assertEqual(getMassObject('g'), 5.3)
	def test_getVelocityObject_1(self):
		self.assertAlmostEqual(getVelocityObject(10), 7)
	def test_getVelocityObject_2(self):
		self.assertAlmostEqual(getVelocityObject(50), 15.6524758)
	def test_getVelocitySkater_1(self):
		self.assertAlmostEqual(getVelocitySkater(100, 5, 50), 2.5)
	def test_getVelocitySkater_2(self):
		self.assertAlmostEqual(getVelocitySkater(160, 10, 50), 3.125)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
