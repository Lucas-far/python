

"""
Módulo: join.py
Objetivo: converter uma classe iterável que contenham apenas dados de string nela, para uma classe string
Observação: método que contêm string em sua sintaxe, para adicionar caracteres separadores entre cada letra, se desejado
"""

# @dict @list @set @str @tuple
print([1], l := " ".join(['l', 'i', 's', 't', 'a']))  # string com espaço, aumenta a espaçamento das letras
print([2], t := " | ".join(('t', 'u', 'p', 'l', 'a')))
print([3], cj := "_".join({'s', 'e', 't'}))
