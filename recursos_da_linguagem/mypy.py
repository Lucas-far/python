

"""
Módulo: mypy.py
Objetivo: verificar arquivos, a procura de erros mais incomuns, que o python por si, pode talvez não apontar
EXEMPLO: verificar módulos com presença de tipagem, e retornar se a tipagem correta foi aplicada
Instalar: pip install mypy
"""

def fonte():
    """
    Curso  # Programação em Python do básico ao avançado
    Seção  # Seção 24:Novidades do Python 3.8
    Aula   # 169. Tipos de dados mais precisos
    Tempo  # 03:45
    """

def tutorial():
    """
    1 - pip install mypy
    2 - ir a um diretório, e nele fazer: [ mypy 'nome do arquivo.formato' ]
    """

def mandar_mensagem(texto: str) -> str:
    return texto

print(mandar_mensagem(['Eu não gosto de panetone']))  # Há um erro aqui, mas não é anunciado na execução normal

# Verificando com mypy esse arquivo
"mypy 'mypy.py'"

# Retorno
'mypy.py:27: error: Argument 1 to "mandar_mensagem" has incompatible type "List[str]"; expected "str"'
