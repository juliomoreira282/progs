import pygame
import math
import random
from pygame.locals import *
from pygame import Vector2

LARGURA, ALTURA = 800, 600
FPS = 60
QTD_PARTICULAS = 100
COR_FUNDO = (10, 10, 10)
COR_LUZ = (255, 220, 150)
RAIO_DA_LUZ = 50

class SistemaParticulas:
    def __init__(self, qtd):
        self.particulas = []
        self.criar_particulas(qtd)
    
    def criar_particulas(self, qtd):
        for _ in range(qtd):
            posicao = Vector2(random.randint(0, LARGURA), random.randint(0, ALTURA))
            velocidade = Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(0.5, 2.0)
            tamanho = random.randint(3, 8)
            cor = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            vida = random.uniform(5, 10)

            self.particulas.append({
                'posicao': posicao,
                'velocidade': velocidade,
                'tamanho': tamanho,
                'cor': cor,
                'vida': vida,
                'vida_maxima': vida
            })

    def atualizar(self, dt, luz_pos):
        for particula in self.particulas:
            particula['posicao'] += particula['velocidade'] * dt * 60
            
            if particula['posicao'].x < 0 or particula['posicao'] > LARGURA:
                particula['velocidade'].x *= -0.9
            if particula['posicao'].y < 0 or particula['posicao'].y > ALTURA:
                particula['velocidade'].y *= -0.9
            
            particula['posicao'].x = max(0, min(LARGURA, particula['posicao'].x))
            particula['posicao'].y = max(0, min(ALTURA, particula['posicao'].y))

            centro = Vector2(LARGURA / 2, ALTURA / 2)
            direcao = centro - particula['posicao']
            if direcao.length() > 0:
                direcao = direcao.normalize()
                particula['velocidade'] += direcao * 0.01 * dt
            
            if particula['velocidade'].length() > 3:
                particula['velocidade'] = particula['velocidade'].normalize() * 3

            particula['vida'] -= 0.01 * dt
            if particula['vida'] <= 0:
                particula['posicao'] = Vector2(random.randint(0, LARGURA), random.randint(0, ALTURA))
                particula['veloocidade'] = Vector2(random.uniform(-1, 1), random.uniform(-1, 1)).normalize() * random.uniform(0.5, 2.0)
                particula['vida'] = particula['vida_maxima']
            
            distancia = (particula['posicao'] - luz_pos).length()
            if distancia < RAIO_DA_LUZ:
                fator_luz = 1.0 - (distancia / RAIO_DA_LUZ)
                r = min(255, int(particula['cor_original'][0] + COR_LUZ[0] * fator_luz * 0.5))
                g = min(255, int(particula['cor_original'][1] + COR_LUZ[1] * fator_luz * 0.5))
                b = min(255, int(particula['cor_original'][2] + COR_LUZ[2] * fator_luz * 0.5))

                particula['cor'] = (r, g, b)
                particula['tamanho'] = particula['tamanho'] * (1 + fator_luz * 0.3)
            else:
                particula['cor'] = particula['cor_original']
    
    def desenhar(self, surface):
        for particula in self.particulas:
            alpha = int(255 * particula['vida'] / particula['vida_maxima'])
            tamanho = int(particula['tamanho'] * (0.7 + 0.3 * particula['vida'] / particula['vida_maxima']))
            pygame.draw.circle(surface, particula['cor'],
                              (int(particula['posicao'].x), int(particula['posicao'].y)),
                              tamanho)
            
class FonteDeLuz:
    def __init__(self):
        self.posicao = Vector2(LARGURA // 2, ALTURA // 2)
        self.cor = COR_LUZ
        self.raio = RAIO_DA_LUZ
        self.intensidade_flicker = 0.1
    
    def atualizar(self, dt, mouse_pos=None):
        if mouse_pos:
            direcao = Vector2(mouse_pos) - self.posicao
            self.posicao += direcao * 0.1 * dt
        
        self.raio = RAIO_DA_LUZ * (1 + math.sin(pygame.time.get_ticks() * 0.002) * self.intensidade_flicker)
    
    def desenhar(self, superficie):
        superficie_luz = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
        for raio in range(int(self.raio), 0, -4):
            alpha = int(100 * (raio / self.raio))
            cor = (self.cor[0], self.cor[1], self.cor[2], alpha)
            pygame.draw.circle(superficie_luz, cor, 
                              (int(self.posicao.x), int(self.posicao.y)),
                              raio)
        
        superficie.blit(superficie_luz, (0, 0), flags_especiais=pygame.BLEND_RGBA_ADD)

def renderizar_texto(superficie, texto, posicao ,cor=(255, 255, 255)):
    fonte = pygame.font.SysFont('Arial', 16)
    superficie_texto = fonte.render(texto, True, cor)
    superficie.blit(superficie_texto, posicao)

def main():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Sistema de Partículas com Iluminação Dinâmica")
    clock = pygame.time.Clock()

    particulas = SistemaParticulas(QTD_PARTICULAS)
    luz = FonteDeLuz()

    rodando = True
    while rodando:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    rodando = False
        
        mouse_pos = pygame.mouse.get_pos()
        luz.atualizar(dt, mouse_pos)
        particulas.atualizar(dt, luz.posicao)

        screen.fill(COR_FUNDO)
        particulas.desenhar(screen)
        luz.desenhar(screen)
        texto_fps = f"FPS: {int(clock.get_fps())}"
        renderizar_texto(screen, texto_fps, (10, 10))
        renderizar_texto(screen, "Mova o mouse para controlar a luz", 10, 30)

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()