matriz = []
l=int(input('Digite o valor de linhas:'))
c=int(input('Digite o valor de colunas:'))
for i in range(l):
    linha = []
    for z in range(c):
        num=int(input('Digite o elemento ['+ str(i)+']['+str(z)+']'))
        linha.append(num)
    matriz.append(linha)

maior=matriz[0][0]
for i in range(len(matriz)):
    for j in range(len(matriz)):
        elemento=matriz[i][j]
        if elemento > maior:
            maior=elemento           

print("O maior elemento da matriz é:",maior," na posição["+str(i)+']['+str(j)+']')
            
    
