

"""
Módulo: open_.py
Objetivo: abrir um arquivo existente, para fazer sua leitura
Objetivo2: criar um arquivo e inserir conteúdo, que é opcional
Observação:
    - há uma versão melhorada desse método: [ with open('arquivo.formato', 'prefixo') as var ]
    - se optar por usar esse método, ao final, é preciso especificar o fechamento com o método [ .close() ]
    - ver exemplos abaixo...
"""

from os import chdir

chdir('/home/lucas/Documents/')  # mudando a rota para criar módulo na área de trabalho

"FORMA MENOS ATUAL"  # Criação de arquivo, com sobreposição de dados: par2='w'
def exemplo_1() -> None:
    arquivo = open('z.txt', 'w')  # criação e escrita (w = write)
    arquivo.write('linha 1\n')    # adição de conteúdo
    arquivo.close()               # fechar arquivo (mandatório)
    arquivo = open('z.txt', 'w')  # arquivo não é recriado, mas aberto
    arquivo.write('linha 2')      # adição de conteúdo (sobreposição)
    arquivo.close()               # fechar arquivo (mandatório)


"FORMA MENOS ATUAL"  # Criação de arquivo, com acumulação de dados: par2='a'
def exemplo_2() -> None:
    arquivo = open('z2.txt', 'a')
    arquivo.write('linha 1\n')
    arquivo.close()
    arquivo = open('z2.txt', 'a')
    arquivo.write('linha 2')
    arquivo.close()


"FORMA MENOS ATUAL"  # Leitura de arquivo existente: par2='r'
def ler_exemplo_2() -> None:
    arquivo = open('z2.txt', 'r')  # pegue arquivo do par1 e faça sua leitura
    print(ler := arquivo.read())   # variável que armazena a leitura (criação e print ao mesmo tempo)
    arquivo.close()                # fechar arquivo (mandatório)


"FORMA MAIS ATUAL"  # Criação de arquivo, com sobreposição de dados: par2='w'
def exemplo_3() -> None:
    with open('z3.txt', 'w') as txt:  # criação da variável na declaração
        txt.write('linha 1\n')        # adição de conteúdo
        "OBS"  # usando with open(), não é necessário fechar o arquivo
    with open('z3.txt', 'w') as txt:  # reabertura
        txt.write('linha 2')          # adição de conteúdo (sobreposição)

"FORMA MAIS ATUAL"  # Criação de arquivo, com acumulação de dados: par2='a'
def exemplo_4() -> None:
    with open('z4.txt', 'a') as txt:
        txt.write('linha1\n')
    with open('z4.txt', 'a') as txt:
        txt.write('linha2')

"FORMA MAIS ATUAL"  # Leitura de arquivo existente: par2='r'
def ler_exemplo_4() -> None:
    with open('z4.txt', 'r') as txt:
        print(ler := txt.read())

if __name__ == '__main__':
    exemplo_1()
    exemplo_2()
    ler_exemplo_2()
    exemplo_3()
    exemplo_4()
    ler_exemplo_4()
