"""Índice de Massa Corporal - é um critério da Organização Mundial da Saudade para indicar a
condição de peso de uma pessoa. A fórmula é IMC = peso / (altura)². Elabore um algoritmo que leia o
peso e a altura de uma adulto e mostre sua condição."""

import os
 
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))
 
imc = peso / altura**2
 
print("Seu IMC é: %.4f" % imc)
 

if imc < 18.5:
	print("Abaixo do peso")
elif imc < 25:
	print("Peso normal")
elif imc < 30:
	print("Acima do peso")
else:
	print("Obeso")
 
os.system("pause")