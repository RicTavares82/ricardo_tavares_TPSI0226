# Exercício 1: Crie um algoritmo que mostre os 30 primeiros números ímpares e pares.

# Cria a função
import random

# cria um int random num intervalo específico (ex: 1 a 10)
num = random.randint(1, 10)
print(f"Inteiro: {num}")

print()
# cria numero decimal (float) entre 0 e 1
num2 = random.random()
print(f"Decimal entre 0 e 1: {num2}")

print()
# cria numero decimal num intervalo específico (ex: 10 a 20)
num3 = random.uniform(10, 20)
print(f"Decimal entre numeros escolhidos: {num3}")

print()
# inserir numeros aleatorios numa lista
numerosSorteados = []  # lista
for i in range(5):
    num = random.randint(1, 10)  # Gerar um NOVO numero em cada volta
    print(f"Tentativa {i+1}: {num}")
    numerosSorteados.append(num)
print(f"uma lista: {numerosSorteados}")

# usar random para escolher directamente dentro de uma lista
opcoes = ["pedra", "papel", "tesoura"]
print(opcoes)
escolha_computador = random.choice(
    opcoes
)  # escolhe um indice dentro da lista (exemplo) opcoes.
print(f"O computador escolheu: {escolha_computador} dentro de da lista")


# melhor opçao é usar uma função --> sempre que é chamada retorna um numero novo.


def novo_numero():
    return random.randint(1, 10)


# função criada

# Cada vez que chamas a função com (), ela gera um valor novo
print(novo_numero())
print(novo_numero())
print(novo_numero())
