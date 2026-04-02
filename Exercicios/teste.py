contciclos = 0
numChoice = 40
conti = ""
for y in range(1, numChoice + 1):
    contciclos += 1
    if contciclos == 21:
        conti = input("\nQuer continuar a ver a lista? s/n: ").lower()
        contciclos = 0
        if conti == "s":
            print("\nVamos continuar\n")
        elif conti == "n":
            print("\nChegou ao fim da lista, ADEUS!!!\n")
            break
    sum = numChoice * y
    print(f"{numChoice} X {y} = {sum}")
