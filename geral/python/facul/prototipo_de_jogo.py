import pygame

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Protótipo de Jogo")

AZUL = (50, 150, 255)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

x, y = 400, 300
raio = 20
spdX = 5
spdY = 0

gravidade = 0.5
clock = pygame.time.Clock()

plataformas = [(200, 500, 400, 20), (100, 400, 200, 20), (500, 300, 400, 20), (400, 350, 75, 20)]


rodando = True
while rodando:
    screen.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= spdX
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += spdX
    else:
        velocidadeHorizontal = 0
    
    if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and not aerial:
        spdY = -10
        aerial = True
    spdY += gravidade
    y += spdY
    aerial = True
    for plataforma in plataformas:
        px, py, plarg, palt = plataforma
        if x + raio > px and x - raio < px + plarg and y + raio > py and y + raio < py + palt:
            y = py - raio
            spdY = 0
            aerial = False

    if y > altura:
        x, y = 400, 300
        spdY = 0

    for plataforma in plataformas:
        pygame.draw.rect(screen, AZUL, plataforma)

    pygame.draw.circle(screen, VERMELHO, (x, y), raio)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()