# Exercício 6: Somar valores de um dicionário
# Dado o seguinte dicionário com os valores de vendas por mês:
# vendas = {'Janeiro': 1000, 'Fevereiro': 1500, 'Março': 1200}
# Calcula o total de vendas do trimestre e imprime o resultado.


vendas = {"Janeiro": 1000, "Fevereiro": 1500, "Março": 1200}
total_vendas = sum(vendas.values())
print(f"O total de vendas do trimestre é: {total_vendas}")
