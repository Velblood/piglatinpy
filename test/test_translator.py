from unittest import TestCase

from src.error import PigLatinError
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

    def test_translate_word_starting_vowel_ending_consonant(self):
        translator = PigLatinTranslator("ink")
        translate = translator.translate()
        self.assertEqual("inkay", translate)

    def test_translate_word_starting_vowel_ending_invalid_char(self):
        translator = PigLatinTranslator("ink1")
        self.assertRaises(PigLatinError, translator.translate)

    def test_translate_word_starting_consonant(self):
        translator = PigLatinTranslator("hello")
        translate = translator.translate()
        self.assertEqual("ellohay", translate)

    def test_translate_word_starting_y(self):
        translator = PigLatinTranslator("y")
        translate = translator.translate()
        self.assertEqual("yay", translate)

    def test_translate_word_starting_invalid_char(self):
        translator = PigLatinTranslator("1ay")
        self.assertRaises(PigLatinError, translator.translate)

    def test_translate_word_starting_more_consonants(self):
        translator = PigLatinTranslator("known")
        translate = translator.translate()
        self.assertEqual("ownknay", translate)
