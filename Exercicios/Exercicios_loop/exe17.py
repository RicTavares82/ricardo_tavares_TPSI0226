# Exercícios 17: Elabore um programa que determine os múltiplos de 5 mas não múltiplos de 3 …. De 1 a 1000 deve ser a sequência.

for i in range(1001):
    if ((i + 1) % 5) == 0 and ((i + 1) % 3) != 0:
        print(i + 1, end=" ")
print()
