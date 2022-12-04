from random import randint

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_number: int, second_number: int) -> int:
    """gcd means greatest common divisor"""

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number

    greatest_common_divisor = first_number + second_number
    return greatest_common_divisor


def get_game():
    random_number_1 = randint(2, 100)
    random_number_2 = randint(2, 100)

    question = f'{random_number_1} {random_number_2}'
    correct_answer = str(get_gcd(random_number_1, random_number_2))

    return question, correct_answer
