import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cenário com Sol em Movimento Parabólico")

AMARELO = (255, 255, 0)
AZUL = (135, 206, 235)
VERDE = (34, 139, 39)
MARROM = (139, 69, 19)
VERMELHO = (255, 0, 0)

def desenharSol(angulo, posicaoX, posicaoY):
    screen.fill(AZUL)
    sol = pygame.Surface((200, 200), pygame.SRCALPHA)
    pygame.draw.circle(sol, AMARELO, (100, 100), 50)
    
    solRotacionado = pygame.transform.rotate(sol, angulo)
    retangulo = solRotacionado.get_rect(center=(posicaoX, posicaoY))
    screen.blit(solRotacionado, retangulo.topleft)
    
    for i in range(12):
        anguloRaio = math.radians(i * 30 + angulo)
        raioX = 100 * math.cos(anguloRaio) + posicaoX
        raioY = 100 * math.sin(anguloRaio) + posicaoY
        ponto1 = (posicaoX, posicaoY)
        ponto2 = (raioX, raioY)
        ponto3 = (posicaoX + (raioX - posicaoX) * 0.2, posicaoY + (raioY - posicaoY) * 0.2)

        pygame.draw.polygon(screen, AMARELO, [ponto1, ponto2, ponto3])
        pygame.draw.polygon(screen, MARROM, [(250, 300), (250, 500), (450, 500), (450, 300)])
        pygame.draw.polygon(screen, VERMELHO, [(235, 300), (350, 200), (465, 300)])
        pygame.draw.polygon(screen, MARROM, [(100, 350), (100, 500), (75, 500), (75, 350)])
        pygame.draw.circle(screen, VERDE, (88, 325), 75)
        pygame.draw.polygon(screen, VERDE, [(0, 600), (0, 500), (800, 500), (800, 600)])
        pygame.draw.polygon(screen, AMARELO, [(325, 500), (325, 425), (375, 425), (375, 425)])

angulo = 0
tempo = 0
movimentoMaximo = 800
velocidade = 0.05
tempoMaximo = 200
desenhar = True
while desenhar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            desenhar = False
            pygame.quit()
    
    posicaoX = movimentoMaximo * (tempo / tempoMaximo)
    posicaoY = 300 - 100 * math.sin(math.radians(tempo * 1))
    desenharSol(angulo, posicaoX, posicaoY)
    angulo += 1
    if angulo >= 360:
        angulo = 0
    tempo += velocidade
    
    if tempo > tempoMaximo:
        tempo = 0
    pygame.display.flip()