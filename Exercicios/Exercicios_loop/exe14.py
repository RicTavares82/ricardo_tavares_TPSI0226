# Exercício 14: Altere o programa anterior para que mostre todas as tabuadas de 1 a 100. (ciclos for).

sum = 0
numChoice = 0

for i in range(101):
    print("Proxima tabuada é {i}")
    for y in range(10):
        sum = i * (y + 1)
        print(f"{i} X {y+1} = {sum}")
