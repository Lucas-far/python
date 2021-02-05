

"""
Módulo: arg_somente_posicional.py

Objetivo:
    1 - impedir o uso, em funções, de argumento nomeados (keyword arguments)
    2 - obrigar o uso, em funções, de argumento nomeados (keyword arguments)
    3 - misturar o uso, em funções, entre ser ou não obrigatório o uso de argumentos nomeados (keyword arguments)
"""

from collections import Counter

# Uso comum
def criar_dicio(chave, valor):
    return {chave: valor}

# Objetivo 1 (proibir uso de argumento nomeado) REPRESENTAÇÃO: / (último parâmetro)
def texto_invertido(texto: str = '', /):
    return texto[::-1]

# Objetivo 2 (obrigar uso de argumento nomeado) REPRESENTAÇÃO: * (primeiro parâmetro)
def contar_letras(*, texto: str = ''):
    texto = dict(Counter(texto))
    return texto

# Objetivo 3 (misturar uso obrigatório e não obrigatório)
"OBS"  # Parâmetro(s) antes da / = não podem usar argumentos nomeados
"OBS"  # Parâmetro(s) após o *   = devem usar argumentos nomeados
def mensagem(email, /, assunto='Não especificado', *, texto):
    resultado = f"""
    ========== Opinião do usuário ==========
    {email}
    {assunto}
    {texto}
    """
    return resultado

if __name__ == '__main__':
    print([1], criar_dicio(chave='linguagem', valor='Python'))
    print([2], texto_invertido('Eu não sei o que dizer'))  # Se argumento nomeado for usado aqui, gera erro
    print([3], contar_letras(texto='Estou com fome! :('))  # Se argumento nomeado não for usado, gera erro
    print([4], mensagem('lalala@gmail.com', 'Ratos', texto='Os ratos são primos dos esquilos'))
