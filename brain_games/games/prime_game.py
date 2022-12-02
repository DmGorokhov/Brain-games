from random import randint

GAME_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number and number % divisor != 0:
        divisor += 2
    return divisor * divisor > number


def result():
    number = randint(1, 200)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
