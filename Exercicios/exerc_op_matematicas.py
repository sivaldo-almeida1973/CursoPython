"""

Realizar a media de notas de 4 alunos

aluno1 = 8
aluno2 = 7
aluno3 = 5
aluno4 = 8

media = (aluno1 + aluno2 + aluno3 + aluno4)/ 4
print(media)

#==========================================
Ex:
notaPedro = int(input('Digite sua nota: '))
notaLucas = int(input('Digite sua nota: '))
notaSivaldo = int(input('Digite sua nota: '))
notaAlice = int(input('Digite sua nota: '))

media = (notaSivaldo + notaAlice + notaLucas + notaPedro)/4
print(f'A media das notas: {media}')

#====================================================
2)converter a temperatura de graus °C para °F e para K.
Dados : °F = °C * 1.8 + 32      e K =°C  + 273.15

"""

tempC = float(input('Digite a temperatura em °C:'))
tempF = tempC * 1.8 + 32  #converte a temperatura
print(f'A temperatura de {tempC} Graus °C ,convertida em fahrenheit {tempF} ')

tempk = tempC + 273.15
print(f'A temperatura de {tempC} Graus °C, convertida em Kelvin {tempk} ')
