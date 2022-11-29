import random

game_question = 'What is the result of the expression?'


def calculate_expession():
    number1, number2 = random.choices(range(30), k=2)
    operation = random.choice(['+', '-', '*'])

    expression = f'{number1} {operation} {number2}'

    if operation == '+':
        correct_answer = str(number1 + number2)
    elif operation == '-':
        correct_answer = str(number1 - number2)
    else:
        correct_answer = str(number1 * number2)

    return expression, correct_answer


def result():
    return calculate_expession()
