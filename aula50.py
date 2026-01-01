import os
palavra_secreta='perfume'
letras_acertadas=''
num_tentativa = 0
while True:
    letra_digitada=input('Digite apenas uma letra: ')
    num_tentativa += 1
    if len(letra_digitada) > 1:
        print('digite apenas uma letra.')
        continue
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    print(letras_acertadas)
    palavra_formada=''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
            print(letra_secreta )
        else:
            palavra_formada += '*'
            
    print('palavra formada: ',palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Você ganhou Parabens!!1!')
        print('a palavra era:',palavra_secreta)
        print('tentativas: ' , num_tentativa)
        letras_acertadas=''
        num_tentativa = 0
        