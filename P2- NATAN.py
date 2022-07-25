import os
'''
Estrutura

dc_cliente[CPF]=[nome, rua, nro, bairro, cidade, estado, telefone, e-mail]


dc_planos[CodPlano]=( TipoPlano, ValorMensalBasico, [[recursodisponível1, qtde_max1, valor_unitário1],
[recursodisponível2, qtde_max2, valor_unitário2],...,[recursodisponívelN, qtde_maxN, valor_unitárioN]] )

dc_consumo[(CPF, CodPlano)]:[DataVencimento, [[recurso_consumido1, qtde], [recurso_consumido2, qtde],
....., [recurso_consumidoN, qtde]]]

'''
#=============================================================================================#
def mostrarmenu():
    print("1. Gerenciamento de Clientes")
    print("2. Gerenciamento de Planos")
    print("3. Gerenciamento de Consumo")
    print("4. Relatórios")
    print("5. Sair")
#=============================================================================================#
def submenuClientes():
    print("\n\nGerenciamento de Clientes:\n")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
#=============================================================================================#
def submenuPlanos():
    print("\n\nGerenciamento de Planos:\n")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
#=============================================================================================#
def submenuConsumo():
    print("\n\nGerenciamento de Consumo:\n")
    print("1 - Listar todos")
    print("2 - Listar um")
    print("3 - Incluir")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
#=============================================================================================#
def submenuRelatorio():
    print("\n\nRELATÓRIOS\n")
    print("1-  Relatório(D) ")
    print("2-  Relatório(E) ")
    print("3-  Relatório(F) ")
    print("4-  Sair")
    
#=============================================================================================#
def existe_cliente(dicionario,chave):
    if chave in dicionario:
        return True
    else:
        return False

    
def existe_plano(dicionario,chave):
    if chave in dicionario:
        return True
    else:
        return False

def existe_consumo(dicionariocliente,dicionarioplano,cpf,cod):
    if cpf in dicionariocliente and cod in dicionarioplano:
        return True
    else:
        return False
#=============================================================================================#
    
def grava_Cliente(dicionario):
    ref_arq=open('clientes.txt', 'w' )
    for chave in dicionario:
        linha=''
        linha=linha + str(chave) + '\t'
        valor=dicionario[chave]
        linha= linha + valor[0] + '\t' #nome
        linha= linha + valor[1] + '\t' #rua
        linha= linha + valor[2] + '\t' #nro
        linha= linha + valor[3] + '\t' #bairro
        linha= linha + valor[4] + '\t' #cidade
        linha= linha + valor[5] + '\t' #estado
        linha= linha + valor[6] + '\t' #telefone
        linha= linha + valor[7] + '\t' #e-mail
        linha = linha + '\n'
        ref_arq.write(linha)
    ref_arq.close()

def grava_Plano(dicionario):
    ref_arq=open('planos.txt', 'w' )
    for chave in dicionario:
        linha=""
        linha= linha + str(chave) + '\t'
        valor=dicionario[chave]
        linha= linha + valor[0] +  '\t' # TipoPlano
        linha= linha + str(valor[1]) +  '\t' # ValorMensal
        lista=valor[2]
        linha= linha + str(len(lista)) + '\t' # Nro de recursos
        for i in range(len(lista)):
            if i!=0:
                linha= linha + '#'+ '\t'
            for j in range(len(lista[i])):
                linha=linha+ str(lista[i][j]) + '\t'#Recursos
        linha = linha + '#'+'\t'
        linha = linha + '\n'
        ref_arq.write(linha)
    ref_arq.close()

def grava_Consumo(dicionario):
    ref_arq=open('consumos.txt', 'w' )
    for chave in dicionario:
        linha=''
        linha = str(chave[0]) + '\t'
        linha = linha + str(chave[1]) + '\t'
        valor=dicionario[chave]
        linha= linha + valor[0] + '\t' # Data nascimento
        lista=valor[1]
        linha= linha + str(len(lista)) + '\t' # nro de recursos adcionados
        for i in range(len(lista)):
            if i!=0:
                linha= linha +'#' + '\t'
            for j in range(len(lista[i])):
                linha=linha+ str(lista[i][j]) + '\t'#Recursos
        linha = linha + '#'+'\t'
        linha = linha + '\n'
        ref_arq.write(linha)
    ref_arq.close()
            
                
