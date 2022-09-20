'''Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), 
personalizado com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.'''

lista_de_amigos = [
    'Igor',
    'João',
    'Maria']

for nome in lista_de_amigos :
    print('Olá como vai você, {}?'.format(nome))