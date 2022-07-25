
cinema=[]
nomefilme=input("Nome do Filme:")
while nomefilme!= "":
    filmes=[]
    atores=[]
    lista=[]
    salaehorarios=[]
    salas=[]
    filmes.append(nomefilme)
    ano=input("Ano lançamento:")
    filmes.append(int(ano))
    nomeatores=input("Atores:")
    while nomeatores != "":
        atores.append(nomeatores)
        nomeatores=input("Atores:")
    sala=input("Sala:")
    while sala!="":
        salas.append(sala)
        horarios=[]
        hora=input("Horário:")
        while hora != "":
            horarios.append(hora)
            hora=input("Horário:")
        salas.append(horarios)
        sala=input("Sala:")
    lista.append(salas)
    filmes.append(atores)
    cinema.append(filmes)
    cinema.append(salas)
    nomefilme=input("Nome do Filme:")

#b) O nome dos filme com maior quantidade de atores;









