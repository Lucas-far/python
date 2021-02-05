

"""
Módulo: __annotations__.py

Objetivo: criar um dicionário que retorna as classes especificadas nos parâmetros em função

Objetivo 2: criar um dicionário que retorna as classes especificadas nos atributos de instância em POO
"""

# [ .__annotations__ ] em POO
class Dados:
    # Método de instância com decorador, não aceita o método
    @property
    def nome(self) -> str:
        return self.__nome

    # Atributos de instância aceitam o método...se há tipagem tipagem + __init__
    def __init__(self, nome: str, idade: int, calvice: bool):
        self.__nome = nome
        self.__idade = idade
        self.__calvice = calvice

    # Métodos de instância sem decorador, aceitam o método...se há tipagem especificada
    def exibir_nome(self) -> str:
        return self.__nome

pessoa = Dados('Lucas', 28, False)
print([1], pessoa.__init__.__annotations__)
print([2], pessoa.exibir_nome.__annotations__)

"Exemplo errado"  # print(pessoa.nome.__annotations__)

# [ .__annotations__ ] em uma função normal (tipagem obrigatória)
def dados(nome: str, idade: int, calvice: bool):

    if calvice:
        calvice = 'Sim'
    else:
        calvice = 'Não'

    return \
        f"""
        Dados:
        1. Nome: {nome}
        2. Idade: {str(idade) + ' anos'}
        3. Possui calvice? {calvice}
        """

if __name__ == '__main__':
    dados('Lucas', 28, False)
    print([3], dados.__annotations__)
