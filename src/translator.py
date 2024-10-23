from src.error import PigLatinError

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


class PigLatinTranslator:

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self._phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self._phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """
        if self._phrase == "":
            return "nil"
        return PigLatinTranslator._translate_word(self._phrase)

    @staticmethod
    def _translate_word(word: str) -> str:
        starting_letter = word[0]
        if starting_letter in CONSONANTS:
            return PigLatinTranslator._translate_word_starting_consonant(word)
        elif starting_letter in VOWELS:
            return PigLatinTranslator._translate_word_starting_vowel(word)
        raise PigLatinError

    @staticmethod
    def _translate_word_starting_vowel(word: str) -> str:
        last_letter = word[-1]
        if last_letter == "y":
            return word + "nay"
        elif last_letter in VOWELS:
            return word + "yay"
        elif last_letter in CONSONANTS:
            return word + "ay"
        raise PigLatinError

    @staticmethod
    def _translate_word_starting_consonant(word: str) -> str:
        local_phrase = ""
        for char in word:
            if char in CONSONANTS:
                local_phrase += char
            else:
                break

        return word[len(local_phrase):] + local_phrase + "ay"
