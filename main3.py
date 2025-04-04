import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("\n ---- MENU CADASTRO ----")
    print("1 - Cadastrar pessoa")
    print("2 - Ver cadastros")
    print("3 - Sair")
    print("-------------------------")

def salvar_cadastros (cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8") as arquivos:
        json.dump(cadastros, arquivos, indent=4,  ensure_ascii=False)

def carregar_cadastros():
    try:
        with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def cadastrar_pessoa (cadastros):
    nome = input("seu nome:")
    idade = input("sua idade:")
    turma = input("sua turma:")
    curso = input("seu curso:")
    cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
    print("****cadastro realizado com sucesso bruhhhh****")

    '''Aham, paramos no dia 04/04/2025, na aula de reposição :d'''
    
