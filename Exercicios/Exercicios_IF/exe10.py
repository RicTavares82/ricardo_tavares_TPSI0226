# exercicio 10

numeros = [2, 3, 5, 6, 8, 9, 10, 12, 14, 15]
contaPar = 0
contaImp = 0

for i in range(10):
    if (numeros[i] % 2) == 0:
        # print("é par o numero ", numeros[i])
        contaPar = contaPar + 1
    if (numeros[i] % 2) != 0:
        # print("é impar o numero ", numeros[i])
        contaImp = contaImp + 1

print("Pares", contaPar)
print("Impares", contaImp)

print()
# ---------------------
# outra forma de apresentar o mesmo resultado

num1 = 2
num2 = 3
num3 = 5
num4 = 6
num5 = 8
num6 = 9
num7 = 10
num8 = 12
num9 = 14
num10 = 15

contaPar = 0
contaImp = 0

if (num1 % 2) == 0:
    print("é par o numero ", num1)
    contaPar += 1
else:
    print("é Impar o numero ", num1)
    contaImp += 1
if (num2 % 2) == 0:
    print("é par o numero ", num2)
    contaPar += 1
else:
    print("é Impar o numero ", num2)
    contaImp += 1
if (num3 % 2) == 0:
    print("é par o numero ", num3)
    contaPar += 1
else:
    print("é Impar o numero ", num3)
    contaImp += 1
if (num4 % 2) == 0:
    print("é par o numero ", num4)
    contaPar += 1
else:
    print("é Impar o numero ", num4)
    contaImp += 1
if (num5 % 2) == 0:
    print("é par o numero ", num5)
    contaPar += 1
else:
    print("é Impar o numero ", num5)
    contaImp += 1
if (num6 % 2) == 0:
    print("é par o numero ", num6)
    contaPar += 1
else:
    print("é Impar o numero ", num6)
    contaImp += 1
if (num7 % 2) == 0:
    print("é par o numero ", num7)
    contaPar += 1
else:
    print("é Impar o numero ", num7)
    contaImp += 1
if (num8 % 2) == 0:
    print("é par o numero ", num8)
    contaPar += 1
else:
    print("é Impar o numero ", num8)
    contaImp += 1
if (num9 % 2) == 0:
    print("é par o numero ", num9)
    contaPar += 1
else:
    print("é Impar o numero ", num9)
    contaImp += 1
if (num10 % 2) == 0:
    print("é par o numero ", num10)
    contaPar += 1
else:
    print("é Impar o numero ", num10)
    contaImp += 1

print()
print("Pares: ", contaPar)
print("Impares: ", contaImp)
