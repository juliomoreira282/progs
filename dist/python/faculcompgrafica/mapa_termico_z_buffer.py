import pygame
import random
import math
import numpy as np
from pygame.locals import *

pygame.init()
LARGURA, ALTURA = 900, 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Mapa Térmico com Z-Buffer")
clock = pygame.time.Clock()

CORES_TERMICAS = [
    ((255, 0, 0), "Muito Quente") # Vermelho
    ((255, 128, 0), "Quente") # Laranja
    ((255, 255, 0), "Morno") # Amarelo
    ((0, 128, 255), "Frio") # Azul Claro
    ((0, 0, 255), "Muito Frio") # Azul
]

def gerar_poligono_convexo(centro, raio, num_pontos=6):
    angulos = sorted([random.uniform(0, 2 * math.pi) for _ in range(num_pontos)])
    pontos = [
        (int(centro[0] + raio * math.cos(a)), int(centro[1] + raio * math.sin(a)))
        for a in angulos
    ]
    return pontos

def gerar_camadas(num_camadas=5, zoom=1.0):
    camadas = []
    for i in range(num_camadas):
        centro_x = random.randint(100, LARGURA - 250)
        centro_y = random.randint(100, ALTURA - 100)
        raio = int(random.randint(60, 120) * zoom) 
        poligono = gerar_poligono_convexo((centro_x, centro_y), raio)
        cor_inicial, rotulo = CORES_TERMICAS[i % len(CORES_TERMICAS)]
        cor_final = tuple(min(255, c + 100) for c in cor_inicial)
        z = random.uniform(0.0, 1.0)
        camadas.append({
            'poligono': poligono,
            'centro': (centro_x, centro_y), 
            'cor_inicial': cor_inicial,
            'z': z,
            'rotulo': rotulo
        })
    
    return camadas

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def distancia(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])


def desenhar_poligono_zbuffer_gradiente(poligono, centro, cor_inicial, cor_final, z, z_buffer, framebuffer):
    mascara = pygame.mask.from_surface(superficie_poligono(poligono))
    offset = mascara.get_bounding_rect().topleft
    distancia_maxima = max([distancia(p, centro) for p in poligono]) + 1e-6

    for y in range(mascara.get_size()[1]):
        for x in range(mascara.get_size()[0]):
            if mascara.get_at((x, y)):
                px = x + offset[0]
                py = y + offset[1]
                if 0 <= px < LARGURA and 0 <= py < ALTURA:
                    if z < z_buffer[px, py]:
                        dist = distancia((px, py), centro) / distancia_maxima
                        cor = lerp_color(cor_inicial, cor_final, dist)
                        framebuffer.set_at((px, py), cor)
                        z_buffer[px, py] = z

def superficie_poligono(pontos):
    superficie = pygame.Surface((LARGURA, ALTURA), SRCALPHA)
    pygame.draw.polygon(superficie, (255, 255, 255), pontos)
    return superficie

def rotacionar_ponto_centro(ponto, centro, angulo):
    cx, cy = centro
    px, py = ponto
    s = math.sin(angulo)
    c = math.cos(angulo)
    px -= cx
    py -= cy
    x_novo = px * c - py * s
    y_novo = px * s - py * c
    return (int(x_novo + cx), int(y_novo + cy))

def rotacionar_poligonos(camadas, angulo):
    for camada in camadas:
        camada['poligono'] = [rotacionar_ponto_centro(p, camada['centro'], angulo) for p in camada['poligono']]

def renderizar(camadas, framebuffer, z_buffer):
    framebuffer.fill((0, 0, 0))
    z_buffer[:, :] = np.inf
    for camada in camadas:
        desenhar_poligono_zbuffer_gradiente(
            camada['poligono'], camada['centro'],
            camada['cor_inicial'], camada['cor_final'],
            camada['z'], z_buffer, framebuffer
        )

def desenhar_legenda(screen):
    font = pygame.font.SysFont(None, 22)
    legenda_x = LARGURA - 90
    pygame.draw.rect(screen, (20, 20, 20), (legenda_x - 10, 0, 100, ALTURA))
    y = 30
    for cor, rotulo in CORES_TERMICAS:
        pygame.draw.rect(screen, cor, (legenda_x, y, 20, 20))
        texto = font.render(rotulo, True, (255, 255, 255))
        screen.blit(texto, (legenda_x + 30, y + 2))
        y += 35
    pygame.draw.line(screen, (255, 255, 255), (legenda_x - 5, 0), (legenda_x - 5, ALTURA), 1)

def main():
    zoom = 1.0
    camadas = gerar_camadas(zoom=zoom)
    framebuffer = pygame.Surface((LARGURA, ALTURA))
    z_buffer = np.full((LARGURA, ALTURA), np.inf)

    renderizar(camadas, framebuffer, z_buffer)

    rodando = True
    while rodando:
        redesenhar = False
        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False

            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    rotacionar_poligonos(camadas, math.radians(-10))
                    redesenhar = True
                elif event.button == 3:
                    camadas = gerar_camadas(zoom=zoom)
                    redesenhar = True
            
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    rodando = False
                elif event.key == K_LEFT:
                    rotacionar_poligonos(camadas, math.radians(-10))
                    redesenhar = True
                elif event.key == K_RIGHT:
                    rotacionar_poligonos(camadas, math.radians(10))
                elif event.key == K_UP:
                    zoom = min(2.0, zoom + 0.1)
                    camadas = gerar_camadas(zoom=zoom)
                    redesenhar = True
                elif event.key == K_DOWN:
                    zoom = max(0.3, zoom - 0.1)
                    camadas = gerar_camadas(zoom=zoom)
                    redesenhar = True
                
        if redesenhar:
            renderizar(camadas, framebuffer, z_buffer)
        
        screen.blit(framebuffer, (0, 0))
        desenhar_legenda(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()