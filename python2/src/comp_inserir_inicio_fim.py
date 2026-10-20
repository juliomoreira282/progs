import random
import pickle
import os
import time
import string
import pygame as pg

arquivo_dados_placas = 'dados_placas.pkl'

def gerar_placas():
    letras_1 = "".join(random.choices(string.ascii_uppercase, k=3))
    numero_1 = str(random.randint(0, 9))
    letra_2 = random.choice(string.ascii_uppercase)
    numeros_2 = "".join(random.choices(string.digits, k=2))
    return f"{letras_1}{numero_1}{letra_2}{numeros_2}"

status_sistema = ""

if os.path.exists(arquivo_dados_placas):
    with open(arquivo_dados_placas, 'rb') as arquivo_bin:
        lista_caminhoes = pickle.load(arquivo_dados_placas)

else:
    tamanho_lista = 3000
    lista_caminhoes = []
    while len(lista_caminhoes) < tamanho_lista:
        placa = gerar_placas()
        if placa not in lista_caminhoes:
            lista_caminhoes.append(placa)

    with open(arquivo_dados_placas, 'wb') as arquivo_bin:
        pickle.dump(lista_caminhoes, arquivo_bin)

    status_sistema = f"{len(lista_caminhoes)} itens novos gerados."

pg.init()
largura, altura = 800, 600
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption("Comparação Inserir no Início x No Final")

fonte_titulo = pg.font.SysFont("arial", 26, bold=True)
fonte_texto = pg.font.SysFont("arial", 20)
fonte_entrada = pg.font.SysFont("courier new", 28, bold=True)

caixa_entrada = pg.Rect(50, 130, 200, 40)
btn_inicio = pg.Rect(280, 130, 200, 40)
btn_final = pg.Rect(500, 130, 200, 40)

cor_inativa = pg.Color(100, 100, 100)
cor_ativa = pg.Color(50, 150, 255)
cor_caixa = cor_inativa

ativo = False
texto_digitado = ""
resultado_tempo = "Aguardando ação..."
resultado_acao = ""

executando = True
while executando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            executando = False
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if caixa_entrada.collidepoint(event.pos):
                ativo = True
            else:
                ativo = False
            cor_caixa = cor_ativa if ativo else cor_inativa

            if btn_inicio.collidepoint(event.pos) and texto_digitado:
                nova_placa = texto_digitado.upper()

                inicio_t = time.perf_counter()
                lista_caminhoes.insert(0, nova_placa)
                fim_t = time.perf_counter()

                resultado_tempo = f"Tempo de inserção: {(fim_t - inicio_t):.9f} seg."
                resultado_acao = "Adicionado ao INÍCIO (O(n) - Todos os itens deslocados)"
                texto_digitado = ""

            if btn_final.collidepoint(event.pos) and texto_digitado:
                nova_placa = texto_digitado.upper()

                inicio_t = time.perf_counter()
                lista_caminhoes.append(nova_placa)
                fim_t = time.perf_counter()

                resultado_tempo = f"Tempo de inserção: {(fim_t - inicio_t):.9f} seg."
                resultado_acao = "Adicionado ao FINAL (O(1) - Adicionado no espaço livre)"
                texto_digitado = ""

        if event.type == pg.KEYDOWN:
            if ativo:
                if event.key == pg.K_BACKSPACE:
                    texto_digitado = texto_digitado[:-1]
                else:
                    if len(texto_digitado) < 7 and event.unicode.isalnum():
                        texto_digitado = event.unicode.upper()

    tela.fill((30, 30, 30))

    tela.blit(fonte_titulo.render("Comparador de Desempenho de Inserção", True, (255, 255, 255)), (50, 30))
    tela.blit(fonte_texto.render(status_sistema, True, (150, 150, 150)), (50, 70))
    tela.blit(fonte_texto.render("Digite uma placa: (Ex.: ABC1F23): ", True, (200, 200, 200)), (50, 105))
    
    pg.draw.rect(tela, cor_caixa, caixa_entrada, 2)
    superficie_texto = fonte_entrada.render(texto_digitado, True, (255, 255, 255))
    tela.blit(superficie_texto, (caixa_entrada.x + 10, caixa_entrada.y + 5))

    pg.draw.rect(tela, (60, 60, 60), btn_inicio)
    tela.blit(fonte_texto.render("Inserir no Início", True, (255, 255, 255)), (btn_inicio.x + 30, btn_final.y + 8))
    
    pg.draw.rect(tela, (60, 60, 60), btn_final)
    tela.blit(fonte_texto.render("Inserir no Final", True, (255, 255, 255)), (btn_final.x + 35, btn_final.y + 8))

    pg.draw.rect(tela, (40, 40, 40), (50, 200, 700, 100))
    tela.blit(fonte_titulo.render(resultado_acao, True, (255, 200, 50)), (70, 220))
    tela.blit(fonte_texto.render(resultado_tempo, True, (50, 255, 50)), (70, 260))

    pg.display.flip()
pg.quit()