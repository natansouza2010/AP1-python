def fibonacci(x):
    n=0
    n1=1
    soma=0
    for z in range(0,x):
        print(soma)
        soma=n1+n
        n=n1
        n1=soma


fibonacci(int(input("Informe quantos termos você quer : ")))
