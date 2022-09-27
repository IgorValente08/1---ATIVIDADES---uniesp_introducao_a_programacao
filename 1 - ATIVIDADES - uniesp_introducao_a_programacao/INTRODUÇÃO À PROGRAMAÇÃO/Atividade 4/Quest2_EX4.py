"""Ler o ano atual e o ano de nascimento de uma pessoa. 
Escrever uma mensagem que diga se ela poderá ou não votar este ano 
(não é necessário considerar o mês em que a pessoa nasceu)."""


def voto (ano):


    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não pode votar!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Pode votar (opcional)!'
    else:
        return f'Com {idade} anos: Pode votar (obrigatório)!'
        
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
