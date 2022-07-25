#Tamanhos das listas tem que ser IGUAIS


def Uniao(lista1,lista2):
    uniao=lista1+lista2
    return uniao


def Diferenca(lista1,lista2):
    diferença=[]
    for i in lista1:
        if i not in lista2:
            diferença.append(i)

    for z in lista2:
        if z not in lista1:
            diferença.append(z)
    return diferença

def Interseccao(lista1,lista2):
    interseccao=[]
    for i in lista2:
        if i in lista1:
            interseccao.append(i)
    return interseccao


def Soma(lista1,lista2):
    soma=[]
    for i in range(len(lista1)):
        soma.append(lista1[i]+lista2[i])
    return soma

def Multiplicao(lista1,lista2):
    multiplicao=[]
    for i in range(len(lista1)):
        multiplicao.append(lista1[i]*lista2[i])
    return multiplicao

def Subtracao(lista1,lista2):
    subtracao=[]
    for i in range(len(lista1)):
        subtracao.append(lista1[i]-lista2[i])
    return subtracao

def Divisao(lista1,lista2):
    divisao=[]
    for i in range(len(lista1)):
        divisao.append(lista1[i]/lista2[i])
    return divisao
    

    
