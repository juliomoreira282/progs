import random
import pickle
import os
import time
import pygame

arquivo_dados_rotas = 'dados_rotas_quick.pkl'

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

def particao(list: list, inicio: int, fim: int):
    pivo = list[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if list[j] <= pivo:
            i += 1
            list[i], list[j] = list[j], list[i]

    list[i + 1], list[fim] = list[fim], list[i + 1]
    return i + 1

def quicksort_inplace(list: list, inicio: int, fim: int):
    if inicio < fim:
        posicao_pivo = particao(list, inicio, fim)

        quicksort_inplace(list, inicio, posicao_pivo - 1)
        quicksort_inplace(list, posicao_pivo + 1, fim) 

lista_rotas_ordenar = lista_rotas_trimestre

inicio_tempo = time.perf_counter() 

quicksort_inplace(lista_rotas_ordenar, 0, len(lista_rotas_ordenar))

fim_tempo = time.perf_counter()

tempo_exec = fim_tempo - inicio_tempo

pygame.init()

largura, altura = 600, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Demonstração de Desempenho Extrema - Merge Sort")

fonte_titulo = pygame.font.SysFont("arial", 28, bold=True)
fonte_texto = pygame.font.SysFont("arial", 22)

texto_titulo = fonte_titulo.render("Resultados da Ordenação", True, "#FFFFFF")
texto_itens = fonte_texto.render(f"Total de itens na lista: {len(lista_rotas_ordenar)}", True, "#C8C8C8")
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