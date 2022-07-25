def media(a,b,c,d):
    soma=a+b+c+d
    mediafinal=soma/4
    if mediafinal>=6:
        return True
    else:
        return False
a=float(input("Digite uma nota:"))
b=float(input("Digite uma nota:"))
c=float(input("Digite uma nota:"))
d=float(input("Digite uma nota:"))
mediafinal=media(a,b,c,d)
print(mediafinal)

