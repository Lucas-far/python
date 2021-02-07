

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
        animals = {

            # sample of key to add new content
            'sample': {
                'sample': f'{colors[3]}what is a sample?{colors[7]}',
                'description': """
                            (1) 
                        """
            },

            'bat': {
                'bat': f'{colors[3]}What is a bat?{colors[7]}',
                'definition': """
                    (1) it is a flying beast (1) é uma besta voadora
                    (2) it can drink blood or eat fruits (2) ele pode beber sangue ou comer frutas
                    (3) it has an awful sight (3) ele têm uma vista horrível
                    (4) it sees through sound waves it throw (4) ele vê por sonoras lançadas por ele
                """
            },

            'bear': {
                'bear': f'{colors[3]}what is a bear?{colors[7]}',
                'definition': """
                    (1) it is a furry beast (1) é uma besta peluda
                    (2) it is heavy weight (2) ele é pesado
                    (3) it can kill human beings easily (3) ele pode matar seres humanos facilmente
                    (4) it is absurly strong (4) ele é absurdamente forte
                    (5) it inhabits woods around the world (5) ele habita florestas ao redor do mundo
                    (6) it drinks honey (6) ele bebe mel
                """
            },

            'chimp': {
                'chimp': f'{colors[3]}what is a chimp?{colors[7]}',
                'description': """
                    (1) it is a monkey (1) é um macaco
                    (2) it eat fruits (2) ele come frutas
                    (3) it climbs trees (3) ele sobe em árvores
                """
            },
        }

        keys_available = [key for key in animals.keys()]
        # print('keys_available = ', keys_available)

        key_chosen = choice(keys_available)
        # print('key_chosen = ', key_chosen)

        question = list(animals.get(key_chosen).values())[0]
        # print('question = ', question)


        answer = list(animals.get(key_chosen).values())[1]
        # print('answer = ', answer)

        user_guess = input(f'\n{bricks} ' + question + f' {bricks}' + '\n-> ')
        # print('user_guess = ', user_guess)

        print(f'Your answer: {user_guess}')
        print(f'Answer: {answer}')

english_practice()
