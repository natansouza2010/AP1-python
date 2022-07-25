import string

def ValidaInteiroPositivo(nro):
    if nro[0] == "+":
        nro = nro[1:]
    for i in nro:
        if i not in string.digits:
            return False
    return True


def ValidaInteiroPositivoNegativo(nro):
    texto=nro.replace("-","")
    if(texto.isdigit()):
        return True
    else:
        return False


def ValidaReaisPositivoNegativo(nro):
    texto=nro.replace("-","")
    texto1=texto.replace(".","")
    if texto1.isdigit():
        return True
    else:
        return False

    
