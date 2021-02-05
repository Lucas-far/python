

"""
Módulo: keys.py
Objetivo: mostrar todas e somente as chaves contidas em uma classe dicionário
Observação:
    - dicionários sob a influência do método, tornam-se incapazes de chamar chave
    - para corrigir esse comportamento, o dicionário precisa receber cast iterável (ver def detalhes)
"""

# @dict

print([1], {'chave': 'valor', 'chave2': 'valor2'}.keys())
print([2], d := {'1': 1, '2': 2.0, '3': 3j}.keys())

# Um dicionário perde-se o acesso por chave ao usar: .keys() ou .items() ou .values()
try:
    print(d['1'])  # tentativa de chamada de chave falha, por causa do método [ .keys() ]
except TypeError as error:
    print('\033[1:32m' + str(error) + '\033[m')

# O novo acesso agora só é possível por cast
print([3], list(d)[1])
print([4], list(d).pop(list(d).index('2')))  # não lembro porque eu fiz isso
