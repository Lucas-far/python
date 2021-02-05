

"""
Módulo: most_common.py
Objetivo: filtrar através de um inteiro, o número de ocorrência de letras, caso classe string
Objetivo 2: filtrar através de um inteiro, o número de ocorrência de palavras, caso outras classes iteráveis

Observação:
    - método complementar de outro: Counter()
    - método gerador de lista com dados tupla, ao invés de dicionário
    - método não faz sentido ser usado com classes: conjunto, dicionário
    - em conjunto, dados não repetem-se
    - em dicionário, chaves não repetem-se
"""

from collections import Counter

# @list @range @set @str @tuple

# Comportamento em iteráveis == str (contagem de letras)
print([1], Counter('t2vsd4m3fov5w4vul4faks2wxydc3uxomfomh25qoehvlvbqig4no6tasznizlgxewx7os').most_common(2))

# Comportamento em iteráveis != str (contagem de palavras)
print([2], l :=
      Counter("""
      Olá, Lucas Farias Santos,
      Sua senha de login foi alterada. Se você acha que isso seja um erro, clique no botão abaixo para acessar
      nosso portal de suporte, onde você poderá entrar em contato com nossa equipe de suporte. Entre em contato
      com a equipe de suporte
      """.split()).most_common(3))
