'''
5. Escreva um programa que leia inteiros positivos m e n e os elementos
de uma matriz A de números inteiros de dimensão m x n e ao final
mostra a quantidade de linhas e colunas que tem apenas zeros (linhas
nulas e colunas nulas).
'''
A = []
l=int(input('Digite o valor de linhas:'))
c=int(input('Digite o valor de colunas:'))
for i in range(l):
    linha = []
    for z in range(c):
        num=int(input('Digite o elemento ['+ str(i)+']['+str(z)+']'))
        linha.append(num)
    A.append(linha)

linha=len(A)
coluna=len(A[0])

#Total de Linhas Nulas 
tLinha=0
for i in range(linha):
    somaelemento=0
    for elemento in A[i]:
        somaelemento=somaelemento+elemento
    if somaelemento==0:
        tLinha=tLinha+1

#Tranposição da Matriz para cálculo da coluna 
transposta=[]
for j in range(len(A[0])):
    linha=[]
    for i in range(len(A)):
        linha.append(A[i][j])
    transposta.append(linha)


#Total de Colunas 
tColuna=0
for i in range(len(transposta)):
    somaelemento=0
    for elemento in transposta[i]:
        somaelemento=somaelemento+elemento
    if somaelemento==0:
        tColuna=tColuna+1

print("A Matriz contém :",tLinha," linhas nulas e,",tColuna,"colunas nulas") 
