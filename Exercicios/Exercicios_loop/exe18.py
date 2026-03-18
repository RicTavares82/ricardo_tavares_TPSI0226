# Exercícios 18: Elabore um programa que leia uma entrada e diga quantos números perfeitos existem. Exemplo de numero perfeito em que somando todos os divisores ele da o numero inicial.
# 6=3+2+1 .

soma = 0
num = int(input("Escreva um numero: "))
for i in range(num):
    if (num % (i + 1)) == 0 and (i + 1) != num:
        print(i + 1)
        soma = (i + 1) + soma

print("a soma é: ", soma)

if (soma) != num:
    print(f"O numero {num} não é perfeito")
else:
    print(f"O numero {num} é perfeito")
