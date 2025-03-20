import pygame

pygame.init()

# Configuração da tela
largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Animação com Pygame")

# Cores
AZUL = (50, 150, 255)
BRANCO = (255, 255, 255)

x, y = 100, 300
spdX = 5
spdY = 0

clock = pygame.time.Clock() # Relógio para controle de FPS

rodando = True
while rodando:
    screen.fill(AZUL)
    for event in pygame.event.get(): # Captura eventos
        if event.type == pygame.QUIT:
            rodando = False
    x += spdX # Atualiza posição do círculo
    if x > largura - 50 or x < 50: # Mantém dentro da tela
        spdX = -spdX
    pygame.draw.circle(screen, BRANCO, (x, y), 50) # Desenho do Círculo
    pygame.display.flip()
    clock.tick(60) # Mantém a fluidez da animação com 60 FPS

pygame.quit()