

palavra=input("Digite uma palavra: ")
caractere=input("Digite um caractere a ser apagado: ")
indice = 0
existe_letra = False
a=''
b=''
c=''

while indice < len(palavra) and not existe_letra:
    if palavra[indice] == caractere:
        existe_letra = True
        if existe_letra:
            
            for z in palavra[0:indice]:
                a=a+z
                
                
            for j in palavra[(indice+1):len(palavra)]:
                b=b+j

            c=a+b
    
                    
            
    else:
        indice = indice + 1




print('A palavra sem a letra é:',c)
