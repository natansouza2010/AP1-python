matriz = []
l=int(input('Digite o valor de linhas:'))
c=int(input('Digite o valor de colunas:'))
for i in range(l):
    linha = []
    for z in range(c):
        num=int(input('Digite o elemento ['+ str(i)+']['+str(z)+']'))
        linha.append(num)
    matriz.append(linha)

print("Matriz:",l,"x",c)
for l in range(len(matriz)):
    for c in range(len(matriz[0])):
        print(f"[{matriz[l][c]}]", end=" ")
    print()
