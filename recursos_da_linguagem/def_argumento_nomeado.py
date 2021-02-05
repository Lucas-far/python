

"""
Módulo: def_argumento_nomeado.py

Objetivo: simplificar a identificação de um parâmetro e seu argumento

Observação: os argumentos podem ser colocados fora de ordem, pois isso é corrigido na impressão
"""

def show_country(country='undefined', continent='undefined') -> tuple:
    return country, continent

print([1], show_country(country='Japão', continent='Ásia'))
print([2], show_country(continent='Ásia', country='Japão'))  # fora de ordem
