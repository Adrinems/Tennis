#!/usr/bin/env python
import unittest
import sys
sys.path.append('../')
from Tennis import Tennis

class TestTennis(unittest.TestCase):

	def testgana_1(self):
		ten = Tennis()
		self.assertEqual("0 0", ten.show_score())

		ten.add_point(1)
		self.assertEqual("15 0", ten.show_score())

		ten.add_point(2)
		self.assertEqual("15 15", ten.show_score())

		ten.add_point(1)
		self.assertEqual("30 15", ten.show_score())

		ten.add_point(1)
		self.assertEqual("40 15", ten.show_score())

		ten.add_point(1)
		self.assertEqual("GAME Player 1", ten.show_score())


	def testgana_2(self):
		ten = Tennis()
		self.assertEqual("0 0", ten.show_score())

		ten.add_point(2)
		self.assertEqual("0 15", ten.show_score())

		ten.add_point(2)
		self.assertEqual("0 30", ten.show_score())

		ten.add_point(2)
		self.assertEqual("0 40", ten.show_score())

		ten.add_point(2)
		self.assertEqual("GAME Player 2", ten.show_score())

	def testgana_22(self):
		ten = Tennis()
		self.assertEqual("0 0", ten.show_score())

		ten.add_point(2)
		self.assertEqual("0 15", ten.show_score())

		ten.add_point(2)
		self.assertEqual("0 30", ten.show_score())

		ten.add_point(1)
		self.assertEqual("15 30", ten.show_score())

		ten.add_point(2)
		self.assertEqual("15 40", ten.show_score())

		ten.add_point(1)
		self.assertEqual("30 40", ten.show_score())

		ten.add_point(1)
		self.assertEqual("DEUCE", ten.show_score())

		ten.add_point(2)
		self.assertEqual("40 ADV", ten.show_score())

		ten.add_point(2)
		self.assertEqual("GAME Player 2", ten.show_score())

	
if __name__ == "__main__":
	unittest.main()