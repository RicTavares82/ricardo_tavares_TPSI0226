# Listas em inteiros trocas são mais faceis

# numeros = [1, 5, 8, 3, 9, 23]
# index       0  1  2  3  4  5

# for numero in numeros:
#     print(numero)

# numeros[2] = 6

# for numero in numeros:
#     print(numero)


# Lista de strings

nomes = ["Rui", "Pedro", "João"]
# index D1  0        1       2
# index   012      01234    0123
print()
for nome in nomes:
    print(nome)

# print("ola", "mundo", end="\n\n\n")
# print("ola", "mundo", end="\n\n\n", sep="       ")

print()
nomes[0] = "Tiago"
print("print dentro da index da lista o index da letra escolhida")
print(nomes[0])
print()
print("print dentro da index da lista o index da letra escolhida")
print(nomes[0][2])
print()

# 1- quantas dimensões realmente tem? 2 dimensões
# 2 - como adicionar mais elementos?
# 3 - como remover elementos?
# 4- == compara unicode da string completa
print()
print(nomes)

print()
print("remove - remove o nome declarado")
nomes.remove("Pedro")
print(nomes)

print()
print("pop - remove o index declarado")
nomes.pop(0)
print(nomes)

print()
print("append - adiciona uma nova entrada na ultima posição")
nomes.append("Dario")
print(nomes)

print()
print("count - indica o index do nome declarado = ", nomes.count("Dario"))
print("len - dá o numero de nomes (length) = ", len(nomes))
print("index - dá o index do nome declarado = ", nomes.index("João"))
