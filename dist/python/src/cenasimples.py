import pygame

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cena Simples")

AZUL = (135, 206, 235)
AMARELO = (255, 255, 0)
VERDE = (34, 139, 34)
MARROM = (139, 69, 19)
VERMELHO = (255, 0, 0)

screen.fill(AZUL)

pygame.draw.circle(screen, AMARELO, (700, 100), 50)
pygame.draw.polygon(screen, MARROM, [(250, 300), (250, 500), (450, 500), (450, 300)])
pygame.draw.polygon(screen, VERMELHO, [(235, 300), (350, 200), (465, 300)])
pygame.draw.polygon(screen, MARROM, [(100, 350), (100, 500), (75, 500), (75, 350)])
pygame.draw.circle(screen, VERDE, (88, 325), 75 )
pygame.draw.polygon(screen, VERDE, [(0, 600), (0, 500), (800, 500), (800, 600)])
pygame.draw.polygon(screen, AMARELO, [(325, 500), (325, 425), (375, 425), (375, 500)])

desenhando = True
while desenhando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            desenhando = False
        pygame.display.flip()

pygame.quit()