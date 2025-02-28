import pygame

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Animação com Pygame")

AZUL = (50, 150, 255)
BRANCO = (255, 255, 255)

x, y = 400, 300
spdX = 5
spdY = 0

velocidadeHorizontal = 0
velocidadeVertical = 0

gravidade = 0.5
clock = pygame.time.Clock()

rodando = True
while rodando:
    screen.fill(AZUL)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        velocidadeHorizontal = -5
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        velocidadeHorizontal = 5
    else:
        velocidadeHorizontal = 0
    
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        velocidadeVertical = -5
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        velocidadeVertical = 5
    else:
        velocidadeVertical = 0
    
    x += velocidadeHorizontal
    y += velocidadeVertical
    spdY += gravidade
    y += spdY
    if x > largura - 50 or x < 50:
        spdX = -spdX
    if y > altura - 50 or y < 50:
        y = altura - 50
        spdY = -spdY * 0.8
    elif y < 50:
        y = 50
        spdY = -spdY
    pygame.draw.circle(screen, BRANCO, (x, y), 50)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()