#=============================================================================================#
def le_arquivoCliente(dicionario):
    ref_arq=open('clientes.txt','r')
    for linha in ref_arq:
        cliente=linha.split('\t')
        chave=cliente[0]
        nome=cliente[1]
        rua=cliente[2]
        nro=cliente[3]
        bairro=cliente[4]
        cidade=cliente[5]
        estado=cliente[6]
        telefone=cliente[7]
        email=cliente[8]
        valor=[nome, rua, nro, bairro, cidade, estado, telefone, email]
        dicionario[chave]=valor
    ref_arq.close()

def le_arquivoPlano(dicionario):
    ref_arq=open('planos.txt','r')
    for linha in ref_arq:
        plano=linha.split('\t')
        chave=int(plano[0])
        tipoplano=plano[1]
        valormensal=float(plano[2])
        nrorecursos=int(plano[3])
        recurso=plano[4:4 + nrorecursos*4]
        rec=[]
        rec2=[]
        for index in range(len(recurso)):
            if recurso[index] != '#':
                rec.append(recurso[index])
            else:
                rec2.append(rec)    
                rec=[]
            
        valor=(tipoplano, valormensal, [])
        rec3=[]
        rec4=[]
        for index in range(len(rec2)):
            rec3=[]
            tipo=rec2[index][0]
            qtde=int(rec2[index][1])
            valor=float(rec2[index][2])
            rec3.append(tipo)
            rec3.append(qtde)
            rec3.append(valor)
            rec4.insert(index, rec3)

        valor=(tipoplano, valormensal, rec4)
        dicionario[chave]=valor
    ref_arq.close()

            
def le_arquivoConsumo(dicionario):
    ref_arq=open('consumos.txt','r')
    for linha in ref_arq:
        consumo=linha.split('\t')
        chave=(consumo[0],int(consumo[1]))
        
        datanasc=consumo[2]
        nrorecursos=int(consumo[3])
        recurso=consumo[4:4 + nrorecursos * 3]
        rec=[]
        rec2=[]
        
        for i in range(len(recurso)):
            if recurso[i] != '#':
               rec.append(recurso[i])
            else:
                rec2.append(rec)
                rec=[]
        rec3=[]
        rec4=[]
        for indice in range(len(rec2)):
            rec3=[]
            rec_consumido=rec2[indice][0]
            qtde=int(rec2[indice][1])
            rec3.append(rec_consumido)
            rec3.append(qtde)
            rec4.insert(indice, rec3)
            
        valor=[datanasc,rec4]
        dicionario[chave]=valor
               
#=============================================================================================# 
def cadastro_Cliente(dicionario):
    print("\nNova Pessoa\n")
    cpf=input("Digite o seu CPF:")
    chave=cpf
    if existe_cliente(dicionario,cpf):
        print("Pessoa já cadastrada")
    else:
        nome=input("Digite o nome:")
        rua=input("Digite a rua:")
        nro=input("Digite o número:")
        bairro=input("Digite o bairro:")
        cidade=input("Digite o cidade:")
        estado=input("Digite a estado:")
        telefone=input("Digite o telefone:")
        email=input("Digite o e-mail:")
        valor=[nome,rua,nro,bairro,cidade,estado,telefone,email]
        dicionario[chave]=valor
        print("Cadastramento realizado com sucesso!!!")

        

def cadastro_Plano(dicionario):
    print("\nNovo Plano\n")
    cod=int(input("Digite o Código do Plano:"))
    chave=cod
    if existe_plano(dicionario,cod):
        print("Plano já cadastrado")
    else:
        tipo=input("Digite o tipo do plano:")
        valormensal=float(input("Digite o valor mensal:"))
        lista_recursos=[]
        rec=input("Digite o recurso:")
        while rec != "":
            recursos=[]
            recursos.append(rec)
            qtd=input("Digite a quantidade:")
            recursos.append(int(qtd))
            valor=input("Digite o valor:")
            recursos.append(float(valor))
            rec=input("Digite o recurso:")
            lista_recursos.append(recursos)
            
        valor=(tipo, valormensal, lista_recursos)
        dicionario[chave]=valor
        print("Cadastramento realizado com sucesso!!!")


