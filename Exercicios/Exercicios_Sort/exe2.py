# 2. Ordenar uma lista de palavras por ordem alfabética inversa (Z → A), ignorando maiúsculas/minúsculas
# Objetivo: Reordenar da última letra do alfabeto para a primeira, sem distinguir maiúsculas de minúsculas.
# Exemplo:
# ["Python", "inteligência", "Aprender", "dados", "Rede"]
# Resultado esperado:
# ["Rede", "Python", "inteligência", "dados", "Aprender"]
# Como fazer:
# •	Compara os caracteres em minúsculas ("A" e "a" passam a ser tratados como iguais).
# •	Ordena da última letra para a primeira.
# •	A lógica da comparação será invertida: em vez de colocar as menores primeiro, colocas as maiores.


lista = ["Python", "inteligência", "Aprender", "dados", "Rede"]

flag = True
while flag:
    flag = False
    for i in range(len(lista) - 1, 0, -1):
        print(i)
        if lista[i].lower() > lista[i - 1].lower():
            print(i)
            lista[i], lista[i - 1] = lista[i - 1], lista[i]
            flag = True
print(lista)
