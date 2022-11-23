
#lendo td que possui no arquivo txt
# "ls" para listar conteúdo de um diretório
# "cd" mudar de diretório

#with open("Aula14.txt", "r", encoding="utf-8") as arquivo:
#    conteudo = arquivo.read()
#    print(conteudo)


#with open("Aula14.txt", "r", encoding="utf-8") as arquivo:
#    x = 0
#    for linha in arquivo:
#        print(f"linha: {x} Conteúdo: {linha}")
#        x = x + 1

arquivo_de_linhas = []

with open("Aula14.txt", "r", encoding="utf-8") as arquivo:
    arquivo_de_linhas = arquivo.readlines()

print(arquivo_de_linhas)

