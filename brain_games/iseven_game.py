import prompt
from random import randint


def iseven_single_game():
    random_number = randint(1, 1000)
    print('Question:', random_number)

    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    user_answer = prompt.string('Your answer: ')

    if user_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'\'{user_answer}\' is wrong answer ;(. '
              f'Correct_answer was \'{correct_answer}\'.')
        return False


def iseven_game_run():
    for laps in range(3):
        lap_result = iseven_single_game()
        if lap_result == 0:
            return
    return 'victory'
