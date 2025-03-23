import pygame

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Visualização Bidimensional")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

x, y = 200, 200
velocidade = 10
tamanho = 50
angulo = 0

posicaoInicial = (200, 200)
tamanhoInicial = 50
anguloInicial = 0
rodando = True
clock = pygame.time.Clock()

while rodando:
    pygame.time.delay(10)
    screen.fill(PRETO)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= velocidade
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += velocidade

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= velocidade
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += velocidade
    
    if keys[pygame.K_PLUS] or keys[pygame.K_KP_PLUS]:
        tamanho += 5
    if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]:
        tamanho = max(10, tamanho - 5)
    
    if keys[pygame.K_e]:
        angulo -= 5
    if keys[pygame.K_q]:
        angulo += 5

    if keys[pygame.K_r]:
        x, y = posicaoInicial
        tamanho = tamanhoInicial
        angulo = anguloInicial
    
    ret = pygame.Surface((tamanho, tamanho), pygame.SRCALPHA)
    ret.fill(BRANCO)
    retRotacionado = pygame.transform.rotate(ret, angulo)
    retPosicao = retRotacionado.get_rect(center=(x + tamanho // 2, y + tamanho // 2))
    screen.blit(retRotacionado, retPosicao.topleft)
    clock.tick(60)
    pygame.display.flip()

pygame.quit()