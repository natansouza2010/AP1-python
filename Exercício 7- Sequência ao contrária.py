'''
. Crie um programa que leia inicialmente uma sequência de N números
inteiros fornecidos pelo usuário e mostre ao final da leitura a sequência
original e a sequência invertida.
'''

lista=[]
aocontrario=[]
n=input('Digite um número:')
while n!='':
    lista.append(int(n))
    n=input('Digite um número:')
for idx in range((len(lista)-1),-1,-1):
    aocontrario.append(int(lista[idx]))
print('Lista original:',lista)
print('Lista invertida:',aocontrario)


