'''
Escreva um programa em Python que verifique se uma string fornecida pelo usuário pode ser convertida em um número real positivo ou negativo. Em todas as mensagens deve ser aplicada a função de conversão float() somente para os casos onde validação seja positiva. O resultado a ser apresentado para o usuário é o seguinte:
'''

string=input("Digite uma string:")
texto=string.replace("-","")
texto1=texto.replace(".","")
if texto1.isdigit():
    print("A string pode ser convertida para o número:",string)
else:
    print("A string",string,"não pode ser convertida para um número real.")
