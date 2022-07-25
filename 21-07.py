'''
Elabore um programa que solicite ao usuário informar uma texto de qualquer tamanho e uma palavra que ele deseja procurar no texto.
O programa deve mostra na tela se a palavra procurada se encontra no texto e em quais posições (índice inicial e índice final) de cada uma das ocorrências.
Não deverão ser utilizados os métodos find e index, bem como suas variações, pois não serão considerados. Exemplo:
Frase: Sua alegria traz alegria para minha vida!

Palavra: alegria

Ocorrências:

Início:4   Término:10

Início:17  Término:23

ou então: "Não há ocorrências da palavra procurada no texto".
'''
texto=input("Digite alguma frase:")
palavra=input("Digite uma palavra:")
indice=0
if palavra in texto:
    while indice<len(texto):
        if texto[indice:len(palavra)+indice]==palavra:
            inicio=indice
            fim=(inicio+len(palavra)-1)
            print("Início:",inicio, "Término:",fim)
        indice=indice+1
else:
    print("Não há ocorrências da palavra procurada no texto")
    
   

    
  
    
    
