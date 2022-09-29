'''Faça um cadastro de usuários com nome, idade e email, 
utilizando apenas o que você aprendeu até agora.'''

cadastros = []


botao = 1000
while botao != 0:
    print("Digite 1 para cadastrar um novo usuário")
    print("Digite 2 para imprimir todos os usuários")
    print("Digite 0 para sair")
    botao = int(input("Digite a opção desejada: "))

    if botao == 1:

# Entrada de dados
  
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        Email = input("Digite o Email: ")

# Folha de cadastro

        dados = [nome, idade, Email]

# Guardando a folha na pasta

        cadastros.append(dados)

    elif botao == 2:

        for p in cadastros:
            print(p)

    elif botao == 0:
        print("Obrigado por acessar esse software!")

    else:
        print("Digite um número válido")