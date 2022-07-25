'''
Crie um programa que leia inicialmente uma sequencia de
N números inteiros e mostre ao final 2 listas:

'''
lista=[]
n=int(input('Digite um número:'))
while n!="":
    lista.append(int(n))
    n=input('Digite um número:')
print(lista)
lista2=[]
for z in lista:
    if z not in lista2:
        lista2.append(z)
print(lista2)
