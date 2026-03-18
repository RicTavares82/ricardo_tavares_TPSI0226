# Exercícios 16: Elabore um programa que constitua a média de 30 números pares que sejam introduzidos. Validando a entrada de números inteiros entre 1 e 50.

soma = 0

for i in range(30):
    num = int(input(f"Escreva o {i+1}º num. inteiro PAR entre 1 e 50: "))
    while True:
        if (num % 2) != 0 or (num < 1 or num > 50):
            num = int(
                input("Erro!!\nEscreva corretamente um num. inteiro PAR entre 1 e 50: ")
            )
        else:
            break
    soma = num + soma
    print(soma)
print(f"A média é {soma/30:.2}")
