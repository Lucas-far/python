

"""
Módulo: input.py
Objetivo: entrada de texto para coletar dados externos de um usuário para ser exibido em algum algoritmo
Objetivo 2: entrada de texto para coletar dados externos de um usuário para ser salvo em algum documento

Observação:
    - O valor é passado no parâmetro do método, podendo ser string literal ou em variável
    - O input pode receber cast para variar a classe padrão (string)
"""

# Exemplos comuns de conversão
"input()"         # versão normal
"int(input())"    # versão convertida, exemplo 1
"float(input())"  # .......................... 2
"list(input())"   # .......................... 3
"tuple(input())"  # .......................... 4

# Formas de usar input menos atuais
print([1])
input('Qual o seu nome?\n-> ')
msg = 'Qual o seu nome?\n ->'
print([2])
input(msg)

# Formas de usar input mais atuais
print([2], nome := input('Qual o seu nome?\n-> '))
print([3], nome_ := 'Qual o seu nome?\n-> ', nome2 := input(nome_))
print([4])
input(f"{(pergunta := 'Qual o seu nome?')}\n-> ")

# Formas de mostrar dados de um input
linguagem, framework = 'Python', 'Django'
print([5], '%s' % linguagem)
print([6], '%s %s' % (linguagem, framework))
print([7], '{}'.format(linguagem))
print([8], '{} {}'.format(linguagem, framework))
print([9], f'{linguagem}')
print([10], f'{linguagem} {framework}')
