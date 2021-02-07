

from random import choice
colors: tuple = (
    '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
)

def english_practice():
    """"""

    while True:
        bricks = '=' * 40

        words_library = {
            'fork': {f'\n{bricks} what is a fork? {bricks}\n-> ': '\nit is an object which pierces food\nit is a household utensil'},
            'spoon': {f'\n{bricks} what is a spoon? {bricks}\n-> ': '\nit is an object which collects food\nit is a household utensil'},
            'knife': {f'\n{bricks} what is a knife? {bricks}\n-> ': '\nit is an object with tears food\nit is a household utensil'}
        }

        keys_available = [key for key in words_library.keys()]
        key_chosen = choice(keys_available)
        question = list(words_library.get(key_chosen).keys())[0]
        answer = list(words_library.get(key_chosen).values())[0]

        user_guess = input(question)

        print(f'Your answer: {user_guess}')
        print(f'Answer: {answer}')
