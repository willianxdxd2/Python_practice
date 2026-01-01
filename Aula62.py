lista=[]
while True:
    
    print('selecione uma opção')
    opcao=input('digite [i]nserir [a]pagar [l]istar: ')
    if opcao == 'i':
        
        valor=input('Valor:')
        lista.append(valor)
        
    elif opcao == 'a':
        indice_string=input('escolha um valor para apagar')
        indice=int(indice_string)
        del lista[indice]
    elif opcao == 'l':
        
        if len(lista) == 0:
            print('nada para listar')
        for i, valor in enumerate(lista):
            print(i,valor)
    else:
        print('escolha uma das opções válidas')