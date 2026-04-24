class UploadManagement:
    def __init__(self):
        self.uploads = []

    def adicionar_arquivo(self, arquivo: str):
        self.uploads.append(arquivo.capitalize())
        print(f"{arquivo} foi adicionado.")

    def postar_arquivo(self):
        arquivo_postado = self.uploads.pop(0)
        print(f"{arquivo_postado} foi postado.")

    def mostrar_lista_uploads(self):
        print(f"Qtde. de arquivos em espera: {len(self.uploads)} | Arquivos em espera: {self.uploads}")

class HistoryManagement:
    def __init__(self):
        self.historico = []

    def adicionar_ao_historico(self, add_historico: str):
        self.historico.append(add_historico.capitalize())

    def desfazer(self):
        undo = self.historico.pop()
        print(f"Usuário apertou desfazer... Item removido: {undo}")
    
    def mostrar_historico(self):
        print(f"Qtde. de itens no histórico: {len(self.historico)} | Histórico: {self.historico}")

class FollowerManagement:
    def __init__(self):
        self.seguidores = ["@monty_python", "@system_out._println", "@dev_crustaceo"]

    def adicionar_seguidor(self, add_seguidor: str):
        if add_seguidor.startswith('@'):
            self.seguidores.append(add_seguidor)
            print(f"{add_seguidor} foi adicionado.")
        
        else:
            print("Não se esqueça de usar o '@' antes do nome de usuário.")

    def adicionar_seguidor_vip(self, add_seguidor_vip: str):
        if add_seguidor_vip.startswith('@'):
            self.seguidores.insert(0, add_seguidor_vip)
            print(f"Seja bem-vindo! {add_seguidor_vip}!")
        
        else:
            print("Lamentamos informar, mas você se esqueceu do '@' antes do nome de usuário.")

    def banir(self, banir_usuario):
            if banir_usuario not in self.seguidores:
                raise ValueError(f"O usuário {banir_usuario} não está na lista.")
            
            self.seguidores.remove(banir_usuario)
            print(f"{banir_usuario} foi banido, não tem espaço pra você aqui.")

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
            add_arquivo = input("Qual arquivo deseja adicionar? \n")          
            upl.adicionar_arquivo(add_arquivo)
            upl.mostrar_lista_uploads()

        elif comando == 'p':
            upl.postar_arquivo()
            upl.mostrar_lista_uploads()

        elif comando == 'h':
            add_his = input("O que deseja adicionar ao histórico? \n")
            his.adicionar_ao_historico(add_his)
            his.mostrar_historico()

        elif comando == 'z':
            his.desfazer()
            his.mostrar_historico()

        elif comando == 'a':
            add_seg = input("Qual o nome de usuário? Não se esqueça de usar o '@'. \n")
            seg.adicionar_seguidor(add_seg)
            seg.mostrar_seguidores()

        elif comando == 'v':
            add_seg_vip = input("Qual seu nome de usuário, Sr. Usuário VIP?")
            seg.adicionar_seguidor_vip(add_seg_vip)
            seg.mostrar_seguidores()

        elif comando == 'b':
            ban_seg = input("Qual usuário deseja banir? \n")
            seg.banir(ban_seg)
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