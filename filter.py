

"""
Módulo: filter.py
Objetivo: filtrar dado(s) em uma classe iterável, retirando ou isolando esse dado
Observação:
    - funciona sob a influência mandatória da função lambda
    - na função lambda, trabalha-se majoritariamente com operações relacionais ou condições simples
    - método dependente de casting ou next() para convertê-lo num objeto visível
"""

"OBS"  # também pode ser feito com: range e tupla

# Conjunto
cj = {False, None, True, '...'}
print([1], cj2 := list(filter(lambda x: x is False, cj)))     # isolar
print([2], cj3 := list(filter(lambda x: x is not None, cj)))  # retirar
print([3], cj4 := list(filter(lambda x: x == '...', cj)))     # isolar
print([4], cj5 := list(filter(lambda x: x != '...', cj)))     # retirar

# Dicionário
d = {0: 0, 1.0: 1.0, 2j: 2j}
print([5], d2 := tuple(filter(lambda x: x == 1.0, d)))  # isolar
print([6], d3 := tuple(filter(lambda x: x != 0, d)))    # retirar

# Lista
l = ['string', ('tupla',), ['lista']]
print([7], l2 := set(filter(lambda x: x == ('tupla',), l)))  # isolar
print([8], l3 := set(filter(lambda x: x != ['lista'], l)))   # retirar

# String
s = 'Albuquerque'
print([9], s2 := ''.join(list(filter(lambda x: x == 'l', s))))
print([10], s3 := ''.join(list(filter(lambda x: x != 'b', s))))
print([11], s4 := ''.join(list(filter(lambda x: x != 'q' and x != 'u' and x != 'e' and x != 'r', s))))

# filter() + if..........se string 'a' existe em algum dos dados da var abaixo
nome = ['Tereso', 'Marcos', 'Alfredo', 'de', 'Palmeira']
print([12], nomefil := ' '.join(list(filter(lambda x: x if 'a' in x else None, nome))))

# filter() + if + next()
nome2 = filter(lambda x: x if 'e' in x else None, nome)
next(nome2)               # 'Tereso' é saltado
print([13], next(nome2))  # O segundo que contenha a letra 'e' é exibido
