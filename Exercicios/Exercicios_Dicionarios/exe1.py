# Exercício 1: Criar um dicionário simples
# Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
# 1-	Inserir
# 2-	Listar
# O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
# Exemplo:
# nome: Maria
# idade: 20
# curso: Engenharia


n1 = {"Nome": "Pedro", "Idade": 20, "Curso": "Engenharia"}
n2 = {"Nome": "Maria", "Idade": 23, "Curso": "técnologias de informação"}
n3 = {"Nome": "João", "Idade": 22, "Curso": "Engenharia"}
alunos = [n1, n2, n3]


def menu():
    while True:
        print("---Escolhas as opções---")
        print("    1 - inserir")
        print("    2 - Listar")
        escolha = input("Escolha uma opção: ")
        if escolha == "1" or escolha == "2":
            break
        else:
            print("Escolha uma opção válida!!!")
    return escolha


def inserir():
    print("Inserir")
    novoAluno = {"Nome": "", "Idade": "", "Curso": ""}
    novoAluno["Nome"] = input("Nome: ")
    novoAluno["Idade"] = input("Idade: ")
    novoAluno["Curso"] = input("Curso: ")
    alunos.append(novoAluno)


def listar():
    print("Listar")
    for aluno in alunos:
        print(f"Nome: {aluno['Nome']}")
        print(f"Idade: {aluno['Idade']}")
        print(f"Curso: {aluno['Curso']}")


while True:
    escolha = menu()
    match escolha:
        case "1":
            inserir()
        case "2":
            listar()
    sair = input("\nDeseja sair? s/n: ")
    if sair == "s":
        break
