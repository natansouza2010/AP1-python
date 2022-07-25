'''
Faça um programa que percorre uma lista com o seguinte formato:
[['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha',
[7,8]]]. Essa lista indica o número de faltas que cada time fez em cada
jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a
Itália fez 9. O programa deve imprimir na tela: a) o total de faltas do
campeonato; b) o time que fez mais faltas num único jogo; c) o time que
fez menos faltas num único jogo.
'''

placar=[['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha',[7,8]]]

#a) o total de faltas do campeonato
    
totalfaltas=0
for i in placar:
    for z in i[2]:
        totalfaltas=totalfaltas+z
print("O total de faltas nos jogos são :",totalfaltas)


#b o time que fez mais faltas num único jogo;
nrofalta=placar[0][2][0]
timemaisfalta=placar[0][0]

for i in range(len(placar)):
    for jogos in placar[i][2]:
        if int(jogos)>nrofalta:
            nrofalta=int(jogos)
            timemaisfalta=placar[i][0]
print("O time com mais falta num único jogo:",timemaisfalta)

#c o time que fez menos faltas num único jogo;
nrofalta=placar[0][2][0]
timemenosfalta=placar[0][0]
for i in range(len(placar)):
    for jogos in placar[i][2]:
        if int(jogos)<nrofalta:
            nrofalta=int(jogos)
            timemenosfalta=placar[i][0]
print("O time com menos falta num único jogo:",timemenosfalta)

        
            
        
        
            
        

