import pygame
import math

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sol Girando com Movimento de Arco Devagar")

AMARELO = (255, 255, 0)
AZUL = (135, 206, 235)
VERDE = (34, 139, 39)
MARROM = (139, 69, 19)
VERMELHO = (255, 0, 0)

def desenhar_sol(angulo, posicao_x, posicao_y):
    tela.fill(AZUL)  
    sol = pygame.Surface((200, 200), pygame.SRCALPHA)
    pygame.draw.circle(sol, AMARELO, (100, 100), 50)  
     
    sol_rotacionado = pygame.transform.rotate(sol, angulo)
    retangulo = sol_rotacionado.get_rect(center=(posicao_x, posicao_y))  
    tela.blit(sol_rotacionado, retangulo.topleft)  

    for i in range(12):
        angulo_raio = math.radians(i * 30 + angulo) 
        raio_x = 100 * math.cos(angulo_raio) + posicao_x
        raio_y = 100 * math.sin(angulo_raio) + posicao_y
        ponto1 = (posicao_x, posicao_y)
        ponto2 = (raio_x, raio_y)
        ponto3 = (posicao_x + (raio_x - posicao_x) * 0.2, posicao_y + (raio_y - posicao_y) * 0.2)

        pygame.draw.polygon(tela, AMARELO, [ponto1, ponto2, ponto3])
        pygame.draw.polygon(tela, MARROM, [(250, 300), (250, 500), (450, 500), (450, 300)])
        pygame.draw.polygon(tela, VERMELHO, [(235, 300), (350, 200), (465, 300)])
        pygame.draw.polygon(tela, MARROM, [(100, 350), (100, 500), (75, 500), (75, 350)])
        pygame.draw.circle(tela, VERDE, (88, 325), 75)
        pygame.draw.polygon(tela, VERDE, [(0, 600), (0, 500), (800, 500), (800, 600)])
        pygame.draw.polygon(tela, AMARELO, [(325, 500), (325, 425), (375, 425), (375, 500)])
 
angulo = 0

tempo = 0
movimento_maximo = 800

velocidade = 0.05  
tempo_maximo = 200 

desenhar = True
while desenhar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            desenhar = False
            pygame.quit()

    posicao_x = movimento_maximo * (tempo / tempo_maximo) 
      
    posicao_y = 300 - 100 * math.sin(math.radians(tempo * 1))

    desenhar_sol(angulo, posicao_x, posicao_y)

    angulo += 1
    if angulo >= 360:
        angulo = 0  

    tempo += velocidade
    if tempo > tempo_maximo:
        tempo = 0

    pygame.display.flip()