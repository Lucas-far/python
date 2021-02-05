

"""
Módulo: DictWriter.py

Objetivo: criar arquivo [ .csv ] (arquivo de tabela com separação dos campos por meio de vírgula)
"""

from os import chdir, getcwd
from csv import DictWriter

chdir(getcwd())
with open('dados.csv', 'w') as csv:
    # Primeiro, cria-se os dados de cabeçalho
    arquivo = DictWriter(csv, fieldnames=('Nome', 'Idade', 'Nacionalidade'))

    # Segundo, criam-se objetos, usando dicionário, repetindo cabaçalhos, e definindo seus valores
    objeto1 = {'Nome': 'Hélia', 'Idade': 27, 'Nacionalidade': 'brasileira'}
    objeto2 = {'Nome': 'Ramon', 'Idade': 19, 'Nacionalidade': 'espanhol'}

    # Por último, os cabeçalhos e objetos devem ser inseridos
    arquivo.writeheader()      # inserção do cabaçalho
    arquivo.writerow(objeto1)  # inserção do objeto em linha
    arquivo.writerow(objeto2)  # ...........................
