# escritas no python define o txt

nome = "Igor"
with open("Aula14_escrita.txt", "a", encoding="utf-8") as arquivo:
    for line in range(10):
        arquivo.write(f"{line} - Meu Nome é {nome}\n")

