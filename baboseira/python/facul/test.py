import pygame

pygame.init() 

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Primitivas Gráficas 2D")

desenhando = True
while desenhando:
    for event in pygame.get():
        if event.type == pygame.quit():
            desenhando = False
    pygame.display.flip()

pygame.quit()