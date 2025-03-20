import pygame

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Visualização 2D")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

x, y = 200, 200
velocidade = 0.5
rodando = True
while rodando:
    screen.fill(PRETO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= velocidade
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += velocidade
    
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= velocidade
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += velocidade
    
    pygame.draw.rect(screen, (BRANCO), [x, y, 50, 50])

    pygame.display.flip()
pygame.quit()