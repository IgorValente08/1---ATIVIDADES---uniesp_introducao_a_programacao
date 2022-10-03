"""As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, 
e 1,00 se forem compradas pelo menos 12. Escreva um programa que leia 
o número de maçãs compradas, calcule e escreva o custo total da compra."""


ma = int(input("Quantidade de maçãs comprada?: "))

if ma < 12:
    soma = ma * 1.30
    print("valor a ser pago:",soma)

else:
    soma = ma * 1.00
    print("valoe a ser pago:",soma)