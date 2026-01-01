"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
digito=9
#novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)