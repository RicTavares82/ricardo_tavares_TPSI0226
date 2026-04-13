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


lista = ["olhos", "zeca", "abrir", "olaria"]

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

conta = 0
while True:
    palavra1 = lista[conta]
    palavra2 = lista[conta + 1]

    for i in range(len(palavra1)):
        conta2 = 0

        if palavra1[i] > palavra2[i]:
            lista[conta], lista[conta + 1] = lista[conta + 1], lista[conta]
            conta += 1
            break
        elif palavra2[i] < palavra1[i]:
            conta += 1
            break
        else:
            if
            for letra2 in palavra2:
                if palavra2[i] > palavra1[i]:
                    lista[conta], lista[conta + 1] = lista[conta + 1], lista[conta]
                else:
                    conta2 += 1


