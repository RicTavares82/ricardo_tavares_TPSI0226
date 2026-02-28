# Operadores aritméticos (atribuição)

# soma + , subtração - , divisão / , multiplicação * , mode % (resto da divisão), potência **

total=0
num1=0
num2=0

#input de valores
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#prmeira forma de concatenar string com variáveis
print("A soma é: " + str(num1 + num2))

#segunda forma de concatenar string com variáveis
print("A soma é: ", num1 + num2)

#terceira forma de concatenar string com variáveis
print(f"A soma é: {num1 + num2}")

# quarta forma de concatenar string com variáveis
total = num1 + num2
print("A soma é: ", total)

# o resto dos operadores em baixo
total = num1 - num2
print("A subtração é: ", total)

total = num1 * num2
print("A multiplicação é: ", total)

total = num1 / num2
print("A divisão é: ", total)

total = num1 % num2
print("O resto da divisão é: ", total)

total = num1 ** num2
print("A potência é: ", total)

"----------------------------------------"

#operadores de comparação

# igualdade == , diferente != , maior que > , menor que < , maior ou igual >= , menor ou igual <=

# comparação entre num1 e num2
if num1 == num2:
    print("Os números são iguais")
elif num1 > num2:
    print("num1 é maior que num2")
else:
    print("num1 é menor que num2")

# comparação entre num1 e num2
if num1 != num2:
    print("Os números são diferentes")

"----------------------------------------"

# operadores lógicos

# and , or , not (em c# seria && , || , !)
# and -> todas as condições devem ser verdadeiras
# or -> pelo menos uma condição deve ser verdadeira
# not -> nega a condição

"----------------------------------------"

#operadores de decisão

# if , elif , else

if num1 > 0 and num2 > 0:
    print("Ambos os números são positivos")
elif num1 < 0 and num2 < 0:
    print("Ambos os números são negativos")
else:
    print("Um dos números é positivo e o outro é negativo")

# comparação entre num1 e num2
if num1 > num2:
    print("num1 é maior que num2")
else:
    print("num1 é menor ou igual a num2")

"----------------------------------------"

# exercicio, encontra o maior e o menor
val1 = 2
val2 = 3
val3 = 4

if val1>val2 and val2>val3:
    print("val1 é o maior , val3 é o menor")
elif val1>val3 and val3>val2:
    print("val1 é o maior , val2 é o menor")

# continuar o codigo
elif val2>val1 and val1>val3:
    print("val2 é o maior , val3 é o menor")
elif val2>val3 and val3>val1:
    print("val2 é o maior , val1 é o menor")
elif val3>val1 and val1>val2:
    print("val3 é o maior , val2 é o menor")
else:
    print("val3 é o maior , val1 é o menor")


#outra forma de encontrar o maior e o menor
maior = max(val1, val2, val3)
menor = min(val1, val2, val3)

print(f"{maior} é o maior, {menor} é o menor")