'''
Faça um programa em Python que leia um valor N fornecido pelo usuário e crie uma lista de N elementos do tipo Inteiro fornecidos pelo usuário como String.
Incorpore os códigos de verificação de conversão desenvolvidos nos exercícios anteriores e teste os valores antes de incluí-los na lista.
Só inclua os valores que possam ser convertidos utilizando a função de conversão int().

'''
listainteiros=[]
n=input("Digite um valor N:")
while n!="":
    if(n.isdigit()):
        listainteiros.append(n)
    n=input("Digite um valor N:")
print(listainteiros)
