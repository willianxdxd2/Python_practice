"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

verdadeiro = True

while verdadeiro:
    nome=input('vou te perguntar varias vezes pq vc é burro, qual seu nome? ')
    print(f'meu nome é {nome}')
    if nome == 'sair':
        break
print ('acabou')