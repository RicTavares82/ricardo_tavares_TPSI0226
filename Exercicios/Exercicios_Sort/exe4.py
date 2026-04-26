# 4. Ordenar uma lista de palavras pela quantidade de letras minúsculas
#  Objetivo: Contar quantas letras minúsculas há em cada palavra e ordená-las do menor para o maior número.
# Exemplo:
# ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]
# Resultado esperado:
# ["CÓDIGO", "intELIGENTE", "PYthon", "dados", "banana"]
# Como fazer:
# •	Conta, para cada palavra, quantos caracteres estão entre 'a' e 'z'.
# •	Usa esse número como "peso" para ordenar.
# •	Palavras com mais minúsculas vão para o fim da lista.


def contar_minusculas(palavra):
    contador = 0
    for letra in palavra:
        # Verificar se a letra está entre 'a' e 'z' (ASCII)
        if "a" <= letra <= "z":
            contador += 1
    return contador


lista = ["PYthon", "banana", "CÓDIGO", "intELIGENTE", "dados"]

for volta in range(len(lista)):
    for i in range(0, len(lista) - 1):
        if contar_minusculas(lista[i]) > contar_minusculas(lista[i + 1]):
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print("ordenado:", lista)
