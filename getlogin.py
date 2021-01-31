

"""
Módulo: getlogin.py
Objetivo: retornar o nome de usuário de alguém no seu OS
"""

from os import getcwd, getlogin
print(getlogin())
print(getcwd() + '/' + getlogin())
