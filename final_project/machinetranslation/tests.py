import unittest
from translator import english_to_french, french_to_english

class TestLanguageTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello everyone.'), 'Bonjour à tous.')
        self.assertEqual(english_to_french('Goodbye.'), 'Au revoir.')
        self.assertEqual(english_to_french('How are you?'), 'Comment allez-vous ?')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertEqual(french_to_english('Comment allez-vous ?'), 'How are you?')

if __name__ == '__main__':
    unittest.main()
