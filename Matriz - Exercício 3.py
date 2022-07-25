'''
um programa que lê o valor de n e uma matriz A de inteiros de dimensão
n x n, e crie a matriz transposta de A (At
). Ao final deve ser mostrada a
matriz original e sua respectiva transposta. Matriz Transposta: matriz
A
t obtida a partir da matriz A trocando-se ordenadamente as linhas por
colunas ou as colunas por linhas.
'''
matriz = []
l=int(input('Digite o valor de linhas:'))
c=int(input('Digite o valor de colunas:'))
for i in range(l):
    linha = []
    for z in range(c):
        num=int(input('Digite o elemento ['+ str(i)+']['+str(z)+']'))
        linha.append(num)
    matriz.append(linha)


#Matriz Nula/ para transposição
nrolinhas=(len(matriz))
nrocolunas=(len(matriz[0]))
transposta=[]
for i in range(nrocolunas):
    linha=[]
    for j in range(nrolinhas):
        linha.append(0)
    transposta.append(linha)
        
#Transposição
for i in range(nrolinhas):
    for j in range(nrocolunas):
        transposta[j][i]=matriz[i][j]

#Prints das matrizes
print("Matriz A")
for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        print(f"[{matriz[l][c]}]", end=" ")
    print()

print("Matriz Transposta de A")
for l in range(len(transposta)):
    for c in range(len(transposta[0])):
        print(f"[{transposta[l][c]}]", end=" ")
    print()

'''
#Tranposição 2 
transposta=[]
for j in range(len(matriz[0])):
    linha=[]
    for i in range(len(matriz)):
        linha.append(matriz[i][j])
    transposta.append(linha)

'''
        
