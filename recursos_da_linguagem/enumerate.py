

"""
Módulo: enumerate.py
Objetivo: enumerar cada dado de um iterável, dentro ou fora de um loop for

Observações:
    - para funcionar em um loop for, é preciso 2 vars internas: uma para enumerate() e a outra para os dados
"""

# Uso normal
print([1], dict(enumerate('Cleber')))
print([2], list(enumerate('Diego')))
print([3], tuple(enumerate('Helena')))
print([4], cj := set(enumerate('Pedrita')))

print('========== BLOCO DE DIVISÃO ==========')

# Uso em loop for com uma var no loop
for x in enumerate(cj):
    print(x)

print('========== BLOCO DE DIVISÃO 2 ==========')

# Uso em loop for com duas vars no loop
for y, x in enumerate(cj):
    print(y, x)

print('========== BLOCO DE DIVISÃO 3 ==========')

# Uso em loop for com duas vars no loop (usando end="")
for y, x in enumerate(cj):
    print(y, x, end=' ')
