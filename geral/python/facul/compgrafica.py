import pygame

pygame.init() 

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Cena Simples")

azul = (135, 206, 235)
amarelo = (255, 255, 0)
verde = (34, 139, 34)
marrom = (139, 69, 19)
vermelho = (255, 0, 0)

screen.fill(azul)

pygame.draw.circle(screen, amarelo, (700, 100), 50)
pygame.draw.polygon(screen, marrom, [(250, 300), (250, 500), (450, 500), (450, 300)])
pygame.draw.polygon(screen, vermelho, [(235, 300), (350, 250), (465, 300)])
pygame.draw.polygon(screen, marrom, [(50, 350), (50, 500), (75, 500), (75, 350)])
pygame.draw.circle(screen, verde, (63,325), 75)

desenhando = True
while desenhando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            desenhando = False
    pygame.display.flip()

pygame.quit()