lista=[]
listaaocubo=[]
n=input('Digite um número:')
while n!='':
    aocubo=int(n)*int(n)*int(n)
    lista.append(int(n))
    listaaocubo.append(int(aocubo))
    n=input('Digite um número:')
print(lista)
print(listaaocubo)
