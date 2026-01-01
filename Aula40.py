contador= 0
while contador <=100:
    contador += 1
    if contador >=56 and contador <=80:
        print ('não vou mostrar o', contador)
        continue
    print(contador)
    
    if contador == 100:
        print('chegou')