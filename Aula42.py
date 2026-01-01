"""
Iterando strings com while
"""
nome='joão pascal de souza'
indice=0
botar_na_string=''
while indice < len(nome):
    letra = nome[indice]
    botar_na_string += f'*{letra}'
    indice +=1

    
    
print(botar_na_string)