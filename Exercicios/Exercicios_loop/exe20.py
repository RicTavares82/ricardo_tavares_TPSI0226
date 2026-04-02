# Teste Final: Elabore um programa que leia um valor de entrada e mostre para cada valor até ao 1 (se é número Primo, Quantos divisores e números perfeitos) o Programa deve validar entradas entre 1 e 30.000, e parar de 10 em 10 valores com instrução para parar ou continuar. No mesmo programa use um menu e Elabore uma calculadora simples (+,-,*,/) com a função extra tabuada. Validar entradas de 1 a 1000 (nota a tabuada deve apresentar todas as multiplicações de 1 ate ao máximo introduzido) deve parar de 20 em 20 valores.


while True:
    print("1 - Ver se um numero é primo, perfeito e numero de divisores")
    print("2 - Calculadora")
    print("3 - Função Extra (Tabuada)")
    escolha = input("\nEscolha uma opção: ")
    match escolha:
        case "1":
            contciclos = 0

            print("\nVer se um numero é primo, perfeito e quantos divisores tem")
            while True:
                num = int(input("\nEscreva um numero: "))
                if num > 0 and num < 30001:
                    break
                else:
                    print("\nEscreva um numero válido entre 1 e 30000: ")

            for i in range(num, 0, -1):
                somaj = 0
                somaj2 = 0
                contDivisores = 0
                # conti = ""

                if contciclos == 10:
                    conti = input("\nQuer continuar a ver a lista? s/n: \n").lower()
                    if conti == "n":
                        break
                    else:
                        contciclos = 0

                for j in range(i, 0, -1):
                    if (i % j) == 0:
                        contDivisores += 1
                        # se numero perfeito acumula
                        if j != i:
                            somaj += j

                # Validar divisores
                if contDivisores == 2:
                    sePrimo = "é primo"
                else:
                    sePrimo = "não é primo"

                # validar os numeros Perfeito
                if somaj == i and i != 0:
                    sePerfeito = "perfeito"
                else:
                    sePerfeito = "imperfeito"

                print(
                    f"O {i}, {sePrimo}, tem {contDivisores} divisores e é um numero {sePerfeito}"
                )
                contciclos += 1

            print("\nChegou ao fim da lista, ADEUS!!!\n")
        case "2":
            while True:
                print("\nCalculadora")
                print("1 - somar")
                print("2 - subtrair")
                print("3 - multiplicar")
                print("4 - dividir")
                escolha = input("\nEscolha uma opção: ")
                match escolha:
                    case "1":
                        print("somar")
                        num1 = int(input("\nEscolha o primeiro numero: "))
                        num2 = int(input("\nEscolha o segundo numero: "))
                        print(f"{num1} + {num2} = {num1 + num2}")

                    case "2":
                        print("subtrair")
                        num1 = int(input("\nEscolha o primeiro numero: "))
                        num2 = int(input("\nEscolha o segundo numero: "))
                        print(f"{num1} - {num2} = {num1 - num2}")

                    case "3":
                        print("multiplicar")
                        num1 = int(input("\nEscolha o primeiro numero: "))
                        num2 = int(input("\nEscolha o segundo numero: "))
                        print(f"{num1} * {num2} = {num1 * num2}")

                    case "4":
                        print("dividir")
                        num1 = int(input("\nEscolha o primeiro numero: "))
                        num2 = int(input("\nEscolha o segundo numero: "))
                        if num2 == 0:
                            print("não pode escolher 0 para o divisor")
                            num2 = int(input("\nEscolha o segundo numero: "))

                        print(f"{num1} / {num2} = {(num1 / num2):2}")
                    case _:
                        print("Escolha uma opção válida entre 1 e 4")

                conti = input("\nQuer continuar? s/n: \n").lower()
                if conti == "n":
                    break
            print("\nADEUS!!!\n")
        case "3":
            contciclos = 0
            sum = 0
            numChoice = 0
            print("Tabuada")
            while True:
                numChoice = int(input("Numero (entre 1 e 1000): "))
                if numChoice > 0 and numChoice < 1001:
                    break
                else:
                    print("\nEscreva um numero válido entre 1 e 1000: ")
            for y in range(1, numChoice + 1):

                if contciclos == 20:
                    conti = input("\nQuer continuar a ver a lista? s/n: ").lower()
                    contciclos = 0
                    if conti == "n":
                        print("\nChegou ao fim da lista, ADEUS!!!\n")
                        break
                sum = numChoice * y
                print(f"{numChoice} X {y} = {sum}")
                contciclos += 1

        case _:
            print("\nNúmero inválido, escolha a opção entre 1 e 3.\n ")
