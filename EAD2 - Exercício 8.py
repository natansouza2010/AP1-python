'''
Faça um programa em Python que crie duas listas de valores inteiros a partir de strings fornecidas pelo usuário
(o critério de parada para a entrada de dados em cada lista pode ser o <ENTER>). Faça a consistência utilizando o código que você
criou no exercício 2 antes de inserir o elemento na lista. Gere como resultado a lista DIFERENÇA e mostre na tela. A lista DIFERENÇA
deve ser construída com os elementos que ESTÃO presentes nas na lista 1 e que NÃO estão na lista 2, sem repetição de elementos.
'''



lista1=[]
n1=input("Digite um número para a primeira lista:")
while n1!="":
    if n1.isdigit():
        lista1.append(n1)
    n1=input("Digite um número para a primeira lista:")
lista2=[]

n2=input("Digite um número para a segunda lista:")
while n2!="":
    if n2.isdigit():
        lista2.append(n2)
        n2=input("Digite um número para a segunda lista:")

lista3=[]

        
for z in lista1:
    if z not in lista2:
        lista3.append(z)
          
print("Lista Diferença:",lista3)
