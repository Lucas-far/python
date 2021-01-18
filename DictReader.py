

"""
Módulo: DictReader.py

Objetivo: ler arquivos [ .csv ] já criados/existentes
"""

from csv import DictReader
from os import chdir, getcwd

# Arquivo [ .csv ] a ser criado para testar esse script
def arquivo_csv():
    """
    nome,idade,esporte favorito,
    Lucas,28,ciclismo
    Luana,23,andar de patins
    Euclides,34,rugby
    """

chdir(getcwd())

# Lendo todos os dados
with open('dados.csv', 'r') as csv:
    # reading = DictReader(csv)
    for line in DictReader(csv):
        print(line)

print('\n')

# Lendo dados de forma especificada (chaves especificadas)
with open('dados.csv', 'r') as csv:
    # reading = DictReader(csv)
    for line in DictReader(csv):
        print(line['nome'])
        print(line['idade'])
        print(line['esporte favorito'])
