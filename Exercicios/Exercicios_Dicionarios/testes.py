# alunos = {"Nome": "Pedro", "Idade": 20, "Curso": "Engenharia"}
# alunos1 = {"Nome": "Maria", "Idade": 23, "Curso": "técnologias de informação"}
# alunos2 = {"Nome": "João", "Idade": 22, "Curso": "Engenharia"}
# listaAlunos = [alunos, alunos1, alunos2]

# numAlunos = str(len(listaAlunos)+1)
# print(numAlunos)

# novoAluno = "alunos" + numAlunos
# print(novoAluno)
# # novoAluno = {"Nome": "", "Idade": "", "Curso": ""}


dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])
