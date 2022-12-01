from random import randint as randint, choice as choice

game_question = 'What number is missing in the progression?'


def get_progression():
    lenght = randint(5, 10)
    start_value = randint(1, 80)
    step = randint(1, 9)
    progression = list(range(start_value, start_value + (lenght * step), step))

    return progression


def result():
    progression = get_progression()
    missing_number = choice(progression)
    progression[progression.index(missing_number)] = '..'
    question = ' '.join([str(item) for item in progression])

    return question, str(missing_number)
