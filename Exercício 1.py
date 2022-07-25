lista=[]
soma=0
n=int(input('Digite um número:'))
while n!="":
    lista.append(int(n))
    n=input('Digite um número:')
for z in lista:
    soma= soma+z
media=soma/len(lista)
print('A sequencia de números é:{} e a sua média é :{}'.format(lista,media))
