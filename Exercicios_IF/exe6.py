# Exercício 6

10% para compras até 200,00€.
15% para compras entre 200,01€ e 500,00€.
20% para compras acima de 500,00€.

nome = input("Cliente: ")
compra = int(input("Valor da Compra: "))
# valorDesconto = compra * 0.10

if compra < 200:
    print(f"Nome: {nome}")
    print(f"Compra: {compra}€")
    print(f"Desconto: {compra * 0.1}€")
    print(f"Total a pagar: {compra - compra * 0.1}€")
elif compra > 500:
    print(f"Nome: {nome}")
    print(f"Compra: {compra}€")
    print(f"Desconto: {compra * 0.2}€")
    print(f"Total a pagar: {compra - (compra * 0.2)}€")
else:
    print(f"Nome: {nome}")
    print(f"Compra: {compra}€")
    print(f"Desconto: {compra * 0.15}€")
    print(f"Total a pagar: {compra - (compra * 0.15)}€")