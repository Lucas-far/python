

"""
Módulo: hash.py
Objetivo: criptografar dados, mudando seus dados visuais originais
Observação:
    - a importação do método é complexa, portanto recomenda-se um apelido
    - sua uso é recomendável em string, mas pode ser usado em outros iteráveis que contenham strings nelas

Instalação: pip install passlib
"""

from passlib.hash import pbkdf2_sha256 as codify

# @str

print([1], codify.hash('abcdefghijklmnopqrstuvwxyz'))
print([2], [codify.hash(x) for x in {'python', 'django', 'pycharm'}])
