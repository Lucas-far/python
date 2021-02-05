

"""
Módulo: find.py
Objetivo: retornar o número inteiro do índice de um caractere procurado, da esquerda para a direita
Observação:
    - se o dado procurado for repetido no iterável, o método retorna o primeiro encontrado, da esquerda para a direita
    - esse método é igual ao método [ index() ], porém menos eficiente
    - o método faz contagem indexada (contagem do 0)
    - para uma contagem padrão, somar o resultado do método + 1
"""

# @str
print([1], 'Albert Einstein'.find('i') + 1)  # + 1 para mostrar o posição em contagem padrão

"Diferença entre [ find() ] e [ index() ]?"
# [ index() ] filtra, podendo especificar o índice inicial e final da procura

print([2], '170270370'.find('7'))
print([3], '170270370'.index('7', 2))     # procurar '7' a partir do índice 2 até o final
print([4], '027720727'.index('7', 0, 4))  # procurar '7' a partir do índice 0 até o índice 4
