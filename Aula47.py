texto ='Willian'
iterador=iter(texto)
while True:
    try:
        nex=next(iterador)
        print(nex)
    except StopIteration:
        break
    
    