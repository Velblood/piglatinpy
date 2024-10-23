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
        starting_letter = self._phrase[0]
        if starting_letter in CONSONANTS:
            return self._translate_word_starting_consonant()
        elif starting_letter in VOWELS:
            return self._translate_word_starting_vowel()
        raise PigLatinError

    def _translate_word_starting_vowel(self) -> str:
        last_letter = self._phrase[-1]
        if last_letter == "y":
            return self._phrase + "nay"
        elif last_letter in VOWELS:
            return self._phrase + "yay"
        elif last_letter in CONSONANTS:
            return self._phrase + "ay"
        raise PigLatinError

    def _translate_word_starting_consonant(self):
        local_phrase = ""
        for char in self._phrase:
            if char in CONSONANTS:
                local_phrase += char
            else:
                break

        return self._phrase[len(local_phrase):] + local_phrase + "ay"
