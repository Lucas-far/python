

"""
Módulo: def_argumentos_ordenados.py

Objetivo: ordenar os tipos de parâmetros da forma correta, para não haver erros na execução da função
"""

"Tipo 1"  # parâmetro mandatório            / recebe qualquer classe
"Tipo 2"  # parâmetro args não mandatório   / recebe qualquer classe, que será armazenada em uma tupla
"Tipo 3"  # parâmetro não mandatório        / recebe a classe declarada no parâmetro
"Tipo 4"  # parâmetro kwargs não mandatório / recebe string como chave e qualquer classe como valor

# Exemplo com todos os parâmetros
def ordem(par, *args, par2=True, **kwargs):
    return par, args, par2, kwargs

# Parâmetro mandatório
def tipo1(par):
    return par

# Parâmetro args não mandatório
def tipo2(*args):
    return args

# Parâmetro não obrigatório
def tipo3(nome='não informado'):
    return nome

# Parâmetro kwargs não mandatório
def tipo4(**kwargs):
    return kwargs

if __name__ == '__main__':
    print([1], ordem(False, None, chave='...'))
    print([2], tipo1(False))
    print([3], tipo2())
    print([4], tipo3())
    print([5], tipo4())
    print([6], var := tipo4(dicio=[*range(1, 4)]))
    print([7], var['dicio'])
