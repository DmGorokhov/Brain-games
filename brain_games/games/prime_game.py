from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int):
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number and number % divisor != 0:
        divisor += 2
    return divisor * divisor > number


def get_game():
    number_for_question = randint(1, 200)
    if is_prime(number_for_question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number_for_question, correct_answer
