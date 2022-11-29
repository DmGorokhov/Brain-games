from random import randint

game_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_number):
    if random_number % 2 == 0:
        return True
    else:
        return False


def result():
    random_number = randint(1, 1000)
    if is_even(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
