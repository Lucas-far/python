

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

    @property
    def _op_simbolo(self) -> str:
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

def fonte3():
    """
    Curso: || Programação em Python do básico ao avançado
    Seção: || Seção 25:Projeto Python 1 - Game
    Aula:  || 180. Implementação - Parte 1
    """

# Continuação da parte7 (edição do método: jogar)
def parte8():
    """
    def jogar(pontos: int = 0) -> None:

        text = 'Informe a nível de dificuldade desejado: [1, 2, 3 ou 4]'
        dificuldade: int = int(input(text))
        calc: Calcular = Calcular(dificuldade)
        print('Informe o resultado para a seguinte operação')
        calc.mostrar_operacao()
        resultado: int = int(input())
        if calc.checar_resultado(resultado):
            pontos += 1
            print(f'Seus pontos: {pontos} ponto(s).')
        continuar: int = int(input('Deseja continuar? [ 0 = não / 1 = sim ]'))
        if continuar:
            jogar(pontos)
        else:
            print(f'Sua pontuação final: {pontos} ponto(s).')
    """

def fonte4():
    """
    Curso: || Programação em Python do básico ao avançado
    Seção: || Seção 25:Projeto Python 1 - Game
    Aula:  || 180. Implementação - Parte 2
    """

# [ raiz / models / calcular.py ]
"OBS"  # Ao escolher a dificuldade, o método retorna um valor
"OBS"  # Esse retorno será dado aos atributos de instância [ valor1, valor2 ]
def parte9():
    """
    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1_000)
        elif self.dificuldade == 4:
            return randint(0, 10_000)
        else:
            return randint(0, 100_000)
    """

# [ raiz / teste.py ] o objeto recebe argumentos entrre  1 até 4
def parte10():
    """
    from models.calcular import Calcular

    calcular: Calcular = Calcular(1)
    print(calcular)

    EXEMPLO DE RETORNO COM DIFICULDADE 1
        Valor 1: 1
        Valor 2: 2
        Dificuldade: 1
        Operação: subtração

    EXEMPLO DE RETORNO COM DIFICULDADE 2
        Valor 1: 72
        Valor 2: 92
        Dificuldade: 2
        Operação: multiplicação

    EXEMPLO DE RETORNO COM DIFICULDADE 3
        Valor 1: 57
        Valor 2: 363
        Dificuldade: 3
        Operação: soma

    EXEMPLO DE RETORNO COM DIFICULDADE 4
        Valor 1: 320
        Valor 2: 6667
        Dificuldade: 4
        Operação: multiplicação
    """

# [ raiz / models / calcular.py ] implementação do método que calcula o resultado entre atributos de instância
def parte11():
    """
    @property
    def _gerar_resultado(self) -> int:
        if self.operacao == 1:
            return self.valor1 + self.valor2
        elif self.operacao == 2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2
    """

# [ raiz / models / calcular.py ] implementação do método que retorna o símbolo da operação
def parte12():
    """
    @property
    def _op_simbolo(self) -> str:
        if self.__operacao == 1:
            return '+'
        elif self.__operacao == 2:
            return '-'
        else:
            return '*'
    """

# [ raiz / models / calcular.py ]
def parte13():
    """
    def checar_resultado(self, resposta: int) -> bool:
        certo: bool = False

        if self.resultado == resposta:
            print('Resposta certa')
            certo = True
        else:
            print('Resposta errada')
        print(f'{self.valor1} {self._op_simbolo} {self.__valor2} = {self.__resultado}')
        return certo
    """

# [ raiz / models / calcular.py ]
def parte14():
    """
    def mostrar_operacao(self) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.__valor2} = ?')
    """
