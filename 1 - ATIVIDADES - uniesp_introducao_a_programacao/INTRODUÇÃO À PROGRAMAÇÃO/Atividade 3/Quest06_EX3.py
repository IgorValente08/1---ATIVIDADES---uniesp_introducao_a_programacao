"""a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome
personalizado.
c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
convites. Imprima o nome das pessoas que não poderão comparecer.
d. Modifique sua lista, substitua os desistentes por novos convidados.
e. Exiba um novo convite para cada pessoa que continua presente em sua lista."""

#Convite

convidados = [
    "igor", "Thor", "Hercules", "Goku", "Loki"

]

for nome in convidados:
    mensagem = f"Bora pra balada, {nome}!"
    print(mensagem)

# Quem não poderá ir

print("Thor: infelizmente não posso estar no mesmo ambiente que o Hercules!")

print("Goku: infelizmente não posso estar no mesmo ambiente que o Hercules!")

#Modifique sua lista, substitua os desistentes por novos convidados.

convidados [1] = "Capitão America"
convidados [3] = "Hulk"

# Convite

for nome in convidados:
    mensagem = f"Bora pra balada, {nome.upper()}!"
    print(mensagem)