'''
Crie um programa que leia inicialmente duas sequências de N
elementos cada uma. Ao final mostre as duas sequências originais e diga
se as listas são iguais ou não. Duas listas são consideradas iguais quando
possuem os mesmos elementos na mesma ordem
'''

lista=[]
lista2=[]

x=input("Quantos elementos terão a lista:")

cont=0

n=input("Digite um número:")
while cont<int(x):
    lista.append(int(n))
    n=input("Digite um número:")
    cont=cont+1
    
cont=0

y=input("Quantos elementos terão a lista:")

n=input("Digite um número da segunda lista:")
while cont<int(y):
    lista2.append(int(n))
    n=input("Digite um número da segunda lista:")
    cont=cont+1

if x==y:
    if lista==lista2:
        print("lista iguais")
    else:
        print("lista diferentes")
else:
    print("lista Diferentes")



        
