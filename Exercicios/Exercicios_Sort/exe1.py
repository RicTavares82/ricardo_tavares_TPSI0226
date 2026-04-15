# 1.	Ordenar uma lista de palavras por ordem alfabética (A → Z)
# Objetivo: Reordenar as palavras, comparando carácter por carácter, como se estivesses a fazer o papel da função sorted().
# Exemplo:
# ["banana", "uva", "abacaxi", "laranja"]
# Resultado esperado:
# ["abacaxi", "banana", "laranja", "uva"]
# Como fazer:
# •	Compara as palavras duas a duas.
# •	Usa o código ASCII de cada letra para decidir qual vem antes.
# •	Se duas palavras começarem pela mesma letra, continua a comparação na letra seguinte.
# •	Se uma palavra for prefixo da outra (como "casa" e "casamento"), a mais curta deve vir primeiro.


listaLetras = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

listaASCII = [
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    121,
    122,
]
# lista = ["banana", "uva", "abacaxi", "laranja"]
# ["abacaxi", "banana", "laranja", "uva"]

lista = ["banana", "laranja", "casamento", "casa"]

flag = True
print(lista)

while flag:
    flag = False
    print(lista)
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            print(lista)
            flag = True
print("Lista ordenada:", lista)
