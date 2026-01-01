"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
""" 
#10  9  8    7  6  5    4  3  2
#5  0  2  .  7  8  3 .  9  6  0-03
cpf=input('coloque os digitos antes do traço do cpf')
print(cpf)
cpf_limpo=cpf.replace('.','')

lista=[]
intervalo=range(10,1,-1)
for i, j in zip(cpf_limpo,intervalo):
    I_num=int(i)
    numeros=I_num*j
    print(numeros)
    lista.append(numeros)

soma_total = sum(lista)


print("Valores na lista:", lista)
print("Soma total dos valores na lista:", soma_total)

multi=soma_total*10
resto=multi%11
print(resto)

#oq eu aprendi que da pra colocar duas coisas ao mesmo tempo no for uma variavel ligando a cada uma 
#que existe a função sum para somar tudo
#a função zip para colocar os dois iteraveis do for
#a função replace para tirar algo indesejado e mudar oq vc quiser
#a usar lista de forma mais eficiente
#e a usar um pouco mais do range e faze-lo ser decrescente começando do 10 ir até o 1 e pulado de -1 em -1