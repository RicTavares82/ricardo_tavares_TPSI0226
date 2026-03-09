# Exercício 2

num1 = 5
num2 = 2
num3 = 8

# maior
if num1 > num2 and num1 > num3:
    print(f"O maior número é: {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior número é: {num2}")
else:
    print(f"O maior número é: {num3}")
# Menor
if num1 < num2 and num1 < num3:
    print(f"O menor número é: {num1}")
elif num2 < num1 and num2 < num3:
    print(f"O menor número é: {num2}")
else:
    print(f"O menor número é: {num3}")

print()

# Outra forma de mostrar o maior e menor número usando a função max() e min()
maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
