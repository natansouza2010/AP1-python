
frase=input('Digite uma frase:')
a=0
e=0
i=0
o=0
u=0
espaço=0
for z in frase:
    if str(z) == "a":
        a=a+1
    elif str(z)=="e":
        e=e+1
    elif str(z)=="i":
        i=i+1
    elif str(z)=="o":
        o=o+1
    elif str(z)=="u":
        u=u+1
    elif str(z)==" ":
        espaço=espaço+1
        
print('A frase {} possui respectivamente as vogais : A:({}) E:({}) I:({}) O:({}) U:({}) e {} espaços' .format(frase,a,e,i,o,u,espaço))
