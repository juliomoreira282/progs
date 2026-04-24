import os

materias = {}
assuntos = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_principal():
    print("=" * 43)
    print("         DEVSTUDO - MENU PRINCIPAL")
    print("=" * 43)
    print("1. Cadastrar Matéria")
    print("2. Listar Matérias")
    print("3. Pesquisar Matéria")
    print("4. Excluir Matéria")
    print("5. Fechar Programa")
    print("=" * 43)

def cadastro_de_materia():
    materia = input("Qual o nome da matéria que deseja adicionar? \n").capitalize()
    nome_materia = materia.capitalize()
    limpar_tela()
        
    assunto = input("Qual assunto deseja adicionar? \n")
    assuntos.append(assunto.capitalize())
        
    while True:
        comando = int(input("Deseja adicionar outro assunto? (0 / 1) \n"))
            
        if comando == 1:
                assunto = input("Qual assunto deseja adicionar? \n")
                assuntos.append(assunto.capitalize())
                          
        elif comando == 0:
            materias[materia] = {
                "nome": nome_materia,
                "assuntos": assuntos 
            }
            break
        else:
            print("Comando inválido. Tente novamente.")

while True:
    menu_principal()
    comando = input("Escolha uma opção: ")
    if comando == '1':
        cadastro_de_materia()

    elif comando == '2':
        limpar_tela()
        for materia in materias:
            for assunto in assuntos:
                print(f"Matéria: {materia}")
                print(f"Assuntos: {assunto}")

    elif comando == '3':
        materia = input("Digite o nome de uma matéria: ")
        if materia.capitalize() in materias:
            print(f"Matéria: {materia} | Assuntos: {assuntos}")

        else:
            comando = int(input("Deseja cadastrar uma nova matéria? (0 / 1) \n"))
            if comando == 1:
                cadastro_de_materia()
            
            elif comando == 0:
                print("Voltando para a rotina normal.")
                limpar_tela()

    elif comando == '4':
        materia = input("Digite o nome de uma matéria: ")
        if materia.capitalize() in materias:
            comando = int(input("Tem certeza de que quer fazer isso? (0 / 1) \n"))

            if comando == 1:
                del materias[materia]
                print(f"Matéria {materia} deletada com sucesso.")

            elif comando == 0:
                print("Voltando à rotina normal.")
                limpar_tela()

            else:
                print("Comando inválido. Tente novamente.")

    elif comando == '5' or comando.lower() == 's':
        limpar_tela()
        print("Programa encerrado com sucesso")