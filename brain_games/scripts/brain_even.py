#!/usr/bin/env python3

import brain_games.cli
import brain_games.iseven_game


def main():
    user_name = brain_games.cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    user_result = brain_games.iseven_game.iseven_game_run()

    if user_result == 'victory':
        print(f'Congratulations, {user_name}!')
    else:
        print(f'Let\'s try again, {user_name}!')


if __name__ == '__main__':
    main()
