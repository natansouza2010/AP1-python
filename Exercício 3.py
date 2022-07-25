
numeros=[]
par=0
impar=1
n=int(input('Digite um número:'))
while n!="":
    numeros.append(int(n))
    n=input('Digite um número:')
for z in numeros:
    if z%2==0:
        par=z+par
    if z%2==1:
        impar=z*impar
print("A sequencia dos números digitados:",numeros,"Soma dos pares é = ",par," Multiplicação dos impares =",impar)

