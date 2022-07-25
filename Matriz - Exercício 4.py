'''
Escreva um programa que lê um valor n e uma matriz A de inteiros de
dimensão n x n, e verifica se A é simétrica. Matriz simétrica: matriz
quadrada de ordem n tal que A = At
'''
matriz = []
n=int(input('Digite o valor de linhas e de colunas (Matriz Quadrática):'))
for i in range(n):
    linha = []
    for z in range(n):
        num=int(input('Digite o elemento ['+ str(i)+']['+str(z)+']'))
        linha.append(num)
    matriz.append(linha)
    
teste=True
for i in range(n):
    for j in range(n):
        if matriz[i][j]!=matriz[j][i]:
            teste=False

if teste==True:
    print("É uma matriz simétrica")
else:
    print("Não é uma matriz simétrica")
