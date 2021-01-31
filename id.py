

"""
Módulo: id.py
Objetivo: criar um identificador inteiro para qualquer tipo de classe, literal ou em variável
"""

def criar_identificador(classe, dado):
    print(classe, id(dado))

if __name__ == '__main__':
    criar_identificador('booleano', True)
    criar_identificador('complexo', 7j)
    criar_identificador('dicionário', {'c': 'v'})
    criar_identificador('flutuante', 7.0)
    criar_identificador('inteiro', 7)
    criar_identificador('lista', ['l'])
    criar_identificador('nenhum', None)
    criar_identificador('range', range(1, 4))
    criar_identificador('conjunto', {'cj'})
    criar_identificador('string', 's')
    criar_identificador('tupla', ('t',))

l = []
l2 = []
print([1], id(l) == id(l2))  # Mesmo sendo iguais, variáveis nunca criam ids idênticos
