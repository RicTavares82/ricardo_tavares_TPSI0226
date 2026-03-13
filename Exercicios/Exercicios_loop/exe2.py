# Exercício 2: Ler 10 números, e determinar se o número par e número impar.


print("Insira 10 numeros")
print()
for i in range(10):
    escolhidos = int(input(f"Insira o {i+1}º numero: "))
    if (escolhidos % 2) == 0:
        print(f"o numero {escolhidos} é par")
    else:
        print(f"o numero {escolhidos} é impar")
