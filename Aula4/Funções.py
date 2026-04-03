# FUNÇÕES
# Função é um bloco do codigo que pode ser chamado repetidamente evitando a repatição da escrita do codigo
# Dado pertencer a um bloco de codigo pequeno, torna-se mais facil a sua manutenção
# em segurança no scope quando bem aplicada uma função
# ----- scopes e manipulação são feitos atraves de passagem de valores ou parametros e a passagem das referencias das variaveis

# ------------------------------
# passagem por valor normal
num1 = 12
num2 = 13

# valore de retorn nome da função (parametros de entrada)
# def --> definição(função)


# forma normal na programação
# troca = 0
# troca = nu1
# nu1 = nu2
# num2 = troca

# em pyton pode ser mais facil
# nu1,nu2 = nu2,nu1


def troca(nu1, nu2):
    nu1, nu2 = nu2, nu1


troca(num1, num2)
print("num 1: ", num1, "num 2: ", num2)

# -----------------------------
# passagem por referencia de memória
lista1 = [12, 14, 15]

print("antes da função", lista1)


def insertvalue(lis):
    lis.append(19)

    insertvalue(lista1)


print("depois da função", lista1)


# -----------------------------------

# =====================================
# FUNÇÕES: PASSAGEM POR VALOR E REFERÊNCIA
# =====================================

# -------------------------------------
# 1) PASSAGEM POR VALOR (TIPOS IMUTÁVEIS)
# -------------------------------------


def troca_numero(num1, num2):
    print("\nDentro da função (antes da troca):", num1, num2)

    # Troca os valores (apenas localmente)
    num1, num2 = num2, num1

    print("Dentro da função (depois da troca):", num1, num2)

    return num1, num2  # precisa retornar para alterar fora


nu1 = 2
nu2 = 3

print("Antes da função:", nu1, nu2)

nu1, nu2 = troca_numero(nu1, nu2)

print("Depois da função:", nu1, nu2)


# -------------------------------------
# 2) PASSAGEM POR REFERÊNCIA (TIPOS MUTÁVEIS)
# -------------------------------------


def adiciona_elemento(lista):
    print("\nDentro da função (antes do append):", lista)

    # Modifica diretamente o objeto original
    lista.append(5)

    print("Dentro da função (depois do append):", lista)


listas = [1, 2, 3, 4]

print("\nAntes da função:", listas)

adiciona_elemento(listas)

print("Depois da função:", listas)
