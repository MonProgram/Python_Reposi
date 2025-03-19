#atividade 29

def exibir_menu():
    print("Bem-vindo! Ao menu de Login")
    print("1 - Cadastrar")
    print("2 - Logar")
    print("3 - Sair")
    print("---------------------------------")

def cadastrar_pessoa (cadastros):
    nome = input("seu nome:")
    idade = input("sua idade:")
    turma = input("sua turma:")
    curso = input("seu curso:")
    cadastros.append({"nome": nome, "idade": idade, "turma": turma, "curso": curso})
    print("cadastro realizado com sucesso bruhhhh")

def ver_cadastros (cadastros):
    if not cadastros:
        print("Não há cadastros, tem certeza que fez certo?")
    else:
        print("\n ------ Lista de Cadastros ------")
        
        for i, pessoa in enumerate (cadastros, 1):
            print(f"{i}.nome: {pessoa ['nome']}, idade: {pessoa ['idade']}, turma: {pessoa ['turma']}, curso: {pessoa[''
            'curso']}")
                  

def main():
    cadastros = []
    while True:
        exibir_menu()
        opção = input("Escolha uma opção: ")
        if opção == "1":
            cadastrar_pessoa (cadastros)
        elif opção == "2":
            ver_cadastros (cadastros)

        elif opção == "3":
            print("Volte sempre! Obrigado por utilizar nosso sistema xDD")
            break
            
        else:
            print("poh cara, acho que não é isso.")

if __name__ == "__main__":
    main()
