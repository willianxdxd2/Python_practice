"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver nan
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

#entrada=input('digite apenas uma letra:')
palavra='paralelepipedo'
#maior=len(entrada)
ten=0
letra_acertada='a letra é : '
while True :
    entrada=input('digite apenas uma letra:')
    maior=len(entrada)
    sair='sair'
    #sai do programa
    if entrada == sair:
            break
        #-----------------
        #permite entrada do programa com apenas uma letra
    if maior == 1:
        tent = 0
        soma = 1
        tent += soma
        print(f'tentativas: {tent}')
        print('(para sair digite sair)')
       #-------------------
       #diz ao usario se ele acertou a letra ou não
        if entrada in palavra:
            print('está')
            entrada += letra_acertada
            print(letra_acertada)
            continue
        
        else:
            print('não está dentro da palavra')
        
        #--------------------
            
    else:
        print('Você digitou mais de uma letra')