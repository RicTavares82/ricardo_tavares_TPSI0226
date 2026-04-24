# 5. Agrupar palavras pela letra inicial e ordenar cada grupo por ordem alfabética (A → Z)
# Objetivo: Reorganizar as palavras em grupos que comecem com a mesma letra, e depois ordenar cada grupo manualmente.
# Exemplo:
# ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
# Resultado esperado:
# {
#   'b': ['banana', 'bola'],
#   'a': ['abacaxi', 'arroz'],
#   'u': ['urso', 'uva']
# }
# Como fazer:
# •	Cria um dicionário onde cada chave é uma letra inicial.
# •	Coloca cada palavra no grupo correspondente.
# •	Ordena cada grupo individualmente usando comparação com ord().
# Este é o exercício mais completo: vais precisar de organizar, comparar e ordenar em dois níveis.

lista = ["banana", "bola", "abacaxi", "arroz", "uva", "urso"]
dic = {}

for i in range(len(lista)):
    primeiraLetra = lista[i][0]

    if primeiraLetra not in dic.keys():
        dic[primeiraLetra] = [lista[i]]
    else:
        dic[primeiraLetra].append(lista[i])

# print(dic)
for cada in dic.keys():
    print(cada, dic)
