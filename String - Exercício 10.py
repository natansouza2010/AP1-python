
num=input('Digite um número inteiro positivo ou negativo:')
i=0
dig=0
negativo=False
while i<len(num):
    if num[i]=="-" and not negativo:
        dig=dig-1
        negativo=True
    dig=dig+1
    i=i+1
print("O número",num,"possui:",dig,"dígitos")
    
    
    
