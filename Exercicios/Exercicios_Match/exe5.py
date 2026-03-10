# Exercício 5

mensagem = input("Escreva a sua mensagem: ").lower()
# .lower() para passar a maiúsculas

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

print()
# ----------------
# outra forma de apresentar o resultado
text = input("Escreva a sua mensagem: ").lower()

match text:
    case _ if "olá" in text or "bom dia" in text or "oi" in text:
        print("Saudação")
    case _ if "?" in text:
        print("Pergunta")
    case _ if "tchau" in text or "adeus" in text:
        print("Despedida")
    case _:
        print("Mensagem genérica")
