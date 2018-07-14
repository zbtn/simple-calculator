import os
import sys
#import unittest

sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../../lib')
from calculate.calculate import Calculate

#class TestCalculate(unittest.TestCase):
#	def setUp(self):
#		self.calc = Calculate()
#	def test_add_function(self):
#		self.assertEqual(4, self.calc.add(2,2))
#	def test_multiply_function(self):
#		self.assertEqual(4, self.calc.multiply(2,2))
#		self.assertEqual(25, self.calc.multiply(5,5))

calc = Calculate()

def test_add_function():
	"""Test if 2 plus 2 is equal 4."""
	assert calc.add(2,2) == 4

def test_multiply_function():
	"""Test if multiplying really multiply."""
	assert calc.multiply(2,2) == 4
	assert calc.multiply(5,5) == 25

if __name__ =='__main__':
	unittest.main(exit = False)
