'''Faça um programa que receba um número 
e que calcule e mostre a tabuada desse número.'''


for multiplicador in range(0, 11):
    print("tabuada do {} ----- ".format(multiplicador))

    for multiplicando in range(0, 11):

        resultado = multiplicador * multiplicando
        print(str(multiplicador) + "x" + str(multiplicando) \
            + " = " + str(resultado))