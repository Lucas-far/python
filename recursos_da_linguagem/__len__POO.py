

"""
Módulo: __len__POO.py
Objetivo: retornar a quantidade de dados que uma classe iterável contêm
Observação:
    - Quando o atributo de instância não é iterável: (ver class Livro & def __len__)
    - Quando o atributo de instância é iterável: (ver class Livro2 & def __len__)
"""

class Livro:
    def __init__(self, nome, autor, folhas):
        self.__nome = nome
        self.__autor = autor
        self.__folhas = folhas

    def __len__(self):        # método __len__ deve ser usado com iteráveis
        return self.__folhas  # o que não acontece aqui, pois o atributo de instância não é um iterável


class Livro2:
    def __init__(self, nome, autor, folhas):
        self.__nome = nome
        self.__autor = autor
        self.__folhas = folhas

    def __len__(self):            # método __len__ funciona com iteráveis
        return len(self.__autor)  # self.__autor é iterável (str), então está certo, mas len() precisa ser usado


if __name__ == '__main__':
    objeto = Livro('A herva maligna', 'John Alfriad', 172)  # objeto instanciado
    print(len(objeto))  # para retorno do método não iterável: len() fora do escopo
    objeto2 = Livro2('A purificação', 'Laus Stranf', 802)  # objeto instanciado
    print(len(objeto2))  # para retorno do método em iterável: len() dentro do escopo