def cadastro_Consumo(dicionario,dicionarioplanos,cpf,cod,chave):
    print("\nNovo Consumo\n")
    datanasc=input("Digite a Data de Vencimento(DD/MM/AAAA):")
    recursosdisp=[]
    qtdemax=[]
    for i in range(len(dicionarioplanos[cod][2])):
        recursosdisp.append(dicionarioplanos[cod][2][i][0])
        qtdemax.append(dicionarioplanos[cod][2][i][1])
        
    print("Opções disponivéis:")
    for z in range(len(recursosdisp)):
        print("-" ,recursosdisp[z],"- Quantidade máxima:",qtdemax[z])

    
    lista_rec_consumido=[]
    print("Digite uma opção CORRETAMENTE")
    rec=input("Digite o recurso:")
    while rec in recursosdisp:
        rec_consumido=[]
        rec_consumido.append(rec)
        qtde=int(input("Digite a Quantidade:"))
        rec_consumido.append(qtde)
        rec=input("Digite o recurso:")
        lista_rec_consumido.append(rec_consumido)

    valor=[datanasc,lista_rec_consumido]
    dicionario[chave]=valor
    print("Cadastramento realizado com sucesso!!!")  
        



#=============================================================================================#
def menuAlteracaoCliente():
    print("==========OPÇÕES===========!!")
    print("1- Alterar CPF")
    print("2- Alterar Nome")
    print("3- Alterar Rua")
    print("4- Alterar Nro")
    print("5- Alterar Bairro")
    print("6- Alterar Cidade")
    print("7- Alterar Estado")
    print("8- Alterar Telefone")
    print("9- Alterar Email")
    print("10- Sair")

def menuAlteracaoPlano():
    print(" ==========OPÇÕES===========")
    print("1- Alterar Código")
    print("2- Alterar Tipo do Plano")
    print("3- Alterar Valor Mensal")
    print("4- Alterar Recursos")
    print("5- Sair")

def menuAlteracaoConsumo():
    print(" ==========OPÇÕES===========")
    print("1- Alterar CPF e Código")
    print("2- Alterar Data de Nascimento")
    print("3- Alterar Recursos Consumidos")
    print("5- Sair")
#=============================================================================================#
def alterar_Cliente(dicionario):
    if len(dicionario)==0:
        print("Não há clientes cadastrados")
    else:
        print('ALTERAÇÃO DE CADASTRO INICIALIZADA')
        cpf=input("Digite o CPF do cliente:")
        if existe_cliente(dicionario,cpf):
            chave=cpf
            menu1=True
            while menu1:
                menuAlteracaoCliente()
                opc=input("Escolha uma opção:")
                if opc=="1":
                    cpf=input("Digite o novo cpf:")
                    if existe_cliente(dicionario,cpf):
                        print("Pessoa já cadastrada, POR FAVOR DIGITE OUTRO CPF")
                    else:
                        dicionario[cpf]=dicionario[chave]
                        del dicionario[chave]
                        chave=cpf
                        print("Exclusão Realizada!!")
                        
                elif opc=="2":
                     nome=input("Digite o novo nome:")
                     dicionario[chave][0]=nome
                     print("Alteração feita!!!")
                     
                elif opc=="3":
                     rua=input("Digite a nova rua:")
                     dicionario[chave][1]=rua
                     print("Alteração feita!!!")
                     
                elif opc=="4":
                     numero=input("Digite o novo número:")
                     dicionario[chave][2]=numero
                     
                elif opc=="5":
                     bairro=input("Digite o novo bairro:")
                     dicionario[chave][3]=bairro
                     print("Alteração feita!!!")
                     
                elif opc=="6":
                     cidade=input("Digite a nova cidade:")
                     dicionario[chave][4]=cidade
                     print("Alteração feita!!!")
                     
                elif opc=="7":
                     estado=input("Digite o novo estado:")
                     dicionario[chave][5]=estado
                     print("Alteração feita!!!")
                     
                elif opc=="8":
                     telefone=input("Digite o novo telefone:")
                     dicionario[chave][6]=telefone
                     print("Alteração feita!!!")
                     
                elif opc=="9":
                     email=input("Digite o novo e-mail:")
                     dicionario[chave][7]=email
                     print("Alteração feita!!!")
                     
                else:
                    menu1=False
        else:
            print("Usuário não encontrado")

