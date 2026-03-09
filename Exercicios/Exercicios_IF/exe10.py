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
