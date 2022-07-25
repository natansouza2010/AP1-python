

palavra=input('Digite uma palavra:').lower()
inverso=""
for z in range(len(palavra)-1,-1,-1):
    inverso= inverso + palavra[z]
if inverso==palavra:
    print('A palavra',palavra,'é palíndroma') 
else:
    print('A palavra',palavra,'não é palíndroma') 