def alterar_Plano(dicionario):
    if len(dicionario)==0:
        print("Não há clientes cadastrados")
    else:
        print('ALTERAÇÃO DE PLANO INICIALIZADA')
        cod=int(input("Digite o Código do plano:"))
        if existe_plano(dicionario,cod):
            chave=cod
            menu2=True
            while menu2:
                menuAlteracaoPlano()
                opc=input("Escolha uma opção:")
                if opc=="1":
                    cod=int(input("Digite o novo código:"))
                    if existe_cliente(dicionario,cod):
                        print("Plano já cadastrado, POR FAVOR DIGITE OUTRO CÓDIGO")
                    else:
                        dicionario[cod]=dicionario[chave]
                        del dicionario[chave]
                        chave=cod
                        
                elif opc=="2":
                    tipo=input("Digite o novo Tipo de Plano:")
                    valor=(tipo,)+ dicionario[chave][1:]
                    dicionario[chave]=valor
                    print("Alteração feita!!!")
                elif opc=="3":
                    valormensal=float(input("Digite o novo Valor Mensal: "))
                    valor=dicionario[chave][0:1]+(valormensal,)+ dicionario[chave][2:]
                    dicionario[chave]=valor
                    print("Alteração feita!!!")
                elif opc=="4":
                    lista_recursos=[]
                    rec=input("Digite o recurso:")
                    while rec != "":
                        recursos=[]
                        recursos.append(rec)
                        qtd=input("Digite a quantidade:")
                        recursos.append(int(qtd))
                        valor=input("Digite o valor:")
                        recursos.append(float(valor))
                        rec=input("Digite o recurso:")
                        lista_recursos.append(recursos)
                    valor=dicionario[chave][0:2]+(lista_recursos,)+ dicionario[chave][3:]
                    dicionario[chave]=valor
                    print("Alteração feita!!!")
                else:
                    menu2=False
        else:
            print("Plano não Encontrado !!!")

def alterar_Consumo(dicionariocliente,dicionarioplano,dicionarioconsumo,cpf,cod,chave):
    print("ALTERAÇÃO DO CONSUMO INICIALIZADA")
    menu3= True
    while menu3:
        menuAlteracaoConsumo()
        opc=input("Escolha uma opção:")
        if opc=="1":
            cpf=input("Digite o novo cpf:")
            cod=int(input("Digite o novo cod:"))
            chave2=(cpf,cod)
            if existe_consumo(dicionariocliente,dicionarioplano,cpf,cod):
                dicionarioconsumo[chave2]=dicionarioconsumo[chave]
                del dicionarioconsumo[chave]
                chave=chave2
                print("Alteração feita!!!")
            else:
                print("O Usúario precisa estar Cadastrado !")
        elif opc=="2":
            datanasc=input("Digite a nova data de nascimento(DD/MM/AAAA):")
            dicionarioconsumo[chave][0]=datanasc
            print("Alteração feita!!!")
        elif opc=="3":
            lista_rec_consumido=[]
            rec=input("Digite o novo recurso:")
            while rec !="":
                rec_consumido=[]
                rec_consumido.append(rec)
                qtde=int(input("Digite a nova quantidade:"))
                rec_consumido.append(qtde)
                rec=input("Digite o novo recurso:")
                lista_rec_consumido.append(rec_consumido)
            dicionarioconsumo[chave][1]=lista_rec_consumido
            print("Alteração feita!!!")
        elif opc=="4":
            menu3= False
            
    
