

"""
Módulo: or.py
Objetivo: mostrar que o operador condicional "or" possui uma sintaxe específica para uso múltiplo
Observação:
    - a variável ou literal comparado deve ser repetida em todas os usos do "or"
    - em caso das condições ocuparem mais de uma linha, usar [ \ ] e continuar na linha abaixo
"""

# condição de uma linha
nome = 'Leonardo Alves Ribeiro de Aragão'
if 'a' in nome or 'e' in nome or 'i' in nome or 'o' in nome or 'u' in nome:
    print('Há vogais!')
else:
    print('Não há vogais!')

# condição em quebra de linha
mes = 'Janeiro'
if mes == 'January' or mes == 'February' or mes == 'March' or mes == 'April' or mes == 'May' or mes == 'June' or \
  mes == 'July' or mes == 'August' or mes == 'September' or mes == 'October' or mes == 'November' or mes == 'December':
    print('Você acertou um mês em Inglês!')
else:
    print('Você é ruim em meses em Inglês!')
