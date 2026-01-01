"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x,y,z):
    print(f'{x=} y={y} {z=}' ,  '/'  'x + y + z =', x+y+z)
    
soma(1,2,3)
soma(4,6,7)
soma(7,y=9,z=10)
soma(x=10,y=30,z=40)