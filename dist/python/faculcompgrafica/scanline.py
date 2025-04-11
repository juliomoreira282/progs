import pygame
import random
import math
import time

pygame.init()

LARGURA, ALTURA = 800, 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Preenchcimento Aleatório Scanline")

AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)

def gerar_poligono(n, largura, altura):
    cx, cy = largura // 2, altura // 2
    raio = min(largura, altura) // 3
    angulos = sorted([random.uniform(0, 2 * math.pi) for _ in range(n)])
    pontos = [(int(cx + math.cos(a) * random.uniform(raio / 2, raio)), 
               int(cy + math.sin(a) * random.uniform(raio / 2, raio))) for a in angulos]
    return pontos

def scanline_fill(surface, pontos, cor):
    min_y = min(p[1] for p in pontos)
    max_y = max(p[1] for p in pontos)

    for y in range(min_y, max_y + 1):
        interseccoes = []
        for i in range(len(pontos)):
            p1 = pontos[i]
            p2 = pontos[(i + 1) % len(pontos)]
            if p1[1] == p2[1]:
                continue
            if p1[1] < p2[1]:
                y1, y2, x1, x2 = p1[1], p2[1], p1[0], p2[0]
            else:
                y1, y2, x1, x2 = p2[1], p1[1], p2[0], p1[0]
            if y1 <= y < y2:
                x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                interseccoes.append(x)

    interseccoes.sort()
    for i in range(0, len(interseccoes), 2):
        if i + 1 < len(interseccoes):
            pygame.draw.line(surface, cor, (int(interseccoes[i]), y), (int(interseccoes[i + 1]), y))

def main():
    clock = pygame.time.Clock()
    tempo_ultimo_poligono = 0
    pontos = []
    rodando = True
    while rodando:
        screen.fill(PRETO)
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - tempo_ultimo_poligono > 5000 or not pontos:
            num_vertices = random.randint(3, 7)
            pontos = gerar_poligono(num_vertices, LARGURA, ALTURA)
            tempo_ultimo_poligono = tempo_atual
        scanline_fill(screen, pontos, AMARELO)

        pygame.draw.polygon(screen, AZUL, pontos, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

if __name__ == "__main__":
    main()