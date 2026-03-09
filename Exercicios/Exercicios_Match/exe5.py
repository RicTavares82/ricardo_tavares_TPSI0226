# Exercício 5

mensagem = input(
    "Escreva a sua mensagem: "
).lower()  # .lower() para passar a maiúsculas

# Saudação (Comparação exata)
if mensagem == "olá" or mensagem == "bom dia":
    print("Saudação")

# Pergunta (Verificar o último carater da mensagem)
elif mensagem.endswith("?"):
    print("Pergunta")

# Despedida (Pesquisa de palavra dentro do texto)
elif "tchau" in mensagem or "adeus" in mensagem:
    print("Despedida")

# Caso contrário
else:
    print("Mensagem genérica")
