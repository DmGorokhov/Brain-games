from random import randint as randint, choice as choice

GAME_QUESTION = 'What number is missing in the progression?'


def get_progression():
    length = randint(5, 10)
    start_value = randint(1, 80)
    step = randint(1, 9)
    progression = list(range(start_value, start_value + (length * step), step))

    return progression


def get_game():
    progression = get_progression()
    hidden_number = choice(progression)
    progression[progression.index(hidden_number)] = '..'
    question = ' '.join([str(item) for item in progression])

    return question, str(hidden_number)
