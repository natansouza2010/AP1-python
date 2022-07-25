'''
Escreva um programa que leia inteiros positivos m e n e os elementos
de uma matriz A de números inteiros de dimensão m x n e também
um número inteiro denominado fator de multiplicação. Ao final o
programa deve mostrar a matriz multiplicada pelo fator de
multiplicação.
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

#Requisição do fator multiplicação
x=int(input("Indique o valor que sua matriz será multiplicada:"))

#Multiplicação e colocação na nova Matriz
B=[]
for i in range(len(A)):
    linha=[]
    for j in range(len(A[0])):
        produto=0
        produto=produto+A[i][j]*(int(x))
        linha.append(produto)
    B.append(linha)

print("Matriz A(Original)")
for l in range(len(A)):
    for c in range(len(A[0])):
        print(f"[{A[l][c]}]", end=" ")
    print()
print("==="*10)

print("Matriz B(Multiplicada)")
for l in range(len(B)):
    for c in range(len(B[0])):
        print(f"[{B[l][c]}]", end=" ")
    print()

