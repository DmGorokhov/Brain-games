import prompt


def run_game(game):
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(game.GAME_QUESTION)

    for game_laps in range(3):
        question, correct_answer = game.get_game()
        print('Question:', question)

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct_answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {user_name}!')
            return

    print(f'Congratulations, {user_name}!')
    return
