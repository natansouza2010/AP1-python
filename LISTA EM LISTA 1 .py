turma=[]
nome=input("Nome do Aluno:")
nota=0
while nome != "":
    aluno=[]
    lista_notas=[]
    aluno.append(nome)
    idade=int(input("Idade:"))
    aluno.append(idade)
    peso=int(input("Peso:"))
    aluno.append(peso)
    nota=input("Notas:")
    while nota !="":
        lista_notas.append(nota)
        nota=input("Notas:")
    aluno.append(lista_notas)
    turma.append(aluno)
    nome=input("Nome do Aluno:")
'''

#A
for z in turma:
    print("Nome:",z[0],"Idade:",z[1],"Peso:",z[2])
    print("Notas:",end="")
    for nota in z[3]:
        print(nota,"",end="")

   

#B
aluno_maisnovo=aluno[0]
menor=aluno[1]
for aluno in turma:
    if aluno[1]<menor:
        menor=aluno[1]
        aluno_maisnovo=aluno[0]
print('O aluno mais novo é {}'.format(aluno_maisnovo))

#C
aluno_maisvelho=aluno[0]
maior=aluno[1]
for aluno in turma:
    if aluno[1]>maior:
        maior=aluno[1]
        for notas in lista_notas:
            if notas<6:
                 aluno_maisvelho=aluno[0]
print('O aluno mais velho é {}'.format(aluno_maisvelho))


#D O nome e a idade do aluno mais pesado;

alunomaispesado=aluno[0]
idademaispesado=aluno[1]
maiorpeso=aluno[2]
for aluno in turma:
    if aluno[2]>maiorpeso:
        maiorpeso=aluno[2]
        alunomaispesado=aluno[0]
        idademaispesado=aluno[1]
print('O aluno mais pesado é {} com {} anos'.format(alunomaispesado,idademaispesado))


#E O nome e a média de notas de cada aluno
for z in range(len(turma)):
    soma=0
    media=0
    for nota in turma[z][3]:
        soma=soma+int(nota)
        media=soma/len(turma[z][3])
    print(' O aluno {} possui a média de notas de {}'.format(turma[z][0],media))





#F O nome, a nota mais baixa e a nota mais alta de cada aluno;
nomealuno=aluno[0]
notamaisbaixa=100000000000000000
notamaisalta=0

for z in range(len(turma)):
    for nota in turma[z][3]:
        if int(nota) < int(notamaisbaixa):
            notamaisbaixa=nota
        if int(nota)> int(notamaisalta):
            notamaisalta=nota
    print('O aluno {} possui a nota mais baixa {} e a nota mais alta {}'.format(turma[z][0],notamaisbaixa,notamaisalta))



#G O pior aluno entre todos (a menor nota entre todas as notas);
pioraluno=aluno[0]
notabaixa=100000000000000
for z in range(len(turma)):
    for notas in turma[z][3]:
        if int(notas)<int(notabaixa):
            notabaixa=notas
            pioraluno=aluno[0]
print('O aluno {} é o pior aluno com a nota {}'.format(pioraluno,notabaixa))


#H O melhor aluno entre todos(a maior nota entre todas as notas);
melhoraluno=aluno[0]
notamaisalta=0
for z in range(len(turma)):
    for notas in turma[z][3]:
        if int(notas)>int(notamaisalta):
            notamaisalta=notas
            melhoraluno=aluno[0]            
print('O aluno {} é o melhor aluno com a nota {}'.format(melhoraluno,notamaisalta))


#I Os nomes de todos os alunos que possuem pelo menos uma nota igual a 10

listaalunos10=[]
for z in range(len(turma)):
    for notas in turma[z][3]:
        if int(notas)==10:
            aluno10=turma[z][0]
            listaalunos10.append(aluno10)
            
for aluno10 in listaalunos10:
    print('Os alunos com pelo menos uma nota 10 são:{}'.format(aluno10))


#J Todos os dados dos alunos que possuem a substring “de” em seus nomes;

string='de'
for z in range(len(turma)):
    if string in turma[z][0]:
        for y in turma[z]:
            print(y)


#K Todos os dados do aluno que possui o nome mais comprido (pode haver empates)
nomemaiscomprido=0
posição=0
for z in range(len(turma)):
    for nomes in turma[z][0]:
        if len(nomes)>nomemaiscomprido:
            nomemaiscomprido=len(nomes)
            posição=posição+1
for h in turma[posição]:
    print(h)

'''
            

    








