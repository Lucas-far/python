

"""
Módulo: dump.py
Objetivo: a pesquisar...
"""

# from os import chdir
# from pickle import dump, load
#
# # Não faz parte do contexto, mas deseja-se fazer isso em outro local do sistema
# chdir('/home/lucas/Documents')
#
# class Dados:
#     @staticmethod
#     def vazio():
#         return 'Eu sou um método inútil'
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     def __init__(self, nome: str = '', idade: int = 1, nacionalidade: str = 'indefinida'):
#         self.__nome: str = nome
#         self.__idade: int = idade
#         self.__nacionalidade: str = nacionalidade
#
#     def get_nome(self):
#         return self.__nome
#
# if __name__ == '__main__':
#     pessoa = Dados('Robertcleuson', 87, 'brasileiro')
#     print(pessoa)
#
#     # O método [ dump() ] cria um arquivo [ .csv ], para armazenar dados de uma variável objeto
#     with open('dados3.csv', 'wb') as doc:
#         # dump(objeto, var with)
#         dump(pessoa, doc)
#
#     # O método [ load() ] lê os dados do arquivo [ .csv ] criado
#     with open('dados3.csv', 'rb') as doc2:
#         leitura = load(doc2)
#         print(leitura.vazio())
#         print(leitura.nome)
#         print(leitura.get_nome())
