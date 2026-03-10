# exercicio 8
notas = [13, 5, 9, 18, 10, 20, 7, 15, 10, 17]

print("As notas são:", end=" ")
for nota in notas:
    print(nota, end=" ")
print()

menor = min(notas)
maior = max(notas)
print("a nota maior:", maior)
print("a nota menor:", menor)

print()
media = sum(notas) / 10
print(f"a média é:", media)

conta = 0
for i in range(10):
    if notas[i] >= media:
        conta = conta + 1
print(f"existem {conta} pessoas com nota igual ou superior á média.")

# mostrar as notas iguais ou superiores á media
for nota in notas:
    if nota >= media:
        print(f" {nota} é uma nota superior ou igual á média: {media}")

print()
# ----------------
# outra forma de apresentar os mesmo resultados
nota1 = 13
nota2 = 5
nota3 = 9
nota4 = 18
nota5 = 10
nota6 = 20
nota7 = 7
nota8 = 15
nota9 = 10
nota10 = 17

media = (
    nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10
) / 10
print(f"a média é:", media)
conta = 0
if nota1 >= media:
    conta = conta + 1
if nota2 >= media:
    conta = conta + 1
if nota3 >= media:
    conta = conta + 1
if nota4 >= media:
    conta = conta + 1
if nota5 >= media:
    conta = conta + 1
if nota6 >= media:
    conta = conta + 1
if nota7 >= media:
    conta = conta + 1
if nota8 >= media:
    conta = conta + 1
if nota9 >= media:
    conta = conta + 1
if nota10 >= media:
    conta = conta + 1
print(f"existem {conta} pessoas com nota igual ou superior á média.")
