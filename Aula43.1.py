


while True:
    
    
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador(+-*/): ')
    
    numero_valido=None
    numero_1_float=0
    numero_2_float=0
    try:
        numero_1_float=float(numero_1)
        numero_2_float=float(numero_2)
        numero_valido=True
    
    except:
        numero_valido=None
    if numero_valido is None:
        print('Um ou ambos os numeros digitados não são válidos')
        continue
    
    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('digite apenas um operador')
        continue
    
    
     
    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float}' , numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'A sua conta de {numero_1_float} - {numero_2_float} resulta em' , numero_1_float - numero_2_float)
    elif operador == '*':
        print(f'A sua conta de {numero_1_float} * {numero_2_float} resulta em' , numero_1_float * numero_2_float)
    elif operador == '/':
        print(f'A sua conta de {numero_1_float} / {numero_2_float} resulta em' , numero_1_float / numero_2_float)
    else:
        print('erro')
    sair=input('Se deseja sair aperte s: ').lower().startswith('s')
    
    if sair == True:
        break