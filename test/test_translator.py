from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        word = "Hello word"
        translator = PigLatinTranslator(word)
        phrase = translator.get_phrase()
        self.assertEqual(word, phrase)

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        translate = translator.translate()
        self.assertEqual("nil", translate)

    def test_translate_word_starting_vowel_ending_y(self):
        translator = PigLatinTranslator("any")
        translate = translator.translate()
        self.assertEqual("anynay", translate)

    def test_translate_word_starting_vowel_ending_vowel(self):
        translator = PigLatinTranslator("eye")
        translate = translator.translate()
        self.assertEqual("eyeyay", translate)
