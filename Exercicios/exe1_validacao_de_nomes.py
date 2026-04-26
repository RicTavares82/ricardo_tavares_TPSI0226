# Cria um programa que peça ao utilizador para introduzir o seu nome completo. O programa deve validar se o nome contém apenas letras e espaços, a primeira letra do nome deve ser sempre maiúscula e a seguir ao espaço também, usando os códigos ASCII de cada caractere.
# Exemplo:
# Pedro Pereira

# Se o nome for válido, o programa deve exibir:
#  "Nome válido!"
# Caso contrário, deve exibir:
#  "Nome inválido: contém caracteres não permitidos."

# No caso de o programa encontrar um caractere invalido deve parar a execução.

# Exemplos Inválidos:
# Miguel PriMo
# Luis AnseLmo
# Guilherme ramos


def introduzirNome():
    nomeF = input("Escreva o seu nome completo: ")
    return nomeF


# print(nome[0])

flag = True

while flag:
    contador = 0
    nome = introduzirNome()
    listaNome = nome.split()
    caracteres_invalidos = False

    if len(listaNome) < 2:
        print("Nome Completo inválido")
        continue

    for x in listaNome:
        if not x.isalpha():
            print("Nome inválido: contém caracteres não permitidos.--- Outros digitos.")
            caracteres_invalidos = True
    if caracteres_invalidos:
        continue

    for i in range(len(listaNome)):
        # print("i", i)
        for y in range(len(listaNome[i])):
            # print("y", y)
            if y == 0:
                if i >= 1 and listaNome[i][y] > "Z":
                    print(
                        "Nome inválido: contém caracteres não permitidos. Primeira letra Segundo nome"
                    )
                    contador += 1
                    break

                if listaNome[i][y] > "Z":
                    print(
                        "Nome inválido: contém caracteres não permitidos. Primeira letra"
                    )
                    contador += 1
                    # print("contador", contador)
                    break

            if y >= 1:
                if listaNome[i][y] <= "Z":
                    print(
                        "Nome inválido: contém caracteres não permitidos. Letras do meio"
                    )
                    contador += 1
                    # print("contador", contador)
                    break
        if contador >= 1:
            break
    if contador == 0:
        print("Nome válido!")
        break
