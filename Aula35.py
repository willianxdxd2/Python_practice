"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#print(len(Entrada))
entrada = input('Coloque o seu nome aqui: ')
quantidade = len(entrada)
if quantidade >= 1:
    if quantidade <= 4:
        print('pequeno')
    elif quantidade >= 5 and quantidade <=6:
        print('médio')
    else:
        print('grande')
else:
    print('digite algo maior')