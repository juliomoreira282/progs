import random
import pickle
import os
import time
import pygame

arquivo_dados_rotas = 'dados_rotas_merge.pkl'
status_geracao = ""

if os.path.exists(arquivo_dados_rotas):
    print(f"{arquivo_dados_rotas} existe. Carregando valores travados.")
    with open(arquivo_dados_rotas, 'rb') as arquivo_bin:
        lista_rotas_trimestre = pickle.load(arquivo_bin)

else:
    print(f"{arquivo_dados_rotas} não existe. Gerando novos números.")
    tamanho_lista = 1500000
    inicio = 1
    fim = 2000000

    lista_rotas_trimestre = random.sample(range(inicio, fim + 1), tamanho_lista)

    with open(arquivo_dados_rotas, 'wb') as arquivo_bin:
        pickle.dump(lista_rotas_trimestre, arquivo_bin)
    print("Novos valores criados com sucesso.")

def merge_sort(list: list):
    if len(list) <= 1:
        return list
    
    meio = len(list) // 2
    esq = merge_sort(list[:meio])
    dir = merge_sort(list[meio:])
    return merge(esq, dir)

def merge(esq: list, dir: list):
    resultado, i, j, = [], 0, 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]: resultado.append(esq[i]); i += 1
        else: resultado.append(dir[j]); j += 1

    return resultado + esq[i:] + dir[j:]

inicio_tempo = time.perf_counter()

lista_rotas_ordenada = merge_sort(lista_rotas_trimestre)

fim_tempo = time.perf_counter()

tempo_exec = fim_tempo - inicio_tempo

pygame.init()

largura, altura = 600, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Demonstração de Desempenho Extrema - Merge Sort")

fonte_titulo = pygame.font.SysFont("arial", 28, bold=True)
fonte_texto = pygame.font.SysFont("arial", 22)

texto_titulo = fonte_titulo.render("Resultados da Ordenação", True, "#FFFFFF")
texto_itens = fonte_texto.render(f"Total de itens na lista: {len(lista_rotas_ordenada)}", True, "#C8C8C8")
texto_tempo = fonte_texto.render(f"Tempo de Execução: {tempo_exec:.9f} seg.", True, "#32FF32")

executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    tela.fill("#1E1E1E")

    tela.blit(texto_titulo, (30, 40))
    tela.blit(texto_itens, (30, 100))
    tela.blit(texto_tempo, (30, 140))

    pygame.display.flip()

pygame.quit()