

"""
Módulo: Final.py
Objetivo: informar que uma variável constante não deve receber alteração
Observação:
    - apesar de ferramentas como o mypy avisarem que não deve-se redeclarar uma var constante, isso não é impedido
"""

from typing import Final

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 18:50
    """

"OBS"  # Para exemplificar esse arquivo, foi instalado o mypy [ pip install mypy ]

NOME: Final = 'desconhecido'  # declarando usando Final
NOME = '...'                  # essa alteração não deveria acontecer, mas não é impedida, nem detectada (no terminal)
print(NOME)
"mypy 'Final'.py"             # se o mypy for usado, ele detecta o erro, mas não o impede
