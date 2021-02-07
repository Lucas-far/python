

"""
Módulo: operadores_atribuicao.py
Objetivo: alterar um dado numérico pós-declaração, sem precisar redeclarar uma variável
"""

def exemplo():
    """"""
    # O valor abaixo será incrementado, mas isso pode ser feito de forma mais simplificada
    var = 0
    print(f'{var = }')
    var = var + 1
    print(f'{var = }')

"OBS"  # Os dados passam pelas operações especificadas, o [ = ] substitui a repetição da variável

print([1], soma := 0)
soma += 10
print([1], soma)

print([2], diminuir := 0)
diminuir -= 10
print([2], diminuir)

print([3], multiplicar := 11)
multiplicar *= 2.2
print([3], diminuir)

print([4], dividir := 7)
dividir /= 3
print([4], dividir)

print([5], elevar := 7)
elevar **= 3
print([5], elevar)

print([6], modular := 100)
modular %= 2  # operador de atribuição '%=' (se 0 = número par) (se 1 = número ímpar)
print([6], modular)

print([7], dividir_inteiro := 100)
dividir_inteiro //= 7  # divisão inteira (se o resultado é flutuante, a parte decimal é omitida)
print([7], dividir_inteiro)

# Usando operador de atribuição módular de forma mais abrangente
print([8], [x for x in range(1, 10) if x % 3])      # retirar divisíveis por 3
print([9], [x for x in range(1, 10) if not x % 3])  # manter divisíveis por 3

if __name__ == '__main__':
    exemplo()