#=============================================================================================#
def listarUmCliente(dicionario):
    if len(dicionario)==0:
        print("Não há usuarios cadastrados")
    else:
        cpf=input("Digite o cpf do usuário:")
        if existe_cliente(dicionario,cpf):
            for chave in dicionario:
                if chave==cpf:
                    print("Cpf:",cpf,'\n')
                    print("Nome:",dicionario[cpf][0],"Rua:",dicionario[cpf][1],"Nro:",dicionario[cpf][2],"Bairro:",dicionario[cpf][3])
                    print("Cidade:",dicionario[cpf][4],"Estado:",dicionario[cpf][5],"Telefone:",dicionario[cpf][6],"E-mail:",dicionario[cpf][7])
            
        else:
            print("Usuário não encontrado")

def listarUmPlano(dicionario):
    if len(dicionario)==0:
        print("Não há usuarios cadastrados")
    else:
        cod=int(input("Digite o código:"))
        if existe_plano(dicionario,cod):
            for chave in dicionario:
                if chave==cod:
                    print('\t'"Código:",cod,'\n')
                    print("Tipo de Plano:",dicionario[cod][0],"Valor Mensal Básico:",dicionario[cod][1])
                    for i in range(len(dicionario[cod][2])):
                        print("Recurso:",dicionario[cod][2][i][0], "Quantidade:",dicionario[cod][2][i][1], "Valor:",dicionario[cod][2][i][2] )
        else:
            print("Plano não encontrado !!!")

def listarUmConsumo(dicionario,chave):
    for x in dicionario:
        if x==chave:
            print("Cpf",chave[0],"Código:",chave[1])
            print("Data Nascimento:", dicionario[chave][0])
            for i in range(len(dicionario[chave][1])):
                print("Recurso Consumido:",dicionario[chave][1][i][0], " Quantidade:",dicionario[chave][1][i][1]) 
    

#=============================================================================================#
def listarTodosCliente(dicionario):
    if len(dicionario)==0:
        print("Não há usuarios cadastrados")
    else:
        for chave in dicionario:
            print('\n')
            print("Cpf:",chave)
            print("Nome:",dicionario[chave][0],"Rua:",dicionario[chave][1],"Nro:",dicionario[chave][2],"Bairro:",dicionario[chave][3])
            print("Cidade:",dicionario[chave][4],"Estado:",dicionario[chave][5],"Telefone:",dicionario[chave][6],"E-mail:",dicionario[chave][7],'\n')

def listarTodosPlano(dicionario):
    if len(dicionario)==0:
        print("Não há usuarios cadastrados")
    else:
        for chave in dicionario:
            print('\n')
            print("Código:",chave)
            print("Tipo de Plano:",dicionario[chave][0],"Valor Mensal Básico:",dicionario[chave][1])
            for i in range(len(dicionario[chave][2])):
                print("Recurso:",dicionario[chave][2][i][0], "Quantidade:",dicionario[chave][2][i][1], "Valor:",dicionario[chave][2][i][2])


def listarTodosConsumo(dicionario):
    for chave in dicionario:
        print('\n')
        print("Cpf:", chave[0], " Código:", chave[1])
        print("Data Nascimento:", dicionario[chave][0])
        for i in range(len(dicionario[chave][1])):
                print("Recurso Consumido:",dicionario[chave][1][i][0], " Quantidade:",dicionario[chave][1][i][1]) 
        
                
#=============================================================================================#
def excluir_Cliente(dicionario,cpf):
    if len(dicionario)==0:
        print("Não há usuarios cadastrados")
    else: 
        if existe_cliente(dicionario,cpf):
            opc=input("\nConfirma a exclusão do médico (S/N)?")
            if opc.upper()=="S":
                del dicionario[cpf]
                
                print("Usuário removido com sucesso!")
        else:
            print("CPF não encontrado")

def excluir_Plano(dicionario,cod):
    if len(dicionario)==0:
        print("Não há usuarios cadastrados")
    else:
        print(cod)
        if existe_plano(dicionario,cod):
            opc=input("\nConfirma a exclusão do médico (S/N)?")
            if opc.upper()=="S":
                del dicionario[cod]
                print("Usuário removido com sucesso!")
        else:
            print("Código nao encontrado")

