

"""
Módulo: final.py
Objetivo: decorador indicador de que uma classe não pode ter nada seu herdado, porém não bloqueia a ação

Observação:
    - no mypy, esse erro é acusado, mas não é impedido
"""

from typing import final

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 20:50
    """

"OBS"  # Para exemplificar esse arquivo, foi instalado o mypy [ pip install mypy ]

@final
class Professor:  # Essa classe não deveria ser herdada
    def __init__(self, nome):
        self.nome = nome

    @final
    def apresentar(self):  # Esse método não deveria ser sobescrito
        return f'Eu sou {self.nome}, o seu professor de Álgebra'

class Aluno(Professor):    # classe [ Aluno ] não deve herdar de [ Professor ]
    def apresentar(self):  # Esse método não deve ser sobescrito
        return f'Eu sou {self.nome}, um aluno de Álgebra'

"mypy 'final.py'"  # detecta o erro, mas não o impede

if __name__ == '__main__':
    aluno = Aluno('Alfredo')
    print(aluno.apresentar())
