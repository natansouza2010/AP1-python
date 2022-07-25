'''
Foram anotadas as idades e alturas dos alunos de uma turma e
armazenados em uma lista cujos elementos são sublistas com dois
elementos: o primeiro é a idade do aluno e o segundo a sua altura.
Mostre quantos alunos com mais de 13 anos possuem altura inferior à
média de altura desses alunos.
'''
lista=[]
idade=input("Digite a idade:")
while idade!="":
    sublista=[]
    altura=float(input("Digite a altura:"))
    sublista.append(int(idade))
    sublista.append(altura)
    lista.append(sublista)
    idade=input("Digite a idade:")

media=0
for i in range(len(lista)):
        media=media+lista[i][1]
media=media/len(lista)
    

qtd=0
for z in lista:
    if z[0]>13 and z[1] < media:
        qtd=qtd+1

print("Existe",qtd,"alunos com mais de 13 anos de idade com altura inferior a",media)