def excluir_Consumo(dicionario,chave):
    opc=input("\nConfirma a exclusão do médico (S/N)?")
    if opc.upper()=="S":
        del dicionario[chave]
        print("Consumo removido com sucesso!")
            
#=============================================================================================#
def relatorio1(dicionario):
#Mostrar os dados dos planos que possuam maior variedade de recursos disponíveis
    if len(dicionario)==0:
        print("Não existe planos cadastrados")
    else:
        
        maior=0
        for chave in dicionario:
            if int(len(dicionario[chave][2]))>maior:
                maior=len(dicionario[chave][2])
                
        # Empate  
        chaves=[]
        for i in dicionario:
            if len(dicionario[i][2]) == maior:
                chaves.append(i)

        for z in chaves:
            print('\t'"Código:",z,'\n')
            print("Tipo de Plano:",dicionario[z][0],"Valor Mensal Básico:",dicionario[z][1])
            for i in range(len(dicionario[z][2])):
                print("Recurso:",dicionario[z][2][i][0], "Quantidade:",dicionario[z][2][i][1], "Valor:",dicionario[z][2][i][2] )


        
def relatorio2(dicionario):
#Mostrar os dados de um plano a partir do tipo de plano informado pelo usuário;
    if len(dicionario)==0:
        print("Não existe planos cadastrados")
    else:
        plano=input("Informe o plano:")
        chaves=[]
        for chave in dicionario:
            if dicionario[chave][0]==plano:
                chaves.append(chave)
                
        for z in chaves:
            print('\t'"Código:",z,'\n')
            print("Tipo de Plano:",dicionario[z][0],"Valor Mensal Básico:",dicionario[z][1])
            for i in range(len(dicionario[z][2])):
                print("Recurso:",dicionario[z][2][i][0], "Quantidade:",dicionario[z][2][i][1], "Valor:",dicionario[z][2][i][2] )
        




    

def relatorio3(diccliente,dicconsumo):
        lista=[]
        nome=input("Informe o nome do cliente:")
        for z in diccliente:
            if diccliente[z][0]==nome:
                lista.append(z)
                    
        lista2=[]
        for chave in dicconsumo:
            if chave[0]==lista[0]:
                i=chave
                lista2.append(i)

        for h in lista2:
            print("Cpf",h[0],"Código:",h[1])
            print("Data Nascimento:", dicconsumo[h][0])
            for z in range(len(dicconsumo[h][1])):
                print("Recurso Consumido:",dicconsumo[h][1][z][0], " Quantidade:",dicconsumo[h][1][z][1])





#================================================================================================#

