'''
Faça um programa em Python que crie duas listas de valores inteiros a partir de strings fornecidas pelo usuário
(o critério de parada para a entrada de dados em cada lista pode ser o <ENTER>). Faça a consistência utilizando
o código que você criou no exercício 2 antes de inserir o elemento na lista. Gere como resultado a lista INTERSECÇÃO e mostre na tela.
A lista INTERSECÇÃO deve ser construída com os elementos que estão presentes nas duas listas sem repetição de elementos.Faça um programa em Python que
crie duas listas de valores inteiros a partir de strings fornecidas pelo usuário (o critério de parada para a entrada de dados em cada lista pode ser o <ENTER>).
Faça a consistência utilizando o código que você criou no exercício 2 antes de inserir o elemento na lista.
Gere como resultado a lista INTERSECÇÃO e mostre na tela. A lista INTERSECÇÃO deve ser construída com os elementos que estão presentes nas
duas listas sem repetição de elementos.
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
  
listainter=[]
for y in lista2:
    if y in lista1:
        listainter.append(y)
        
print("Lista interseccão (sem repetição):",listainter)

