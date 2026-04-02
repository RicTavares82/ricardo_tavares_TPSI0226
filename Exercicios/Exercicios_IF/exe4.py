# Exercício 4

saldo = 1000

print(f"saldo inicial: {saldo}€")
cheque = int(input("Digite o valor do cheque: "))
if saldo < cheque:
    print("Não existe saldo suficiente na Conta.")
else:
    print(f"Cheque descontado, ficou com {saldo-cheque}€ na conta.")
