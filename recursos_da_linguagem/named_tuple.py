

"""
Módulo: named_tuple.py
Objetivo: chamar uma tupla que chame seus dados por [ notação ponto ], ao invés do método de indexação tradicional
Observação:
    - o segundo parâmetro da variável pode ser uma lista, string ou tupla, mas é mais recomendável uma tupla
    - evitar usar nomes com acentuação nos campos
    - o método possui 2 parâmetros:

        par1=rótulo para os campos (apenas um título, qualquer separador após o nome, gera erro)
        par2=iterável que armazena os campos
"""

from collections import namedtuple

# Exemplo baseado na sintaxe do [ namedtuple ]
exemplo = namedtuple('rótulo', ('campo', 'campo2', 'campo3'))
# Depois cria-se uma segunda variável para dar valor/argumento nomeado aos campos
resultado = exemplo(campo='Geografia', campo2='Álgebra', campo3='Física')

# Exemplo com os três tipos de campo
l = namedtuple('dados', ['nome', 'email', 'idade', 'país'])  # campos em lista
s = namedtuple('dados', 'nome, email, idade, país')          # campos em string
t = namedtuple('dados', ('nome', 'email', 'idade', 'país'))  # campos em tupla

# Criação da segunda var, onde são definidos os argumentos nomeados
dados = l(nome='Lucas', email='l@gmail.com', idade=21, país='Azerbaijão')
dados2 = s(nome='Farias', email='s@outlook.com', idade=40, país='Polônia')
dados3 = t(nome='Santos', email='t@yahoo.com', idade=67, país='Nepal')

# Mesmo não sendo tuplas normais, elas ainda podem ser chamadas por indexação
print([1], dados[0], dados2[1], dados3[2])

# Mas a razão de se criar uma [ namedtuple ], é para usar [ notação ponto ]
print([2], dados.nome, dados2.email, dados3.idade)
