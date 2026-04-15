# alunos = {"Nome": "Pedro", "Idade": 20, "Curso": "Engenharia"}
# alunos1 = {"Nome": "Maria", "Idade": 23, "Curso": "técnologias de informação"}
# alunos2 = {"Nome": "João", "Idade": 22, "Curso": "Engenharia"}
# listaAlunos = [alunos, alunos1, alunos2]

# numAlunos = str(len(listaAlunos)+1)
# print(numAlunos)

# novoAluno = "alunos" + numAlunos
# print(novoAluno)
# # novoAluno = {"Nome": "", "Idade": "", "Curso": ""}


# dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])


# from math import fabs


# def happy_new_year(wishes=True):
#     print("Três...")
#     print("Duas...")
#     print("Uma...")
#     if not wishes:
#         return

#     print("Feliz Ano Novo!")


# happy_new_year(False)


# def is_year_leap(year):
#     if year % 4 != 0:
#         return False
#     elif year % 100 != 0:
#         return True
#     elif year % 400 != 0:
#         return False
#     else:
#         return True


# def days_in_month(year, month):
#     if year < 1582 or month < 1 or month > 12:
#         return None
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     res = days[month - 1]
#     if month == 2 and is_year_leap(year):
#         res = 29
#     return res


# def day_of_year(year, month, day):
#     days = 0
#     for m in range(1, month):
#         md = days_in_month(year, m)
#     if md == None:
#         return None
#     days += md
#     md = days_in_month(year, month)
#     if day >= 1 and day <= md:
#         return days + day
#     else:
#         return None


# # print(day_of_year(2000, 12, 31))


# from math import e


# def is_prime(num):
#     for i in range(2, int(1 + num**0.5)):
#         if num % i == 0:
#             return False
#         return True


# for i in range(1, 20):
#     if is_prime(i + 1):
#         print(i + 1, end=" ")
#     # print()


# 1 American mile = 1609.344 metres
# 1 American gallon = 3.785411784 litres


# def liters_100km_to_miles_gallon(litres):
#     gallons = litres / 3.785411784
#     miles = 100 * 1000 / 1609.344
#     return miles / gallons


# def miles_gallon_to_liters_100km(miles):
#     km100 = miles * 1609.344 / 1000 / 100
#     litres = 3.785411784
#     return litres / km100


# print(liters_100km_to_miles_gallon(3.9))
# print(liters_100km_to_miles_gallon(7.5))
# print(liters_100km_to_miles_gallon(10.0))
# print(miles_gallon_to_liters_100km(60.3))
# print(miles_gallon_to_liters_100km(31.4))
# print(miles_gallon_to_liters_100km(23.5))


# # Exemplo 1
# def wishes():
#     print("Meus desejos")
#     return "Feliz aniversário!"


# wishes()  # saídas: Meus desejos


# # Exemplo 2
# def wishes():
#     print("Meus desejos")
#     return "Feliz aniversário!"


# print(wishes())

# # saídas: Meus desejos
# # Feliz aniversário!


# def create_list(n):
#     my_list = []
#     for i in range(n):
#         my_list.append(i)
#     return my_list


# print(create_list(5))


# def my_function():
#     global var
#     var = 2
#     print("Eu conheço aquela variável?", var)


# var = 1
# print("antes", var)
# my_function()
# print("depois", var)
# var = 1
# print(var)

# --------


# def my_function(n):
#     print("Eu obtive", n)
#     n += 1
#     print("Eu tenho", n)


# var = 1
# my_function(var)
# print(var)

# ------


# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     my_list_1 = [0, 1]
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)


# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)

# ------


# def my_function(my_list_1):
#     print("Print #1:", my_list_1)
#     print("Print #2:", my_list_2)
#     del my_list_1[0]  # Pay attention to this line.
#     print("Print #3:", my_list_1)
#     print("Print #4:", my_list_2)


# my_list_2 = [2, 3]
# my_function(my_list_2)
# print("Print #5:", my_list_2)


# ------


# def mult(x):
#     var = 7
#     return x * var


# var = 2
# print(mult(7))  # saídas: 49


