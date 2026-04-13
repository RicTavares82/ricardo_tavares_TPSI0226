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


def mult(x):
    var = 7
    return x * var


var = 2
print(mult(7))  # saídas: 49


def multi(x):
    var = 2
    return x * var


print(multi(7))  # saídas: 35
