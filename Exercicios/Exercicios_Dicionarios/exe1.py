# Exercício 1: Criar um dicionário simples
# Cria um dicionário chamado alunos que receba nome, idade e curso de cada aluno:
# 1-	Inserir
# 2-	Listar
# O mesmo deve imprimir cada elemento do dicionário no seguinte formato por cada aluno:
# Exemplo:
# nome: Maria
# idade: 20
# curso: Engenharia


# alunos = {"Nome":"","Idade":"","Curso":""}

alunos = {"Nome": "Pedro", "Idade": 20, "Curso": "Engenharia"}
alunos1 = {"Nome": "Maria", "Idade": 23, "Curso": "técnologias de informação"}
alunos2 = {"Nome": "João", "Idade": 22, "Curso": "Engenharia"}
lista = [alunos, alunos1, alunos2]


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

    novainsercao = {"Nome": "", "Idade": "", "Curso": ""}
    alunos[f"{len(alunos)+1}"] = novainsercao
    alunos["Nome"] = input("Nome: ")
    alunos["Idade"] = input("Idade: ")
    alunos["Curso"] = input("Curso: ")
    


while True:
    menu()
    escolha = menu()
    match escolha:
        case "1":
            print("Inserir")
            alunos[f"{len(alunos)+1}"] = "maria"
            alunos["Nome"] = input("Nome: ")
            alunos["Idade"] = input("Idade: ")
            alunos["Curso"] = input("Curso: ")
        case "2":
            print("Listar")
            print(f"Nome: {alunos['Nome']}")
            print(f"Idade: {alunos['Idade']}")
            print(f"Curso: {alunos['Curso']}")
    sair = input("Deseja sair? s/n: ")
    if sair == "s":
        break
