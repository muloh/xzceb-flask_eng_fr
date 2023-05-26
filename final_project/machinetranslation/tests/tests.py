import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
	def test_en_fr(self):
		self.assertEqual(english_to_french("Hello"), 'Bonjour')
		self.assertNotEqual(english_to_french("Hello"), 'Hi')
		self.assertNotEqual(english_to_french("None"), '')
		self.assertNotEqual(english_to_french(0), 0)


class TestFrenchToEnglish(unittest.TestCase):
	def test_fr_en(self):
		self.assertEqual(french_to_english('Bonjour'), "Hello")
		self.assertNotEqual(french_to_english("None"), '')

unittest.main()

