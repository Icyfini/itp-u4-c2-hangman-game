from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['rmotr', 'Python', 'coding']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    return random.choice(list_of_words)


def _mask_word(word):
    if not word:
        raise InvalidWordException
    masked_word = ''
    for char in word:
        masked_word += "*"
    return masked_word


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or len(answer_word) != len(masked_word):
        raise InvalidWordException
    if not character or len(character) > 1:
        raise InvalidGuessedLetterException

    guessed_word = ""
    for index, letter in enumerate(answer_word):
        if letter.lower() == character.lower():
            guessed_word += letter.lower()
        else:
            guessed_word += masked_word[index]
    return guessed_word




def guess_letter(game, letter):
    if game['masked_word'] == game['answer_word'] or game['remaining_misses'] <= 0:
        raise GameFinishedException

    game['masked_word'] = _uncover_word(game['answer_word'], game["masked_word"], letter)
    game['previous_guesses'].append(letter.lower())
    if letter.lower() not in game['masked_word']:
        game['remaining_misses'] -= 1
    if game['remaining_misses'] <= 0:
        raise GameLostException
    if game['masked_word'] == game['answer_word']:
        raise GameWonException



def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
