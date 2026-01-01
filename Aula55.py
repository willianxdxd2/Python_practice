"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
Lista_a=['Luiz','Maria']
lista_b = Lista_a.copy()

Lista_a[0]= 'qualquercoisa'
print(lista_b)