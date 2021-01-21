

"""
Módulo: aulas_sobre_jogo.py
Palavra chave: udemy jogo
"""

def fonte():
    """
    Curso: || Programação em Python do básico ao avançado
    Seção: || Seção 25:Projeto Python 1 - Game
    Aula:  || 178. Criando nosso projeto
    """

# Criando projeto e arquivos necessários
def parte1():
    """
    1 - Criação de um projeto
    2 - [ raiz - botão direito - new - python package - models ]
    3 - [ models - botão direito - new - python file - calcular ]
    4 - [ raiz - botão direito - new - python file - teste ]
    5 - [ raiz - botão direito - new - python file - game ]
    """

def fonte2():
    """
    Curso: || Programação em Python do básico ao avançado
    Seção: || Seção 25:Projeto Python 1 - Game
    Aula:  || 179. Estruturando nosso código
    """

"OBS"  # Códigos abaixo adicionados em: [ raiz / models / calcular.py ]

# Criação o método inicializador
def parte2():
    """
    from random import randint

    class Calcular:
        def __init__(self: object, dificuldade: int) -> None:
            self.__dificuldade: int = dificuldade
            self.__valor1: int = self._gerar_valor
            self.__valor2: int = self._gerar_valor
            self.__operacao: int = randint(1, 3)  # 1 +   2 -   3 *
            self.__resultado: int = self._gerar_resultado
    """

# Criação das propriedades dos atributos de instância
"OBS"  # Na aula, foram criados abaixo do método inicializador
"OBS"  # Porém, foi ensinado anteriormente que métodos com decorador de propriedades, são colocados acima
def parte3():
    """
    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    @property
    def _gerar_valor(self: object) -> int:
        pass

    @property
    def _gerar_resultado(self: object) -> int:
        pass
    """

# Criação do método __str__
def parte4():
    """
    def __str__(self: object) -> str:
        op: str = ''

        if self.__operacao == 1:
            op = 'soma'
        elif self.__operacao == 2:
            op = 'subtração'
        elif self.__operacao == 3:
            op = 'multiplicação'
        else:
            op = 'operação inválida'

        return f'''
        Valor 1: {self.__valor1}
        Valor 2: {self.__valor2}
        Dificuldade: {self.__dificuldade}
        Operação: {op}
        '''
    """

# Criação de outros métodos (implementação futura)
def parte5():
    """
    def checar_resultado(self: object, resposta: int) -> bool:
        pass

    def mostrar_operacao(self: object) -> None:
        pass
    """

"OBS"  # Códigos abaixo adicionados em: [ raiz / teste.py ]

# Testagem
def parte6():
    """
    from models.calcular import Calcular
    calcular: Calcular = Calcular()
    print(calcular)
    """

"OBS"  # Códigos abaixo adicionados em: [ raiz / game.py ]

def parte7():
    """
    from models.calcular import Calcular

    def jogar(pontos: int = 0) -> None:
        pass

    def main() -> None:
        pontos: int = 0
        jogar(pontos)

    if __name__ == '__main__':
        pass
    """
