'''
Crie um programa que leia inicialmente duas sequências de N
elementos cada uma. Ao final mostre as duas sequências originais e diga
se as listas possuem os mesmos elementos ou não. Neste caso, as duas
listas devem possuir os mesmos elementos em qualquer ordem.
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

y =input("Quantos elementos terão a segunda lista:")

n=input("Digite um número da segunda lista:")
while cont<int(y):
    lista2.append(int(n))
    n=input("Digite um número da segunda lista:")
    cont=cont+1
    
#Não conseguir realizar sem utilizar função
print(lista)
print(lista2)

a=lista
b=lista2

a.sort()
b.sort()

if x==y and a==b:
    print("São iguais")
else:
    print("São diferentes")



'''

print(lista)
print(lista2)

if x==y:
    posição=0
    iguais=0
    for i in lista:
        if i==int(lista2[posição]):
            posição=posição+1
            iguais=iguais+1       
        else:
            print("Lista Desiguais")
            
    if len(lista)==iguais:
        print("lista iguais")
        
    else:
        print("lista desiguais")


'''