def main():
    
    dc_clientes={}
    dc_planos={}
    dc_consumo={}
    

    if os.path.exists('clientes.txt'):
        le_arquivoCliente(dc_clientes)
        print("Leitura clientes.txt feita com sucesso !")
    if os.path.exists('planos.txt'):
        le_arquivoPlano(dc_planos)
        print("Leitura de planos.txt feita com sucesso !")
    if os.path.exists('consumos.txt'):
        le_arquivoConsumo(dc_consumo)
        print("Leitura de consumos.txt feita com sucesso !")

        

    menu=True
    while menu:
        mostrarmenu()
        opc=input("\nEscolha uma opção: ")
        if opc=="1":
            menupessoas=True
            while menupessoas:
                submenuClientes()
                opc=input("\nEscolha uma opção: ")
                if opc=="1":
                    print("Listar todos")
                    listarTodosCliente(dc_clientes)
                
                elif opc=="2":
                    print("Listar um")
                    listarUmCliente(dc_clientes)

                elif opc=="3":
                    print("Incluir")
                    cadastro_Cliente(dc_clientes)
                    
                elif opc=="4":
                    print("Alterar")
                    alterar_Cliente(dc_clientes)
                
                elif opc=="5":
                    print("Excluir")
                    cpf=input("Digite o cpf:")
                    excluir_Cliente(dc_clientes,cpf)
                    

                else:
                    print("\nVoltando para o Menu Principal")
                   
                    menupessoas=False
                
        elif opc=="2":
            menuplanos=True
            while menuplanos:
                submenuPlanos()
                opc=input("\nEscolha uma opção: ")
                if opc=="1":
                    print("Listar todos")
                    listarTodosPlano(dc_planos)
                    
                elif opc=="2":
                    print("Listar um")
                    listarUmPlano(dc_planos)

                elif opc=="3":
                    print("Incluir")
                    cadastro_Plano(dc_planos)

                elif opc=="4":
                    print("Alterar")
                    alterar_Plano(dc_planos)
                    
                elif opc=="5":
                    print("Excluir")
                    cod=int(input("Digite o código:"))
                    excluir_Plano(dc_planos,cod)
                    
                else:
                    print("\nVoltando para o Menu Principal")
                    
                    menuplanos=False
                    
        elif opc=="3":
            menuconsumo=True
            while menuconsumo:
                submenuConsumo()
                opc=input("\nEscolha uma opção: ")
                if opc=="1":
                    print("Listar todos")
                    listarTodosConsumo(dc_consumo)
                    
                elif opc=="2":
                    print("Listar um")
                    cpf=input("Digite o cpf:")
                    cod=int(input("Digite o código:"))
                    if existe_consumo(dc_clientes,dc_planos,cpf,cod):
                        chave=(cpf,cod)
                        listarUmConsumo(dc_consumo,chave)
                    else:
                        print("CPF ou o CÓDIGO nao estão cadastrados")
                    

                elif opc=="3":
                    print("Incluir")
                    cpf=input("Digite o cpf:")
                    cod=int(input("Digite o código:"))
                    if existe_consumo(dc_clientes,dc_planos,cpf,cod):
                        chave=(cpf,cod)
                        cadastro_Consumo(dc_consumo,dc_planos,cpf,cod,chave)
                    else:
                        print("CPF ou o CÓDIGO nao estão cadastrados")

                elif opc=="4":
                    print("Alterar")
                    cpf=input("Digite o cpf:")
                    cod=int(input("Digite o código:"))
                    if existe_consumo(dc_clientes,dc_planos,cpf,cod):
                        chave=(cpf,cod)
                        alterar_Consumo(dc_clientes,dc_planos,dc_consumo,cpf,cod,chave)
                    else:
                        print("CPF ou o CÓDIGO nao estão cadastrados")
                    
                elif opc=="5":
                    print("Excluir")
                    cpf=input("Digite o cpf:")
                    cod=int(input("Digite o código:"))
                    if existe_consumo(dc_clientes,dc_planos,cpf,cod):
                        chave=(cpf,cod)
                        excluir_Consumo(dc_consumo,chave)
                    else:
                        print("CPF ou o CÓDIGO nao estão cadastrados")
                else:
                    print("\nVoltando para o Menu Principal")
                
                    menuconsumo=False
                    
        elif opc=="4":
            menurelatorios=True
            while menurelatorios:
                submenuRelatorio()
                opc=input("\nEscolha uma opção dos Relatórios:")
                if opc=="1":
                    print("1- Mostrar os dados dos planos que possuam maior variedade de recursos disponíveis;")
                    relatorio1(dc_planos)
        
                elif opc=="2":
                    print("Relatório 2")
                    print("Mostrar os dados de um plano a partir do tipo de plano informado pelo usuário;")
                    relatorio2(dc_planos)
                    
                elif opc=="3":
                    print("Relatório 3")
                    print("Mostrar todas as informações dos planos já contratados por um cliente, a partir do nome do cliente informado pelo usuário;")
                    relatorio3(dc_clientes,dc_consumo)
                    
                    
                else:
                    print("\nVoltando para o Menu Principal")
                    menurelatorios=False
        else:
            print("\nTerminando a execução do programa!!!")
            print("Gravamento Realizado !")
            grava_Cliente(dc_clientes)
            grava_Plano(dc_planos)
            grava_Consumo(dc_consumo)
            menu=False

main()
        
