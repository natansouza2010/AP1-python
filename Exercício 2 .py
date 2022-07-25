alturas=[]
alt=input('Digite uma altura:')
posicao=0
maior=alt
while alt!="":
    alturas.append(float(alt))
    alt=input('Digite uma altura:')
    if alt>maior:
        maior=alt
        posicao=posicao+1
print("A sequência de alturas é :",alturas,"a maior altura:",maior,"e está na posição:",posicao)

