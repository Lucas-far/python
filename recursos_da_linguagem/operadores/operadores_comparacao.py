

"""
Módulo: operadores_comparacao.py
Objetivo: comparar dados de classe numérica, gerando um booleano dessa comparação
"""

from datetime import datetime

"OBS"  # O sinal [ = ] não faz parte dos operadores, faz parte da fstring [ f'' ]
"OBS"  # O sinal [ = ] combinado o [ f'' ] mostra a sintaxe e o resultado, ao mesmo tempo
print([1], f'{10 < 20 = }')   # operador [ menor que   ]
print([2], f'{10 <= 20 = }')  # ........ [ menor igual ]
print([3], f'{10 > 20 = }')   # ........ [ maior que   ]
print([4], f'{10 >= 20 = }')  # ........ [ maior igual ]
print([5], f'{10 == 20 = }')  # ........ [ igual       ]
print([6], f'{10 != 20 = }')  # ........ [ diferente   ]


"OBS"  # Usando operadores de comparação + (condições)
def exemplo():
    tempo = (datetime.today().hour, datetime.today().minute, datetime.today().second)
    if 0 <= tempo[0] <= 11:
        print('Bom dia')
    elif 12 <= tempo[0] <= 17:
        print('Boa tarde')
    elif 18 <= tempo[0] <= 23:
        print('Boa noite')


"OBS"  # Usando operadores de comparação + (loop for)
def exemplo2():
    hora = [*range(0, 24)]
    for h in hora:
        if h in hora[0:12]:
            print('Bom dia')
            break
        elif h in hora[12:18]:
            print('Boa tarde')
            break
        elif h in hora[18:]:
            print('Boa noite')
            break


if __name__ == '__main__':
    # exemplo()
    print(f'Resultado com função: {exemplo.__name__}')
    exemplo()
    print(f'Resultado com função: {exemplo2.__name__}')
    exemplo2()
