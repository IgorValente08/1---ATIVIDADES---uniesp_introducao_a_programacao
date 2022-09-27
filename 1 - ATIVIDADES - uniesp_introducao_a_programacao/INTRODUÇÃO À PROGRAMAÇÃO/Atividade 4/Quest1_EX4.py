"""As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, 
e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o 
número de maçãs compradas, calcule e escreva o custo total da compra."""

print('[ ! ] Promoção: a partir de 12 maçãs, o valor de cada unidade será R$ 1,00. Valor da unidade R$ 1,30 [ ! ]')
macas=int(input('Digite o número de maças que deseja comprar (0 para sair do programa): '))

preco_promocao = 1.00
preco_normal = 1.30

if macas == 0: # se digitar 0, encerra o programa
    print('Até a próxima!')
    exit(0)
elif macas < 0: # Caso digite um número negativo, mostre a mensagem de "Erro"
    print(f'o número digitado é negativo: {macas}')
    exit(1)
elif macas >= 12: # Calcula o valor total com o valor da promoção
    total = preco_promocao * macas
    print(f'Você comprou {macas} e faz parte da promoção. Valor total: R$ {total}')
else: # Calcular com o valor normal
    total = preco_normal * macas
    print(f'Voce comprou {macas} e não faz parte da promoção. Valor total: R$ {total}')