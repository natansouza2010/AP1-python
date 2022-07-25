'''
Crie um programa que leia inicialmente duas sequências
de N elementos cada uma e ao final mostre as duas sequências originais e a
sequência resultante da soma de seus elementos. Exemplo:
'''
lista1=[]
lista2=[]
lista3=[]

elementos=int(input('Digite quantos números terão na lista:'))
cont=0

n1=input('Digite um número para a primeira lista:')
while int(cont)<elementos:
    lista1.append(int(n1))
    n1=input('Digite um número para a primeira lista:')
    cont=cont+1
    



cont=0

n2=input('Digite um número para a segunda lista:')
while int(cont)<elementos:
    lista2.append(int(n2))
    n2=input('Digite um número para a segundalista:')
    cont=cont+1
    
print(lista1)
print(lista2)

cont=0
pos=0
while cont<elementos:
    a=lista1[pos]
    b=lista2[pos]
    c= a + b 
    lista3.insert(pos,c)
    pos = pos +1
    cont = cont + 1

print(lista3)        

