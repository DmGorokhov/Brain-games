from random import randint

GAME_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def result():
    number = randint(1, 1000)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
