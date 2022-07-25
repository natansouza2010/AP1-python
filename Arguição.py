
#A ESTRUTURA
operadora=[]
telefonia=input("Digite o nome da Operadora:")
operadora.append(telefonia)
listausuarios=[]
nome=input("Digite o Usuário:")
while nome != "":
    usuario=[]
    usuario.append(nome)
    plano=input("Digite o tipo de Plano:")
    usuario.append(plano)
    mensal=input("Digite o valor mensal:")
    usuario.append(float(mensal))
    data=input("Digite a data de vencimento(DD/MM/AAAA):")
    usuario.append(data)
    listarecursos=[]
    rec=input("Digite o recurso:")
    while rec != "":
        recurso=[]
        recurso.append(rec)
        qtd=input("Digite a quantidade:")
        recurso.append(int(qtd))
        valor=input("Digite o valor:")
        recurso.append(float(valor))
        rec=input("Digite o recurso:")
        listarecursos.append(recurso)
    usuario.append(listarecursos)
    nome=input("Digite o Usuário:")
    listausuarios.append(usuario)
operadora.append(listausuarios)
listausuarios=[listausuarios]
'''

operadora=["Tim",[['natan', 'gold',10.00, '09/06/2020', [["ligações locais", 10, 56.00], ["internet", 1, 300.00], ["ligações internacionais", 0, 45.00]]],
                 ['zilma','black', 60.00,'18/07/2020', [['ligações locais', 0,  26.00], ['internet', 1, 200.00], ['ligações internacionais', 0, 45.00]]],
                  ['silvana','black',110.00,'18/07/2020', [['ligações locais', 0,  26.00], ['internet', 1, 200.00], ['ligações internacionais', 0, 45.00]]],
                ['gabriela','blue', 60.00, '09/06/2020', [['ligações locais', 10,  1.00], ['internet', 15, 1.00], ['ligações internacionais', 6, 1.00]]]]]


#Mostre o valor médio do valor mensal básico pago pelos clientes para a operadora e o nome dos clientes que pagam esse
#valor. Este item deve ser implementado percorrendo a estrutura montada, sem alterar o código anterior do programa.
somamensal=0
for i in range(len(operadora[1])):
    somamensal=somamensal+operadora[1][i][2]
media=somamensal/len(operadora[1])

indices=[]
for z in range(len(operadora[1])):
    if operadora[1][z][2]==media:
        indices.append(z)


for h in indices:
    print("Nome:",operadora[1][h][0], "Plano:",operadora[1][h][1]," Data Vencimento:",operadora[1][h][3])
    

'''













#print("EXERCÍCIO B")    
#B RELATÓRIO
print("Operadora:",operadora[0])
for i in range(len(listausuarios[0])):
    print("Usuário:",listausuarios[0][i][0],"Plano:",listausuarios[0][i][1],"Valor Mensal:",listausuarios[0][i][2],"Data Vencimento:",listausuarios[0][i][3])
    for j in range(len(listausuarios[0][i][4])):
        print("====================")
        print("Recurso:",listausuarios[0][i][4][j][0],"\n""---------""\n""Quantidade:",listausuarios[0][i][4][j][1],"\n""Valor:",listausuarios[0][i][4][j][2])
        print("====================")


#C (2,0 pontos) Mostre todos os dados do usuário que possui o plano telefônico de menor valor mensal básico e
#substitua todas as letras “a” do nome do usuário por “#” sem utilizar o método replace();

menorvalormensal=listausuarios[0][0][2]
indicemenor=0
for i in range(len(listausuarios[0])):
    if listausuarios[0][i][2]<menorvalormensal:
        menorvalormensal=listausuarios[0][i][2]
        indicemenor=i
    
listadado=listausuarios[0][indicemenor]
nome=listadado[0]
newnome=[]

for ind in range(len(nome)):
    if nome[ind]=="a":       
        newnome.append("#")
    else:                
        newnome.append(nome[ind])
        
novonome=''                        
for i in newnome:
    novonome=novonome+i
    
listadado[0]=novonome

print("EXERCÍCIO C")
print("O dados do usuário que possui o plano telefônico de menor valor mensal básico")
print(listadado)


                            
                    

#D Mostre todos os dados do usuário que pagará o maior valor de fatura (valor mensal básico +
#valores dos recursos utilizado
valoresfatura=[]
for i in range(len(listausuarios[0])):
    somafatura=0
    soma=listausuarios[0][i][2]
    multirec=0
    for n in range(len(listausuarios[0][i][4])):
        multirec=multirec+(listausuarios[0][i][4][n][1] * listausuarios[0][i][4][n][2])
    somafatura=soma+multirec
    valoresfatura.append(somafatura)
    
x=0
maior=valoresfatura[0]
for i in valoresfatura:
    if i > maior:
        maior=i
        x=x+1
        
print("EXERCÍCIO D")    
print("O dados do usuário que pagará o maior valor de fatura (valor mensal básico +valores dos recursos utilizado")
print(listausuarios[0][x])
        
#E(2,0 pontos) Mostre todos os dados do usuário que apresenta maior valor de consumo para o recurso
#“internet” e data de vencimento com o mês fornecido pelo usuário, sendo o formato da data de vencimento
#igual a DD/MM/AAAA; ;

mesvencimento=input("Digite o mês do vencimento da fatura:")
indicenet=0
maiornet=0
for i in range(len(listausuarios[0])):
    if listausuarios[0][i][3]==mesvencimento:
        for n in range(len(listausuarios[0][i][4])):
            if listausuarios[0][i][4][n][0] == 'internet':
                somanet=listausuarios[0][i][4][n][1] * listausuarios[0][i][4][n][2]
                if somanet > maiornet:
                    maiornet=somanet
                    indicenet=indicenet+i            
print("EXERCÍCIO E")
print("O Usúário que possui o maior valor de consumo para o recurso internet")                  
print(listausuarios[0][indicenet])

#f) (2,0 pontos) Mostre os dados dos usuário que possui o valor total da fatura (valor mensal básico + valores dos
#recursos utilizados) mais próximo do valor médio de fatura total entre todos os usuários.
totalvalores=0
for i in valoresfatura:
    totalvalores=totalvalores+i
mediatotal=totalvalores/len(valoresfatura)

listadiferença=[]
for i in valoresfatura:
    diferença=i-mediatotal
    listadiferença.append(diferença)
    
listadiferençapositiva=[]
for z in listadiferença:
    if z>0:
        listadiferençapositiva.append(z)
    else:
        listadiferençapositiva.append(z*-1)
    
menordiferença=listadiferençapositiva[0]
indice=0
for z in listadiferençapositiva:
    if z<menordiferença:
        menordiferença=z
        indice=indice+1

print("EXERCÍCIO F")        
print("O usúario que possui o valor total da fatura mais próximo da fatura é:")    
print(listausuarios[0][indice])





            
              
          
                    
                
               
                    
                    


