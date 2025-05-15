import pygame
import math
import random
import sys

pygame.init()

LARGURA, ALTURA = 800, 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Representação de Terrenos com Z-Buffer")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
VERDE = (0, 255, 0)
CIANO = (0, 255, 255)
MAGENTA = (255, 0, 255)

CORES = [VERMELHO, VERDE, AZUL, AMARELO, CIANO, MAGENTA]

class Poligono3D:
    def __init__(self, vertices, cor, profundidade):
        self.vertices = vertices
        self.cor = cor
        self.profundidade = profundidade
    
    def desenhar(self, superficie):
        pygame.draw.polygon(superficie, self.cor, self.vertices)
        fonte = pygame.font.SysFont('Arial', 16)
        texto = fonte.render(f"Z={self.profundidade}", True, PRETO)
        centro_x = sum(v[0] for v in self.vertices) / len(self.vertices)
        centro_y = sum(v[1] for v in self.vertices) / len(self.vertices)
        superficie.blit(texto, (centro_x - texto.get_width() // 2, centro_y - texto.get_height() // 2))

class ZBuffer:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.buffer = [[float('inf') for _ in range(largura)] for _ in range(altura)]
        self.cor_buffer = [[PRETO for _ in range(largura)] for _ in range(altura)]
    
    def limpar(self):
        for y in range(self.altura):
            for x in range(self.largura):
                self.buffer[y][x] = float('inf')
                self.cor_buffer[y][x] = PRETO

    def renderizar_poligono(self, poligono):
        min_x = max(0, min(v[0] for v in poligono.vertices))
        max_x = min(self.largura - 1, max(v[0] for v in poligono.vertices))
        min_y = max(0, min(v[1] for v in poligono.vertices))
        max_y = max(self.altura - 1, max(v[1] for v in poligono.vertices))

        min_x, max_x = int(min_x), int(max_x)
        min_y, max_y = int(min_y), int(max_y)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if self.ponto_dentro_poligono((x, y), poligono.vertices):
                    if poligono.profundidade < self.buffer[y][x]:
                        self.buffer[y][x] = poligono.profundidade
                        self.cor_buffer[y][x] = poligono.cor

    def ponto_dentro_poligono(self, ponto, vertices):
        """Verifica se um ponto está dentro de um polígono usando o algoritmo de Ray Casting"""
        x, y = ponto
        dentro = False
        j = len(vertices) - 1

        for i in range(len(vertices)):
            if ((vertices[i][1] > y) != (vertices[j][1] > y)) and \
                (x < vertices[i][0] + (vertices[j][0] - vertices[i][0]) * (y - vertices[i][1]) /
                (vertices[j][1] - vertices[i][1])):
                dentro = not dentro
            j = i
        return dentro
    
    def desenhar(self, superficie):
        for y in range(self.altura):
            for x in range(self.altura):
                if self.buffer[y][x] != float('inf'):
                    superficie.set_at((x, y), self.cor_buffer[y][x])
    
def criar_poligono_aleatorio():
    num_vertices = random.randint(3, 6)
    raio = random.randint(30, 80)
    angulo_inicial = random.uniform(0, 2 * math.pi)
   
    centro_x = random.randint(100, LARGURA - 100)
    centro_y = random.randint(100, ALTURA - 100)
    profundidade = random.randint(1, 10)
   
    vertices = []
    for i in range(num_vertices):
        angulo = angulo_inicial + (2 * math.pi * i / num_vertices)
        x = centro_x + raio * math.cos(angulo)
        y = centro_y + raio * math.sin(angulo)
        vertices.append((x, y))
   
    cor = random.choice(CORES)
    return Poligono3D(vertices, cor, profundidade)
    
def scanline_fill(poligono, superficie, cor):
    vertices = poligono.vertices
   
    # Encontra os limites y
    min_y = int(min(v[1] for v in vertices))
    max_y = int(max(v[1] for v in vertices))
   
    for y in range(min_y, max_y + 1):
        intersecoes = []
       
        for i in range(len(vertices)):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % len(vertices)]
           
            if (y1 <= y < y2) or (y2 <= y < y1):
                if y1 == y2: 
                    continue
               
                x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                intersecoes.append(x)
       
        intersecoes.sort()
       
        for i in range(0, len(intersecoes), 2):
            if i + 1 < len(intersecoes):
                pygame.draw.line(superficie, cor,
                                (int(intersecoes[i]), y),
                                (int(intersecoes[i+1]), y))

def main():
    relogio = pygame.time.Clock()
    z_buffer = ZBuffer(LARGURA, ALTURA)
    poligonos = []
    modo_atual = 0 # 0: Z-Buffer, 1: Ordem de desenho, 2: Demonstração Scanline
    poligono_scanline = None
    fonte = pygame.font.SysFont('Arial', 18)
    texto_ajuda = [
        "Teclas:",
        "ESPAÇO: Adicionar Polígono",
        "DELETE: Remover Todos",
        "M: Mudar Modo de Visualização",
        "ESC: Sair"
    ]

    executando = True
    while executando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    executando = False
                elif event.key == pygame.K_SPACE:
                    poligonos.append(criar_poligono_aleatorio())
                    if modo_atual == 2:
                        poligono_scanline = poligonos[-1]
                elif event.key == pygame.K_DELETE:
                    poligonos.clear()
                    poligono_scanline = None
                elif event.key == pygame.K_m:
                    modo_atual = (modo_atual + 1) % 3
                    if modo_atual == 2 and poligonos:
                        poligono_scanline = poligonos[-1]
        screen.fill(PRETO)
        if modo_atual == 0: # Z-Buffer
            z_buffer.limpar()
            for p in poligonos:
                z_buffer.renderizar_poligono(p)
            z_buffer.desenhar(screen)

            modo_texto = "Modo: Z-Buffer (profundidade)"

        elif modo_atual == 1: # Ordem de desenho (Z-Bufferless)
            poligonos_ordenados = sorted(poligonos, key=lambda p: p.profundidade, reverse=True)
            for p in poligonos_ordenados:
                p.desenhar(screen)
            modo_texto = "Modo: Ordem de Desenho (Z-Bufferless)"
        
        elif modo_atual == 2:
            for p in poligonos:
                pygame.draw.polygon(screen, p.cor, p.vertices, 2)

            if poligono_scanline:
                scanline_fill(poligono_scanline, screen, poligono_scanline.cor)

            modo_texto = "Modo: Demonstração Scanline"
        texto_modo = fonte.render(modo_texto, True, PRETO)
        screen.blit(texto_modo, (10, 10))

        for i, linha in enumerate(texto_ajuda):
            texto = fonte.render(linha, True, BRANCO)
            screen.blit(texto, (10, 40 + i * 25))
        
        texto_contador = fonte.render(f"Polígonos: {len(poligonos)}", True, PRETO)
        screen.blit(texto_contador, (LARGURA - texto_contador.get_width() - 10, 10))

        pygame.display.flip()
        relogio.tick(30)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()