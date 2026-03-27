class UploadManagement:
    def __init__(self):
        self.uploads = []

    def adicionar_arquivo(self):
        arquivo = input("Qual arquivo deseja adicionar? \n")
        self.uploads.append(arquivo.capitalize())

    def postar_arquivo(self):
        arquivo_postado = self.uploads.pop(0)
        print(f"{arquivo_postado} foi postado.")

    def mostrar_lista_uploads(self):
        print(f"Qtde. de arquivos em espera: {len(self.uploads)} | Arquivos em espera: {self.uploads}")

class HistoryManagement:
    def __init__(self):
        self.historico = []

    def adicionar_ao_historico(self):
        add_historico = input("Qual item deseja adicionar ao histórico? \n")
        self.historico.append(add_historico.capitalize())

    def desfazer(self):
        undo = self.historico.pop()
        print(f"Usuário apertou desfazer... Item removido: {undo}")
    
    def mostrar_historico(self):
        print(f"Qtde. de itens no histórico: {len(self.historico)} | Histórico: {self.historico}")

class FollowerManagement:
    def __init__(self):
        self.seguidores = ["@monty_python", "@system_out._println", "@dev_crustaceo"]

    def adicionar_seguidor(self):
        add_seguidor = input("Qual usuário deseja adicionar? Use o '@' antes do nome de usuário. \n")
        self.seguidores.append(add_seguidor)
        print(f"{add_seguidor} foi adicionado.")

    def adicionar_seguidor_vip(self):
        add_seguidor_vip = input("Qual seu nome de usuário, Sr. Usuário VIP? Não se esqueça do '@' antes do nome de usuário. \n")
        self.seguidores.insert(0, add_seguidor_vip)
        print(f"Seja bem-vindo! {add_seguidor_vip}")

    def banir(self):
        try:    
            banir_usuario = input("Qual usuário deseja banir? \n")
            if banir_usuario not in self.seguidores:
                raise ValueError(f"O usuário {banir_usuario} não está na lista.")
            self.seguidores.remove(banir_usuario)

        except ValueError as ve:
            print(f"Erro. {ve}")

    def mostrar_seguidores(self):
        print(f"Qtde. de seguidores: {len(self.seguidores)} | Seguidores: {self.seguidores}")

upl = UploadManagement()
his = HistoryManagement()
seg = FollowerManagement()

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
        comando = input("Digite um comando: ").strip().lower()

        if comando == 's':
            print("Encerrando...")
            break

        elif comando == 'u':
            upl.adicionar_arquivo()
            upl.mostrar_lista_uploads()

        elif comando == 'p':
            upl.postar_arquivo()
            upl.mostrar_lista_uploads()

        elif comando == 'h':
            his.adicionar_ao_historico()
            his.mostrar_historico()

        elif comando == 'z':
            his.desfazer()
            his.mostrar_historico()

        elif comando == 'a':
            seg.adicionar_seguidor()
            seg.mostrar_seguidores()

        elif comando == 'v':
            seg.adicionar_seguidor_vip()
            seg.mostrar_seguidores()

        elif comando == 'b':
            seg.banir()
            seg.mostrar_seguidores()

        elif comando == 'c':
            upl.mostrar_lista_uploads()
            his.mostrar_historico()
            seg.mostrar_seguidores()

        else:
            print("O comando não existe. Tente novamente.")

    except IndexError:
        print("A lista está vazia. Tente novamente.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado. {e}")