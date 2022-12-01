from random import randint

game_question = 'Find the greatest common divisor of given numbers.'


def get_gcd(number1, number2):
    """gcd means greatest common divisor"""

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1

    greatest_common_divisor = number1 + number2
    return greatest_common_divisor


def result():
    number1 = randint(2, 100)
    number2 = randint(2, 100)

    question = f'{number2} {number1}'
    correct_answer = str(get_gcd(number1, number2))

    return question, correct_answer
