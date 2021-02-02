

"""
Módulo: items_keys_values.py
Objetivo: mostrar formas diferentes de iterar sob um dicionário, usando métodos diferentes
"""

d = {'nome': 'Alfredo Costa', 'idade': 43, 'calvice': False, 'atleta': True}

# Forma 1 (apenas chave)
for key in d:
    print('sem método ||', key)

# Forma 2 [ .items() ] (chave e valor em forma de tupla)
for key_value in d.items():
    print('.items() ||', key_value)

# Forma 3 [ .keys() ] == Forma 1
for key_ in d.keys():
    print('.keys() ||', key_)

# Forma 4 [ .values() ] (apenas valor)
for value in d.values():
    print('.values() ||', value)
