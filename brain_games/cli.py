import prompt


def welcome_user():
    print('Welcom to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
