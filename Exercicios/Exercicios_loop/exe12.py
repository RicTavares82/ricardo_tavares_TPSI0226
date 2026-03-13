# Exercício 12: Elabore um programa que leia quantos números quer que se efetue a soma, subtrações, divisões, multiplicações e no fim por meio de um acumulador diga quantas operações foram efetuadas. Exemplo introduzindo o número 60 o programa deve apresentar 60 a somar, dividir multiplicar e subtrair por todos os números menores que ele.

num = int(input("Escreva um numero: "))
cont = 0
som = 0
print("valores a somar: ")
for i in range(num - 1, 0, -1):
    cont += 1
    ope = num + i
    som += ope
    print(f"{num} + {i} = {ope}")
print(f"O total da soma dos valores é {som}")
som = 0
cont = 0
print("valores a subtrair: ")
for i in range(num - 1, 0, -1):
    cont += 1
    ope = num - i
    som += ope
    print(f"{num} - {i} = {ope}")
print(f"O total da soma dos valores é {som}")
som = 0
cont = 0
print("valores a multiplicar: ")
for i in range(num - 1, 0, -1):
    cont += 1
    ope = num * i
    som += ope
    print(f"{num} * {i} = {ope}")
print(f"O total da soma dos valores é {som}")
som = 0
cont = 0
print("valores a dividir: ")
for i in range(num - 1, 0, -1):
    cont += 1
    ope = num / i
    som += ope
    print(f"{num} * {i} = {ope:.2}")
print(f"O total da soma dos valores é {som}")
