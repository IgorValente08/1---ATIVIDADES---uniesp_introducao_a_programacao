"""Construa um algoritmo que, tendo como dados de entrada dois pontos
quaisquer do plano, P(𝑥 , ) e Q( , ), imprima a distância entre eles."""

x1 = float(input('Cordenada x do primeiro pornto: '))
y1 = float(input('Cordenada y do primeiro ponto: '))
x2 = float(input('Cordenada x do segundo ponto: '))
y2 = float(input('Cordenada x do segundo ponto: '))

dist = ((x1 - x2)**2 + (y1 - y2)**2)**0.5

print(f'A distância entre os pontos é de {dist: .2f}')