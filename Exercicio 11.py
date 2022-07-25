'''
Faça uma função que receba uma lista de números armazenados de
forma crescente (faça a consistência) , e dois valores ( limite inferior e
limite superior), e exiba a sublista cujos elementos são maiores ou iguais
ao limite inferior e menores ou iguais ao limite superior. Exemplo:
'''

lista=[]
ult=-14568
n=input("Digite um número em ordem crescente e aperte enter pra finalizar a lista:")
while n!="":
    if int(ult)<int(n):
        lista.append(int(n))
        ult=n
    else:
        print("Digite um número em ordem crescente")
        
    n=input("Digite um número em ordem crescente e aperte enter pra finalizar a lista:")
print(lista)


inf=input("Digite o limite inferior:")
sup=input("Digite o limite superior:")
lista2=[]

for i in lista:
    if i>=int(inf)and i<=int(sup):
        lista2.append(i)

print(lista2)
    
    




    
