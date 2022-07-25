'''
Crie um programa que leia inicialmente uma sequência de N elementos
inteiros positivos fornecidos pelo usuário e substitua seus elementos de
valor ímpar por -1 e os pares por +1. Ao final imprima a sequência
original e a sequência alterada.
'''
lista=[]
listaoriginal=[]
x=input("Quantos elementos terão a lista:")

cont=0

n=input("Digite um número:")
while cont<int(x):
    listaoriginal.append(int(n))
    lista.append(int(n))
    n=input("Digite um número:")
    cont=cont+1

    
posição=0
for i in lista:
    if i%2==0:
        lista[posição]=1
    if i%2==1:
        lista[posição]=-1
    posição=posição+1
    
print(listaoriginal)
print(lista)

    
