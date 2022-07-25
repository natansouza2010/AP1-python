'''
Escreva um programa em Python que verifique se uma string fornecida pelo usuário pode ser convertida em um número inteiro positivo ou inteiro negativo. Em todas as mensagens deve ser aplicada a função de conversão int() somente para os casos onde validação seja positiva. O resultado a ser apresentado para o usuário é o seguinte:

Exemplo de testes de mesa:

entrada: 123  --> mensagem na tela: A string pode ser convertida para o número 123.

entrada: 12b  --> mensagem na tela: A string 12b não pode ser convertida para um número inteiro.

entrada: -123 --> mensagem na tela: A string -123 pode ser convertida para o número -123.

entrada:12.3 --> mensagem na tela: A string 12.3 não pode ser convertida para um número inteiro.

entrada: -12+34 --> mensagem na tela: A string -12+34 não pode ser convertida para um número inteiro.

entrada: 12.34.56 --> mensagem na tela: A string -12.34.56 não pode ser convertida para um número inteiro.

'''
string=input("Digite uma string:")

texto=string.replace("-","")

if(texto.isdigit()):
    print(" A string pode ser convertida para o número.",string)
else:
    print(" A string",string," não pode ser convertida para um número inteiro positivo.")

