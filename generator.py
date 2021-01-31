

"""
Módulo: generator.py
Objetivo: exibir iteráveis autodestrutivos de exibição única, para ter mais espaço em memória
Observação:
    - var gerador é, por padrão, uma tupla, que têm seus dados criptografados em um objeto de memória
    - para descriftografar esses dados, usa-se: [ casting ], ou [ next ], na var gerador
    - uma vez que o objeto é descriptografado, ele só pode ser impresso um vez, pois os dados são destruidos
    - para rever os dados, a var gerador precisa ser redeclarada
    - o ciclo é sempre: instanciar, aplicar casting ou next, imprimir, destruir, redeclarar
    - var gerador é usada por ocupar muito pouco espaço em memória (ver def comparador)
"""

from sys import getsizeof as size

# gerador com casting
semana = (x for x in range(1, 8))  # var gerador criada (início do ciclo)
print([1], semana)                 # var gerador não aplicada = objeto de memória
print([2], set(semana))            # var gerador aplicada = casting set
print([3], list(semana))           # var gerador é zerada, pois já foi usada sua única vez
semana = (x for x in range(1, 8))  # var gerador redeclarada (reinicio do ciclo)
print([4], list(semana))           # var gerador aplicada = casting lista

# gerador com next
vogais = (x for x in 'aeiou')
print([5], next(vogais))  # next precisa de print(), e mostra índice por índice
next(vogais)              # next sem print(), itera sob os dados, mas não os exibe
next(vogais)              # idem
next(vogais)              # idem
print([6], next(vogais))  # ou seja, next() + print() filtra dados que devem ser exibidos

# gerador com if
print([7], g := tuple((x for x in {*range(1, 51)} if not x % 10)))

# gerador com if else
print([8], g2 := tuple(((str(x) + '=' + str(x).replace(str(x), 'sim')) if not x % 7 else 'não' for x in range(1, 11))))

# Comparando o tamanho de tipos de dados em relação à um gerador
def comparador() -> None:
    i = int(input('Insira um número acima de 1 -> '))

    conjunto = {x for x in range(1, i)}
    dicionario = {x: x for x in range(1, i)}
    gerador = (x for x in range(1, i))
    lista = [x for x in range(1, i)]

    print(
        f"""
        Bytes consumidos em conjunto    = [ {size(conjunto)} bytes ]
        Bytes consumidos em dicionário  = [ {size(dicionario)} bytes ]
        Bytes consumidos em lista       = [ {size(lista)} bytes ]
        Bytes consumidos em gerador     = [ {size(gerador)} bytes ]
        """
    )

if __name__ == '__main__':
    comparador()
