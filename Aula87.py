# Manipulando chaves e valores em dicionários
pessoa = {}
chave= 'nome_completo'
pessoa[chave] = 'Luiz Otávio'

print(pessoa[chave])
print(pessoa['nome'])
pessoa['sobrenome']='Miranda'
pessoa[chave]='maria'

del pessoa ['sobrenome']