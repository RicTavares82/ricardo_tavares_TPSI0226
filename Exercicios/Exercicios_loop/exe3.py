# Exercício 3: Ler a nota de 10 alunos, calcular a media e mostrar essa média.
import random


def newNum():
    return random.uniform(1, 20)


num = 0
for i in range(10):
    num = newNum() + num
    print(newNum)

print(f"a média das notas é: {(num / 10):.2f}")
