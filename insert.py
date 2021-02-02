

"""
Módulo: insert.py
Objetivo: inserir um dado dentro de uma classe iterável lista

Observação:
    - o método possui 2 parâmetros mandatórios
    - por ser uma lista, qualquer dado de classe pode ser adicionado, não apenas dados iteráveis

    EXEMPLO SINTAXE:
        var.insert(ínt=índice onde o dado será inserido ,dado)

    - Se o índice fornecido não existir, mas for positivo, o dado é inserido no último índice
"""

# @list
print([1], lt := [])
lt.insert(0, ())
print([2], lt)
lt.insert(1, {})
print([3], lt)
lt.insert(1, set({}))
print([4], lt)
