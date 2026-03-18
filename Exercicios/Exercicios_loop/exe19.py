# Exercícios 19:Escreva um programa que mostre os primeiros 60 números da serie bonatchi.
# 1, 1, 2, 3, 5, 8, 13, 21.
# Como se constrói.
# 1+1=2
#     1+2=3
#         2+3=5

resultado_anterior = 0
atual = 1
# soma = 0
for i in range(60):

    if i > 1:
        resultado_anterior = atual + resultado_anterior
        atual = resultado_anterior
        print(f"{resultado_anterior}")
        print
