import json
import calendar
from datetime import datetime

def salvar_livro(livro):
    try:
        with open('livros_biblioteca.json', 'r') as f:
            livros_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        livros_data = []

    livro['data_cadastro'] = datetime.now().strftime('%d %B %Y')
    livros_data.append(livro)

    with open('livros_biblioteca.json', 'w') as f:
        json.dump(livros_data, f, indent=4)
    print("\nlivro cadastrado com sucesso!")

def exibir_livros():
    try:
        with open('livros_biblioteca.json', 'r') as f:
            livros_data = json.load(f)
        if livros_data:
            print("\nlivros cadastrados:")
            for livro in livros_data:
                print(f"\ntítulo: {livro['titulo']}")
                print(f"autor: {livro['autor']}")
                print(f"ano de publicação: {livro['ano_publicacao']}")
                print(f"número de páginas: {livro['numero_paginas']}")
                print(f"categoria: {livro['categoria']}")
                print(f"data de cadastro: {livro['data_cadastro']}")
        else:
            print("\nnenhum livro cadastrado ainda.")
    except FileNotFoundError:
        print("\nAinda não há livros cadastrados.")

def validar_ano_publicacao(ano):
    try:
        ano = int(ano)
        if ano > 0:
            return ano
        else:
            print("o ano deve ser um número positivo.")
            return None
    except ValueError:
        print("por favor, insira um ano válido.")
        return None

def validar_numero_paginas(paginas):
    try:
        paginas = int(paginas)
        if paginas > 0:
            return paginas
        else:
            print("o número de páginas deve ser maior que zero.")
            return None
    except ValueError:
        print("por favor, insira um número válido para as páginas.")
        return None

def cadastrar_livro():
    print("\ncadastro de novo livro:")

    titulo = input("título do livro: ")
    autor = input("autor do livro: ")

    while True:
        ano_publicacao = input("ano de publicação: ")
        ano_publicacao = validar_ano_publicacao(ano_publicacao)
        if ano_publicacao:
            break

    while True:
        numero_paginas = input("número de páginas: ")
        numero_paginas = validar_numero_paginas(numero_paginas)
        if numero_paginas:
            break

    categoria = input("categoria do livro (ex: ficção, romance, tecnologia, etc.): ")

    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano_publicacao": ano_publicacao,
        "numero_paginas": numero_paginas,
        "categoria": categoria
    }

    salvar_livro(livro)

def consultar_calendario():
    ano = datetime.now().year
    mes = datetime.now().month
    mes_nome = calendar.month_name[mes]
    print(f"\ncalendário de {mes_nome} {ano}:")
    print(calendar.month(ano, mes))

def menu():
    while True:
        print("\nmenu:")
        print("1 - cadastrar novo livro")
        print("2 - exibir livros cadastrados")
        print("3 - consultar calendário")
        print("4 - sair")
        
        opcao = input("escolha uma opção: ")

        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            exibir_livros()
        elif opcao == '3':
            consultar_calendario()
        elif opcao == '4':
            print("saindo...")
            break
        else:
            print("opção inválida, tente novamente.")

menu()