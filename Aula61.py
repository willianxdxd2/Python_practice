
lista=[]
while True:
    
    try:
        entrada=input('você deseja (i)nserir (a)pagar (l)istar (s)air: ').lower()
        if entrada == 's':
            break
        
        if entrada == 'i':
            inserir = input('oq vc deseja inserir: ')
            print(inserir)
        
        lista.append(inserir)
        print(lista)
        
        
        if entrada == 'a':
            print('a')
            
        if entrada == 'l':
            for item , nome in enumerate(lista):
                print(item, nome)
                
        
        
        
    except:
        print('erro')