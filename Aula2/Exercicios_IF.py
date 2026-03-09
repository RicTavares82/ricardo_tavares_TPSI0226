# exercicio 1

# inSegundos = int(input("Digite o número em segundos: "))

# horas = inSegundos // 3600
# restoSegundos = inSegundos % 3600
# minutos = restoSegundos // 60
# segundos = restoSegundos % 60

# print(f"{horas} horas, {minutos} minutos e {segundos} segundos")

# -------------------------

# Exercício 2

# num1 = 5
# num2 = 2
# num3 = 8

# # maior
# if num1 > num2 and num1 > num3:
#     print(f"O maior número é: {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f"O maior número é: {num2}")
# else:
#     print(f"O maior número é: {num3}")
# # Menor
# if num1 < num2 and num1 < num3:
#     print(f"O menor número é: {num1}")
# elif num2 < num1 and num2 < num3:
#     print(f"O menor número é: {num2}")
# else:
#     print(f"O menor número é: {num3}")

# print()

# # Outra forma de mostrar o maior e menor número usando a função max() e min()
# maior = max(num1, num2, num3)
# menor = min(num1, num2, num3)
# print(f"O maior número é: {maior}")
# print(f"O menor número é: {menor}")


# --------------------------

# Exercício 3

# num1 = input("Digite o primeiro número: ")
# num2 = input("Digite o segundo número: ")

# if num1 > num2:
#     print(f"Decrescente: {num1}, {num2}")
# elif num1 < num2:
#     print(f"Crescente: {num1}, {num2}")
# else:
#     print("Os números são iguais")


# --------------------------

# Exercício 4

# saldo = 1000

# print(f"saldo inicial: {saldo}€")
# cheque = int(input("Digite o valor do cheque: "))
# if saldo < cheque:
#     print(f"Não existe saldo suficiente na Conta.")
# else:
#     print(f"Cheque descontado, ficou com {saldo-cheque}€ na conta.")


# -------------------------------

# Exercicio 5

# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# num3 = int(input("Digite o terceiro número: "))

# num1 = 4
# num2 = 9
# num3 = 2

# # Lógica para colocar em ordem crescente usando IF
# # Comparar o 1º com o 2º
# if num1 > num2:

#     aux = num1  # Guarda o 4 na reserva
#     num1 = num2  # num1 recebe 9
#     num2 = aux  # num2 recebe o 4 que estava guardado

#     # forma mais simples e rápida
#     # num1, num2 = num2, num1

# # Comparar o 1º com o 3º
# if num1 > num3:

#     aux = num1  # Guarda o 4 na reserva
#     num1 = num3  # num1 recebe 2
#     num3 = aux  # num3 recebe o 4 que estava guardado

#     # forma mais simples e rápida
#     # num1, num3 = num3, num1

# # Comparar o 2º com o 3º
# if num2 > num3:

#     aux = num2  # Guarda o 9 na reserva
#     num2 = num3  # num2 vira 2
#     num3 = aux  # num3 busca o 9 que estava guardado

#     # forma mais simples e rápida
#     # num2, num3 = num3, num2

# if num1 == num2 or num1 == num3 or num2 == num3:
#     print("Existem números iguais, não é possível ordenar.")
# else:
#     print("Crescente:", num1, num2, num3)
#     print("Decrescente:", num3, num2, num1)


# Outra forma de mostrar o mesmo resultado usando um metodo dentro de uma lista

# # cria a lista com os números já declarados
# numeros = [num1, num2, num3]

# # OU Criando uma lista já com os valores
# # numeros = [4, 9, 2]

# # Ordem Crescente
# numeros.sort()
# print("Crescente:", numeros)
# # Ordem Decrescente
# numeros.sort(reverse=True)  # usado um parametro para inverter o .sort
# print("Decrescente:", numeros)


# -------------------------------

# Exercício 6

# 10% para compras até 200,00€.
# 15% para compras entre 200,01€ e 500,00€.
# 20% para compras acima de 500,00€.

# nome = input("Cliente: ")
# compra = int(input("Valor da Compra: "))
# # valorDesconto = compra * 0.10

