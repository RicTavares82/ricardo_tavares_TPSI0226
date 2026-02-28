'''
comentar várias linhas
'''

"comentário de uma linha"
# comentário de uma linha

"outup para consola"
print ("Hello World from Python")

"INT"
tel=93666556
print (type (tel))
print (tel)
#Variaveis dinamicas alteram de tipo automaticamente
tel="93666556"
print (type (tel))
print (tel)
#exemplo entre um int e uma string
tel=9 #Decimal é um 9
#Variaveis dinamicas alteram de tipo automaticamente
tel="9" #Decimal vale 57 na table ASCII

#float
med=2.3
print (type (med))
print (med)

#string
nom="João"
print (type (nom))
print (nom)

#boolean
verdadeiro=True 
print (type (verdadeiro))
print (verdadeiro) 

#listas []
lista=[1,5,3,4,9]
print (type (lista))
print (lista)
#listas também aceitam qualquer tipo de dados
lista2=[1,"João",2.3,True]
print (type (lista2))
print (lista2)

#tuplas () -> ao contrário das listas são imutáveis, ou seja, não podem ser alteradas depois de criadas
tupla=(1,5,3,4,9)
print (type (tupla))
print (tupla)
#tuplas também aceitam qualquer tipo de dados
