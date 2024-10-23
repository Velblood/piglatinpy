from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        word = "Hello word"
        translator = PigLatinTranslator(word)
        phrase = translator.get_phrase()
        self.assertEqual(word, phrase)
