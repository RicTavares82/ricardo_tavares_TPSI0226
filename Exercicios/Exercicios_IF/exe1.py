# exercicio 1

inSegundos = int(input("Digite o número em segundos: "))

horas = inSegundos // 3600
restoSegundos = inSegundos % 3600
minutos = restoSegundos // 60
segundos = restoSegundos % 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos")
