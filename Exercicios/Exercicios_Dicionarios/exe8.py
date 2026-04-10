# Exercício 8: Juntar dois dicionários
# Dado os seguintes dicionários:
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# Cria um novo dicionário que contenha os pares chave-valor dos dois dicionários juntos.

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {}

for chave in d1.keys():
    valor = d1[chave]
    d3[chave] = valor

for chave in d2.keys():
    valor = d2[chave]
    d3[chave] = valor

print(d3)
