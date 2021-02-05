

"""
Módulo: get.py
Objetivo: retornar o valor de uma chave especificada no parâmetro do método
Observação:
    - se a chave especificada no parâmetro não existir no dicionário, o retorno é None, ou seja, não gera erro
    - o método possui um parâmetro 2, para inserir uma mensagem string, ativada quando a chave não é encontrada
"""

# @dict

d = {'chave': 'valor', 'classe': 'dict'}
print([1], d.get('classe', 'Não encontrado'))
print([2], {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}.get('i', 'Dado não encontrado'))  # usando os 2 pars
print([3], {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}.get('f', 'Dado não encontrado'))  # usando os 2 pars
