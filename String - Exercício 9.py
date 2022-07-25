
palavra1=input('Digite uma palavra:').upper()
palavra2=input('Digite outra palavra:').upper()
alfabeto="ABCDEFGHIJKLMNOPQSTUVXWYZ"
a=''
b=''

if len(palavra1)==len(palavra2):
    for letra in alfabeto:
        for z in palavra1:
            if letra==z:
                a=a+letra

    for letra in alfabeto:
        for y in palavra2:
            if letra==y:
                b=b+letra
    if a==b:
        print("São anagramas")
    else:
        print("Não são anagramas")
else:
    print("Não são anagramas")
    
