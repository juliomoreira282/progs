import random
import pickle
import os
import time
import pygame

lista_cenario_1 = [234.87, 89.34, 3245.09, 345.86, 345.33]

arquivo_dados = 'dados.pkl'

if os.path.exists(arquivo_dados):
    print(f"Arquivo {arquivo_dados} encontrado. Carregando valores travados.")
    with open(arquivo_dados, 'rb') as arquivo_bin:
        lista_importada = pickle.load(arquivo_bin) # Lista importada = Cenário 2

else:
    print(f"Arquivo {arquivo_dados} não encontrado. Gerando novos números.")
    tamanho_lista = 1000
    inicio = 5.0
    fim = 5000.0

    lista_importada = [round(random.uniform(inicio, fim), 2) for _ in range(tamanho_lista)] 

    with open(arquivo_dados, 'wb') as arquivo_bin:
        pickle.dump(lista_importada, arquivo_bin)
    print("Novos valores criados com sucesso.")

def selection_sort(list):
    n = len(list)
    for i in range(n):
        idx_menor = i
        for j in range(i + 1, n):
            if list[j] < list[idx_menor]:
                idx_menor = j

        list[i], list[idx_menor] = list[idx_menor], list[i]

    return list

inicio_tempo = time.perf_counter()

lista_ordenada = selection_sort(lista_importada)

fim_tempo = time.perf_counter()

tempo_execucao = fim_tempo - inicio_tempo

pygame.init()
largura, altura = 600, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desempenho de Algoritmo - Selection Sort")

fonte_titulo = pygame.font.SysFont("arial", 28, bold=True)
fonte_texto = pygame.font.SysFont("arial", 22)

texto_titulo =  fonte_titulo.render("Resultados da Ordenação", True, (255, 255, 255))
texto_itens = fonte_texto.render(f"Total de itens na lista: {len(lista_ordenada)}", True, (200, 200, 200))
texto_tempo = fonte_texto.render(f"Tempo de execução: {tempo_execucao:.9f} segundos", True, (50, 255, 50))

executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    tela.fill((30, 30, 30))

    tela.blit(texto_titulo, (30, 40))
    tela.blit(texto_itens, (30, 100))
    tela.blit(texto_tempo, (30, 140))

    pygame.display.flip()

pygame.quit()