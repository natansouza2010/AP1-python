import ValidaValores

def fatorial(nro):
    if nro==0:
        return 1
    else:
        return nro*fatorial(nro-1)


n=int(input("Digite um número: "))

if n>=0:
    if ValidaValores.ValidaInteiroPositivo(str(fatorial(n))):
        print("O valor do fatorial é:", fatorial(n))
        print("O Número digitado é um Inteiro Positivo!")
else:
    print("O Número digitado não é um Inteiro Positivo!")
    print("Não Existe Fatorial de Número Negativo!")

    