# if compra < 200:
#     print(f"Nome: {nome}")
#     print(f"Compra: {compra}€")
#     print(f"Desconto: {compra * 0.1}€")
#     print(f"Total a pagar: {compra - compra * 0.1}€")
# elif compra > 500:
#     print(f"Nome: {nome}")
#     print(f"Compra: {compra}€")
#     print(f"Desconto: {compra * 0.2}€")
#     print(f"Total a pagar: {compra - (compra * 0.2)}€")
# else:
#     print(f"Nome: {nome}")
#     print(f"Compra: {compra}€")
#     print(f"Desconto: {compra * 0.15}€")
#     print(f"Total a pagar: {compra - (compra * 0.15)}€")


# ---------------------------


# Exercicio 7

# # nota1 = float(input("Nota1: "))
# # nota2 = float(input("Nota2: "))
# # nota3 = float(input("Nota3: "))
# nota1 = 7
# nota2 = 6
# nota3 = 9

# media = (nota1 * 20 + nota2 * 30 + nota3 * 50) / 100

# print(f"Média final: {media}")
# if media >= 6:
#     print("APROVADO")
# else:
#     print("REPROVADO")


# ---------------------


# exercicio 8
# notas = [13, 5, 9, 18, 10, 20, 7, 15, 10, 17]

# print("As notas são:", end=" ")
# for nota in notas:
#     print(nota, end=" ")
# print()

# menor = min(notas)
# maior = max(notas)
# print("a nota maior:", maior)
# print("a nota menor:", menor)

# media = sum(notas) / 10
# print(f"a média é:", media)

# conta = 0
# for i in range(10):
#     if notas[i] >= media:
#         conta = conta + 1
# print(f"existem {conta} pessoas com nota igual ou superior á média.")

# # mostrar as notas iguais ou superiores á media
# for nota in notas:
#     if nota >= media:
#         print(f"Esta nota é superior ou igual á média: {nota}")

# # outra forma de apresentar os mesmo resultados
# nota1 = 13
# nota2 = 5
# nota3 = 9
# nota4 = 18
# nota5 = 10
# nota6 = 20
# nota7 = 7
# nota8 = 15
# nota9 = 10
# nota10 = 17

# media = (
#     nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10
# ) / 10
# print(f"a média é:", media)
# conta = 0
# if nota1 >= media:
#     conta = conta + 1
# if nota2 >= media:
#     conta = conta + 1
# if nota3 >= media:
#     conta = conta + 1
# if nota4 >= media:
#     conta = conta + 1
# if nota5 >= media:
#     conta = conta + 1
# if nota6 >= media:
#     conta = conta + 1
# if nota7 >= media:
#     conta = conta + 1
# if nota8 >= media:
#     conta = conta + 1
# if nota9 >= media:
#     conta = conta + 1
# if nota10 >= media:
#     conta = conta + 1
# print(f"existem {conta} pessoas com nota igual ou superior á média.")


# ------------------------

# Exercicio 9

# while True:
#     escolha = input("Escolha um numero inteiro entre 1 e 12:")
#     match escolha:
#         case "1":
#             print("1 é janeiro.")
#         case "2":
#             print("2 é fevereiro.")
#         case "3":
#             print("3 é março.")
#         case "4":
#             print("4 é abril.")
#         case "5":
#             print("5 é maio.")
#         case "6":
#             print("6 é junho.")
#         case "7":
#             print("7 é julho.")
#         case "8":
#             print("8 é agosto.")
#         case "9":
#             print("9 é setembro.")
#         case "10":
#             print("10 é outubro.")
#         case "11":
#             print("11 é novembro.")
#         case "12":
#             print("12 é dezembro.")
#         case _:
#             print("Número inválido, escolha um número entre 1 e 12.")


# ------------------------

# exercicio 10

# numeros = [2, 3, 5, 6, 8, 9, 10, 12, 14, 15]
# contaPar = 0
# contaImp = 0

# for i in range(10):
#     if (numeros[i] % 2) == 0:
#         # print("é par o numero ", numeros[i])
#         contaPar = contaPar + 1
#     if (numeros[i] % 2) != 0:
#         # print("é impar o numero ", numeros[i])
#         contaImp = contaImp + 1

# print("Pares", contaPar)
# print("Impares", contaImp)
