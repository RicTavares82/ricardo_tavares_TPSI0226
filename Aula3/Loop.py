# loops FOR // While

# lista
nomes = ["João", "Pedro", "Antonio"]

for nome in nomes:
    print(nome)

# função range

print()
for i in range(3):
    print(i)

print()
for i in range(3):
    print(nomes[i])

# len
print()
for i in range(len(nomes)):
    print(nomes[i])


# while  <--- controlado por uma expressao ex: Val1 < Val2
print()
# tamanho da lista 3
i = 0
while i < len(nomes):  # começa em 0 e acaba em 2
    i += 1

print()
# outra forma
while i <= 3:  # começa em 0 e acaba em 2
    i += 1

print()
# outra forma
ifinal = len(nomes)
while i <= ifinal:  # começa em 0 e acaba em 2
    i += 1


# ------------------

# flag True
print()
flag = True
while flag:
    print("1- bom dia")
    print("1- boa tarde")
    print("3- Sair")
    opc = input("intrud a opc")
    match opc:
        case "1":
            print("bom dia")
        case "2":
            print("boa tarde")
        case "3":
            print("sair")
            flag = False
        case _:
            print("opd errada")
