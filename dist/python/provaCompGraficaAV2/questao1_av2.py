import pygame
import math
from pygame.locals import *

pygame.init()

LARGURA, ALTURA = 800, 600

screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desenho de Polígonos Scanline")

VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

posicoes = []
vertices = []
pontos_captura = True

def gerar_vertices(pontos):
    centro_x = sum([p[0] for p in pontos]) / len(pontos)
    centro_y = sum([p[1] for p in pontos]) / len(pontos)
    return sorted(pontos, key=lambda v:math.atan2(v[1] - centro_y, v[0] - centro_x))

def scanline(polygon):
    ymin = int(min([p[1] for p in polygon]))
    ymax = int(max([p[1] for p in polygon]))

    for y in range(ymin, ymax + 1):
        interseccoes = []

        for i in range(len(polygon)):
            p1 = polygon[i]
            p2 = polygon[(i + 1) % len(polygon)]

            if p1[1] == p2[1]:
                continue
            if p1[1] > p2[1]:
                p1, p2 = p2, p1
            if p1[1] <= y <= p2[1]:
                x = p1[0] + (y - p1[1]) * ((p2[0] - p1[0]) / (p2[1] - p1[1]))
                interseccoes.append(x)

        interseccoes.sort()

        for i in range(0, len(interseccoes), 2):
            if i + 1 < len(interseccoes):
                x1 = int(interseccoes[i])
                x2 = int(interseccoes[i + 1])
                pygame.draw.line(screen, VERDE, (x1, y), (x2, y), 2)

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == QUIT:
            rodando = False
        
        elif event.type == MOUSEBUTTONDOWN and pontos_captura:
            pos = pygame.mouse.get_pos()
            posicoes.append(pos)

        elif event.type == KEYDOWN:
            if event.key == K_RETURN and pontos_captura:
                vertices = gerar_vertices(posicoes)
                pontos_captura = False
            elif event.key == K_ESCAPE:
                rodando = False
    
    screen.fill(BRANCO)

    for ponto in posicoes:
        pygame.draw.circle(screen, VERMELHO, ponto, 10)
    
    if not pontos_captura:
        scanline(vertices)
        pygame.draw.polygon(screen, AZUL, vertices, 5)

    pygame.display.flip()

pygame.quit()