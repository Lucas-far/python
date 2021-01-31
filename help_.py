

"""
Módulo: help_.py
Objetivo: retornar docstring matriz de um módulo alvo ou de uma função dentro do módulo alvo

EXEMPLO PARA TERMINAL:
    from help_ import criar_dicio
    help(criar_dicio)
    q

DICIONÁRIO:
    help_       =  arquivo sem extensão importado
    criar_dicio =  função pertencente ao arquivo
"""

def criar_dicio(chave, valor):
    """ Criar um dicionário """
    return {chave: valor}

help(criar_dicio)           # retornando docstring de um função dentro de um módulo alvo
print(criar_dicio.__doc__)  # outra forma
