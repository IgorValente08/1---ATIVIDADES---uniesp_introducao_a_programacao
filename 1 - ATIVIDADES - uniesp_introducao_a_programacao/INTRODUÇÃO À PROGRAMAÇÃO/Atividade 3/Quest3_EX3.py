'''Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de 
cada pessoa acessando cada elemento da lista um de cada vez.'''

lista_de_amigos = [
    'Igor',
    'João',
    'Maria']

for nome in lista_de_amigos :
    print(f'{nome}, obrigado por vir na minha festa!')

# pelo While

x = 0
while x < len(lista_de_amigos) :
    print(f'{lista_de_amigos[x]}, obrigado por vir na minha festa!')
    x += 1