import prompt


def run_game(game):
    print('Welcom to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(game.GAME_QUESTION)

    for game_laps in range(3):
        question, correct_answer = game.result()
        print('Question:', question)

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct_answer was \'{correct_answer}\'.')
            return print(f'Let\'s try again, {user_name}!')

    return print(f'Congratulations, {user_name}!')
