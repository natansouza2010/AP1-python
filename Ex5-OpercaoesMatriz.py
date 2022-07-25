# Matrizes tem que serem de tamanhos Iguais !

def Soma(matriz1,matriz2):
    soma=[]
    for i in range(len(matriz1)):
        for z in range(len(matriz1[i])):
            soma.append(matriz1[i][z]+matriz2[i][z])
    return soma

def Subtracao(matriz1,matriz2):
    subtracao=[]
    for i in range(len(matriz1)):
        for z in range(len(matriz1[i])):
            subtracao.append(matriz1[i][z]-matriz2[i][z])
    return subtracao

def Multiplicao(matriz1,matriz2):
    multiplicao=[]
    for i in range(len(matriz1)):
        for z in range(len(matriz1[i])):
            multiplicao.append(matriz1[i][z]*matriz2[i][z])
    return multiplicao

def Divisao(matriz1,matriz2):
    divisao=[]
    for i in range(len(matriz1)):
        for z in range(len(matriz1[i])):
            divisao.append(matriz1[i][z]/matriz2[i][z])
    return divisao


