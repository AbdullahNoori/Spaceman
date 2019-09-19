from spaceman import is_guess_in_word, is_word_guessed, get_guessed_word
import unittest

class Spaceman(unittest.TestCase):
    def test_is_guess_in_word(self):
        # true cases + 2
        assert is_guess_in_word("r", "mark") == True
        # false cases + 2
    #def test_is_guess_in_word(self)
        assert is_guess_in_word("1", "bob") == False

    def test_is_word_guessed(self):
        # true case #3
        assert is_word_guessed("new york", "califoniah") == False

    def test_get_guessed_word(self):
        assert get_guessed_word("colombias1", "colombia") == "colombia__"



if __name__ == '__main__':
    unittest.main()
