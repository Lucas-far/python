

"""
Módulo: maxlen.py
Ojetivo: parâmetro para determinar a quantidade máxima de índices que uma classe deque pode possuir

Observação:
    - o uso desse parâmetro resulta no remoção de índices, caso o número de dados exceda
    - porém, existe uma lógica:

        * deleta-se índices à direita (se forem usados) [ appendleft ] ou [ extendleft ]
        * deleta-se índices à esquerda (se forem usados) [ append ] ou [ extend ]
"""

from collections import deque

dq = deque(range(1, 6), maxlen=5)

"Empurrão ->"
print([1], dq)
dq.appendleft(6)
print([2], dq)  # note que dado=6 empurrou para fora o dado=5, por conta da restrição de índices
dq.extendleft([7])
print([3], dq)  # note que dado=7 empurra para fora o dado=4, por conta da restrição de índices

"Empurrão <-"
dq.append(4)
print([4], dq)  # note que dado=4 empurra para fora o dado=7, por conta da restrição de índices
dq.extend([5])
print([5], dq)  # note que dado=5 empurra para fora o dado=6, por conta da restrição de índices
