

"""
Módulo: datetime.now.py

Objetivo: retornar a data agora, neste momento, de forma geral (data e hora), ou específica (data ou hora)
"""

from datetime import datetime

print(f'Que dia é hoje? {datetime.now()}')  # Uso de forma geral

# Uso de forma especifica
print('ano', datetime.now().year)
print('mês', datetime.today().month)
print('dia', datetime.now().day)
print('hora', datetime.today().hour)
print('minuto', datetime.now().minute)
print('segundo', datetime.today().second)
print('microsegundo', datetime.now().microsecond)
print('dia da semana', datetime.today().weekday())    # Contagem iniciada pelo índice 0 (dia da semana)
print('dia da semana', datetime.now().isoweekday())   # Contagem iniciada pelo índice 1 (dia da semana)
