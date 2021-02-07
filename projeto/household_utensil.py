

"""

"""

def english_practice():
    """"""

    from random import choice

    colors: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m', '\033[m'
    )

    while True:
        bricks = '=' * 50

        # hold [ alt ] [ ctrl ] [ shift ] [ j ] in order to change the topic to which a library will be designed
        household_utensils = {

            # sample of key to add new content
            'sample': {
                'sample': f'{colors[3]}what is a sample?{colors[7]}',
                'description': """
                            (1) 
                        """
            },

            'fork': {
                'fork': f'{colors[3]}What is a fork?{colors[7]}',
                'definition': """
                    (1) it pierces food (1) ele perfura comida
                    (2) it is a household utensil (2) é um utensilio doméstico
                    (3) it resembles a trident (3) ele parece um trident
                """
            },

            'spoon': {
                'spoon': f'{colors[3]}what is a spoon?{colors[7]}',
                'definition': """
                    (1) it collects food
                    (2) it is a household utensil
                    (3) it is hollow (3) ela é oca
                """
            },

            'knife': {
                'knife': f'{colors[3]}what is a knife?{colors[7]}',
                'description': """
                    (1) it is an object with tears food
                    (2) it is a household utensil
                    (3) it is sharpened (3) é afiada
                """
            },
        }

        keys_available = [key for key in household_utensils.keys()]
        # print('keys_available = ', keys_available)

        key_chosen = choice(keys_available)
        # print('key_chosen = ', key_chosen)

        question = list(household_utensils.get(key_chosen).values())[0]
        # print('question = ', question)


        answer = list(household_utensils.get(key_chosen).values())[1]
        # print('answer = ', answer)

        user_guess = input(f'\n{bricks} ' + question + f' {bricks}' + '\n-> ')
        # print('user_guess = ', user_guess)

        print(f'Your answer: {user_guess}')
        print(f'Answer: {answer}')

english_practice()
