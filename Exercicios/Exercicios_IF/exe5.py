# Exercicio 5

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))

num1 = 4
num2 = 9
num3 = 2

# Lógica para colocar em ordem crescente usando IF
# Comparar o 1º com o 2º
if num1 > num2:

    aux = num1  # Guarda o 4 na reserva
    num1 = num2  # num1 recebe 9
    num2 = aux  # num2 recebe o 4 que estava guardado

    # forma mais simples e rápida
    # num1, num2 = num2, num1

# Comparar o 1º com o 3º
if num1 > num3:

    aux = num1  # Guarda o 4 na reserva
    num1 = num3  # num1 recebe 2
    num3 = aux  # num3 recebe o 4 que estava guardado

    # forma mais simples e rápida
    # num1, num3 = num3, num1

# Comparar o 2º com o 3º
if num2 > num3:

    aux = num2  # Guarda o 9 na reserva
    num2 = num3  # num2 vira 2
    num3 = aux  # num3 busca o 9 que estava guardado

    # forma mais simples e rápida
    # num2, num3 = num3, num2

if num1 == num2 or num1 == num3 or num2 == num3:
    print("Existem números iguais, não é possível ordenar.")
else:
    print("Crescente:", num1, num2, num3)
    print("Decrescente:", num3, num2, num1)


Outra forma de mostrar o mesmo resultado usando um metodo dentro de uma lista

# cria a lista com os números já declarados
numeros = [num1, num2, num3]

# OU Criando uma lista já com os valores
# numeros = [4, 9, 2]

# Ordem Crescente
numeros.sort()
print("Crescente:", numeros)
# Ordem Decrescente
numeros.sort(reverse=True)  # usado um parametro para inverter o .sort
print("Decrescente:", numeros)
