listasig=[["Macaco"],["Galo"],["Cão"],["Porco"],["Rato"],["Boi"],["Tigre"],["Coelho"],["Dragão"],["Serpente"],["Cavalo"],["Carneiro"]]
listafam=[]

nome=input("Digite seu nome:")
while nome!="":
    anos=[]
    ano=input("Digite o ano de nascimento:")
    anos.append(nome)
    anos.append(int(ano))
    listafam.append(anos)
    nome=input("Digite seu nome:")
    
for i in range(len(listafam)):
    a=listafam[i][1]
    if a%12==0:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[0][0])
        
    elif a%12==1:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[1][0])
    elif a%12==2:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[2][0])
    elif a%12==3:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[3][0])

    elif a%12==4:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[4][0])
    elif a%12==5:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[5][0])
    elif a%12==6:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[6][0])
    elif a%12==7:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[7][0])
    elif a%12==8:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[8][0])
    elif a%12==9:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[9][0])
    elif a%12==10:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[10][0])
    elif a%12==11:
        print('Nome:',listafam[i][0],'Ano Nascimento:',listafam[i][1],'Signo:',listasig[11][0])    
        
        
    
    
    
