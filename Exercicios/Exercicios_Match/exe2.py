# Exercício 2
nota = int(input("Digite a nota do teste (0-100): "))

if nota < 50:
    print("Insuficiente")
elif nota >= 50 and nota < 70:
    print("Suficiente")
elif nota >= 70 and nota < 90:
    print("Bom")
elif nota >= 90 and nota < 101:
    print("Excelente")
else:
    print("numero de nota errado")
