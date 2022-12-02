from random import choice, choices

GAME_QUESTION = 'What is the result of the expression?'


def calculate_expession(number1, number2, operation):
    if operation == '+':
        cacl_result = number1 + number2
    elif operation == '-':
        cacl_result = number1 - number2
    else:
        cacl_result = number1 * number2

    return cacl_result


def result():
    number1, number2 = choices(range(30), k=2)
    operation = choice(['+', '-', '*'])

    expression = f'{number1} {operation} {number2}'
    correct_answer = str(calculate_expession(number1, number2, operation))

    return expression, correct_answer
