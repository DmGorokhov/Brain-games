from random import choice, choices

GAME_QUESTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def calculate_expession(first_number, second_number, operation):
    if operation == '+':
        calc_result = first_number + second_number
    elif operation == '-':
        calc_result = first_number - second_number
    else:
        calc_result = first_number * second_number

    return calc_result


def get_game():
    random_num_1, random_num_2 = choices(range(30), k=2)
    operation = choice(OPERATORS)

    question = f'{random_num_1} {operation} {random_num_2}'
    correct_answer = calculate_expession(random_num_1, random_num_2, operation)

    return question, str(correct_answer)
