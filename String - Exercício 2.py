
palavra=input('Digite uma palavra:')
letra=input('Digite uma letra que será removida:')
str_sem_letra=""
for z in palavra:
    if z not in letra:
        str_sem_letra=str_sem_letra+z
print(str_sem_letra)
    
