maior=0
menor=1000000000000000000
qtcid=0
qtveiculos=0
CID=0
nroTOTALACID=0
cod=input("Digite o código da cidade:")
while cod !="0":
    nomecid=input("Digite o nome da cidade:")
    nroveiculos=int(input("Digite o número de veículos de passeio:"))
    nroacid=int(input("Digite o número de acidentes de trânsitos com vítimas:"))
    
    #CÁLCULOS a ( MÉDIA DE ACIDENTES POR CIDADE)
    if nroveiculos<1000:
        
        CID=CID+1
        
        nroTOTALACID=nroTOTALACID+nroacid
        
        mediaAcid= nroTOTALACID/CID
    else:
        mediaAcid=0
        
                                             
    #CÁLCULOS b (MAIOR E MENOR INDICE)
    ind=(nroacid/nroveiculos)*100
    if ind>maior:
        maior=ind
        nomecidMAIOR=nomecid

    if ind<menor:
        menor=ind
        nomecidMENOR=nomecid
    #CÁLCULOS c(MÉDIA DE VEÍCULOS POR CIDADE)
    qtcid=qtcid+1
    qtveiculos=qtveiculos+nroveiculos
    cod=input("Digite o código da cidade:")

    mediaCID=qtveiculos/qtcid

print("A MÉDIA DE ACIDENTES DE TRÂNSITOS ENTRE AS CIDADES COM MENOS DE 1000 VEÍCULOS DE PASSEIO É ",mediaAcid)
print("O MAIOR ÍNDICE DE ACIDENTES DE TRÂNSITO É DE",maior,"% DA CIDADE:",nomecidMAIOR)
print("O MENOR ÍNDICE DE ACIDENTES DE TRÂNSITO É DE",menor,"&DA CIDADE:",nomecidMENOR)
print("A MÉDIA DE VEÍCULOS CONSIDERANDO TODAS AS CIDADES É DE:",mediaCID)
        