# def multi(x):
#     var = 2
#     return x * var


# print(multi(7))  # saídas: 35

# ------


# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

# ----


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))

# -----------


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input("Digite o primeiro lado's comprimento: "))
# b = float(input("Entre no segundo lado's comprimento: "))
# c = float(input("Entre no terceiro lado's comprimento: "))

# if is_a_triangle(a, b, c):
#     print("Sim, pode ser um triângulo.")
# else:
#     print("Não, não pode ser um triângulo.")


# -----

# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# def is_a_right_triangle(a, b, c):
#     if not is_a_triangle(a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2 if a > b and a > c:

#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
# print(is_a_right_triangle(5, 3, 4))
# print(is_a_right_triangle(1, 3, 4))

# ----


# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1

#     product = 1
#     for i in range(2, n + 1):
#         product *= i
#     return product


# for n in range(1, 6):  # testando
#     print(n, factorial_function(n))

# ----


# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1

#     elem_1 = elem_2 = 1
#     the_sum = 0
#     for i in range(3, n + 1):
#         the_sum = elem_1 + elem_2
#         elem_1, elem_2 = elem_2, the_sum
#     return the_sum


# for n in range(1, 10):  # testando
#     print(n, "->", fib(n))


# ----


# def factorial_function(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * factorial_function(n - 1)


# for n in range(1, 6):  # testando
#     print(n, factorial_function(n))

# ---

# my_tuple = (1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)

# ---

# my_lista = [1, 10, 100]

# t1 = my_lista + [1000, 10000]
# t2 = my_lista * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_lista)
# print(-10 not in my_lista)

# ----

# var = 123

# t1 = (1,)
# t2 = (2,)
# t3 = (3, var)

# t1, t2, t3 = t2, t3, t1

# print(t1, t2, t3)


# ---

# school_class = {}

# while True:
#     name = input("Digite o nome do aluno: ")
#     if name == "":
#         break
#     score = int(input("Insira a pontuação do aluno (0-10): "))
#     if score not in range(0, 11):
#         break

#     if name in school_class:
#         school_class[name] += [score]
#     else:
#         school_class[name] = [score]

# for name in sorted(school_class.keys()):
#     adding = 0
#     counter = 0
#     for score in school_class[name]:
#         adding += score
#         counter += 1
#     print(name, ":", adding / counter)

# # ----

# tup = (
#     1,
#     2,
#     3,
# )
# my_list = list(tup)
# print(my_list)  # saídas:

# -----

# try:
#     value= int (input('Insira um número natural:'))
#     print('O recíproco de', value, 'é', 1 / value)
# except:0
#     print('Não sei o que fazer.')

# ----
# try:
#     value = int(input('Digite um número natural: '))
#     print('O recíproco de', value, 'é', 1/value)
# except ValueError:
#     print('Eu não sei o que fazer.')
# except ZeroDivisionError:
#     print('A divisão por zero não é permitida em nosso Universo.')

# try:
#     print(10 / 0)
#     break
# except ZeroDivisionError:
#     print("Ocorreu um erro de divisão por zero...")
# except (ValueError, TypeError):
#     print("Ocorreu um erro de valor ou tipo...")
# except:
#     print("Ocorreu um erro desconhecido...")


# school_class = {}

# while True:
#     name = input("Digite o nome do aluno (ou Enter para sair): ")
#     if name == "":
#         break

#     try:
#         score = int(input(f"Insira a pontuação para {name} (0-10): "))
#         if score not in range(0, 11):
#             print("Nota inválida! Use valores de 0 a 10.")
#             continue

#         # Usando LISTA para guardar as várias notas
#         if name in school_class:
#             school_class[name].append(score)
#         else:
#             school_class[name] = [score]

#     except ValueError:
#         print("Por favor, digite um número inteiro.")

# print("\n--- MÉDIAS FINAIS ---")
# # O sorted() organiza os nomes por ordem alfabética
# for name in sorted(school_class.keys()):
#     notas = school_class[name]
#     media = sum(notas) / len(notas)
#     print(f"{name}: {media:.2f}")


