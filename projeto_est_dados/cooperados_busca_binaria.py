import random
import pickle
import os
import time
import pygame

arquivo_dados_cooperados = 'dados_cooperados.pkl'

if os.path.exists(arquivo_dados_cooperados):
    print(f"{arquivo_dados_cooperados} existe. Carregando valores armazenados.")
    with open(arquivo_dados_cooperados, 'rb') as arquivo_bin:
        lista_cooperados = pickle.load(arquivo_bin)

else:
    print(f"{arquivo_dados_cooperados} não encontrado. Gerando novos valores.")
    tamanho_lista = 3000
    inicio = 1
    fim = 3001

    lista_cooperados = []
    while len(lista_cooperados) < tamanho_lista:
        numero = random.randint(inicio, fim)
        if numero not in lista_cooperados:
            lista_cooperados.append(numero)

    with open(arquivo_dados_cooperados, 'wb') as arquivo_bin:
        pickle.dump(lista_cooperados, arquivo_bin)
    print("Novos valores criados com sucesso.")

def merge_sort(list: list):
    if len(list) <= 1:
        return list
    
    meio = len(list) // 2
    esq = merge_sort(list[:meio])
    dir = merge_sort(list[meio:])
    return merge(esq, dir)

def merge(esq, dir):
    resultado, i, j = [], 0, 0
    while i < len(esq) and j < len(dir):
        if esq[i] <= dir[j]: resultado.append(esq[i]); i += 1
        else: resultado.append(dir[j]); j += 1

    return resultado + esq[i:] + dir[j:]   

def busca_binaria(lista_ordenada: list, valor_procurado: int):
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        chute = lista_ordenada[meio]
        if chute == valor_procurado:
            return f"Achei na posição {meio}!"
        
        if chute > valor_procurado:
            fim = meio - 1

        else:
            inicio = meio + 1

    return "Não está na lista."

lista_ordenada = merge_sort(lista_cooperados)
valor_alvo = 70

inicio_tempo = time.perf_counter()

resultado_da_busca = busca_binaria(lista_ordenada, valor_alvo)

fim_tempo = time.perf_counter()

tempo_execucao = fim_tempo - inicio_tempo

pygame.init()

largura, altura = 600, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desempenho de Algoritmo - Busca Binária")

fonte_titulo = pygame.font.SysFont("arial", 28, bold=True)
fonte_texto = pygame.font.SysFont("arial", 22)

texto_titulo = fonte_titulo.render("Resultados da Busca", True, (255, 255, 255))
texto_itens = fonte_texto.render(f"Total de itens na lista: {len(lista_cooperados)}", True, (200, 200, 200))
texto_tempo = fonte_texto.render(f"Tempo de execução: {tempo_execucao:.9f} segundos", True, (50, 255, 50))
texto_item_procurado = fonte_texto.render(f"Procurando {valor_alvo}: {resultado_da_busca}", True, (200, 200, 200))

executando = True
while executando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    tela.fill((30, 30, 30))

    tela.blit(texto_titulo, (30, 40))
    tela.blit(texto_itens, (30, 100))
    tela.blit(texto_tempo, (30, 140))
    tela.blit(texto_item_procurado, (30, 180))

    pygame.display.flip()

pygame.quit()