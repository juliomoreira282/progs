import os

uploads = []
historico = []
seguidores = ["@monty_python", "@pinguim", "@dev_crustaceo"]

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar_arquivo(arquivo: str):
    uploads.append(arquivo.capitalize())
    print(f"{arquivo} foi adicionado.")
    mostrar_uploads()
    
def postar_arquivo():
    arquivo_postado = uploads.pop(0)
    print(f"{arquivo_postado} foi postado.")
    mostrar_uploads()

def mostrar_uploads():
    print(f"Qtde. de itens na fila de uploads: {len(uploads)} | Fila de uploads: {uploads}")

def adicionar_ao_historico(add_historico: str):
    historico.append(add_historico.capitalize())
    print(f"{add_historico} foi adicionado ao histórico.")
    mostrar_historico()

def desfazer():
    undo = historico.pop()
    print(f"Usuário apertou desfazer... Item removido: {undo}")
    mostrar_historico()

def mostrar_historico():
    print(f"Itens no histórico: {len(historico)} | Histórico: {historico}")

def adicionar_seguidor(add_seguidor: str):
    if add_seguidor.startswith('@'):
        seguidores.append(add_seguidor)
        print(f"{add_seguidor} foi adicionado.")
        mostrar_seguidores()
    
    else:
        print("Não se esqueça do '@' antes do nome de usuário.")

def adicionar_seguidor_vip(add_seguidor_vip: str):
    if add_seguidor_vip.startswith('@'):    
        seguidores.insert(0, add_seguidor_vip)
        print(f"Seja bem-vindo! {add_seguidor_vip}!")
        mostrar_seguidores()
    
    else:
        print("Lamentamos informar, mas você se esqueceu do '@'.")

def banir(banir_usuario: str):
    if banir_usuario not in seguidores:
        raise ValueError(f"O usuário {banir_usuario} não existe.")
    seguidores.remove(banir_usuario)
    mostrar_seguidores()

def mostrar_seguidores():
    print(f"Quantidade de seguidores: {len(seguidores)} | Seguidores: {seguidores}")

def main():
    print("\nMenu de Comandos:")
    print("Digite 'U' para adicionar algo à fila de uploads.")
    print("Digite 'H' para adicionar algo à pilha do histórico.")
    print("Digite 'P' para postar algo que esteja na fila de uploads.")
    print("Digite 'Z' para desfazer algo da pilha do histórico.")
    print("Digite 'A' para adicionar um usuário à lista de seguidores da forma normal.")
    print("Digite 'V' para adicionar um usuário VIP à lista.")
    print("Digite 'B' para banir um usuário.")
    print("Digite 'C' para verificar o estado de cada uma das listas.") 
    print("Digite 'S' para sair.")

    while True:
        try:    
            cmd = input("Digite um comando: ").strip()

            if cmd.lower() == 's':
                print("Encerrando...")
                break

            elif cmd.lower() == 'u':
                add_arquivo = input("Qual arquivo deseja adicionar? \n")
                adicionar_arquivo(add_arquivo)

            elif cmd.lower() == 'p':
                postar_arquivo()

            elif cmd.lower() == 'h':
                add_hist = input("Qual item deseja adicionar ao histórico? \n")
                adicionar_ao_historico(add_hist)

            elif cmd.lower() == 'z':
                desfazer()

            elif cmd.lower() == 'a':
                add_seg = input("Qual seu nome de usuário? Não se esuqeça do '@'. \n")
                adicionar_seguidor(add_seg)

            elif cmd.lower() == 'v':
                add_seg_vip = input("Qual seu nome de usuário, Sr. Usuário VIP? Use o '@' antes do nome de usuário. \n")
                adicionar_seguidor_vip(add_seg_vip)

            elif cmd.lower() == 'b':
                ban_user = input("Qual usuário deseja banir? \n")
                banir(ban_user)

            elif cmd.lower() == 'c':
                mostrar_uploads()
                mostrar_historico()
                mostrar_seguidores()

            else:
                print("O comando não existe. Tente novamente.")

        except IndexError:
            print("A lista está vazia, tente novamente.")

if __name__ == "__main__":
    main()