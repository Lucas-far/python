

"""
Módulo: finally.py
Objetivo: lançar uma mensagem alternativa após o tratamento de um erro específico
Observação:
    - [ finally ] existe quando [ try ] e [ except ] são usados, mas [ finally ] não baseia-se neles
"""

# Exemplo com erro, onde [ except ] é ativado junto ao [ finally ]
try:
    nome = 'Lucas'
    print([1], nome[-7])
except IndexError as index:
    print([2], f'===== Erro da IDE: ===== {index}')  # Erro da IDE em uma variável
finally:
    print([3], '===== Mensagem [finally] ===== Erro tratado com sucesso!')

# Exemplo sem erro, onde [ try ] é ativado junto ao [ finally ]
try:
    nome = 'Lucas'
    print([4], nome[0])
except IndexError as index:
    print([5], f'===== Erro da IDE: ===== {index}')
finally:
    print([6], f'===== Mensagem [finally] ===== Erro tratado com sucesso!')
