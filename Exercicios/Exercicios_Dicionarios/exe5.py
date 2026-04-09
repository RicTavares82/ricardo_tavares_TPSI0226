# Exercício 5: Contar letras numa palavra
# Pede ao utilizador que introduza uma palavra. Em seguida, cria um dicionário onde cada letra da palavra é uma chave e o seu valor é o número de vezes que essa letra aparece.
# Exemplo de entrada: "banana"
# Resultado esperado: {'b': 1, 'a': 3, 'n': 2}
# # Saída: {'b': 1, 'a': 3, 'n': 2}

palavra = input("Escreva uma palavra: ").lower()

dicionario = {}

for i in range(len(palavra)):
    letra = palavra[i]
    if letra not in dicionario.keys():
        dicionario[letra] = 1
    else:
        dicionario[letra] += 1

print(dicionario)
