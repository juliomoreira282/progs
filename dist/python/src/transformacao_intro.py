import pygame

pygame.init()

largura, altura = 800, 600
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Translação de Quadrado com Pygame")

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

def transladar_ponto(ponto, tx, ty):
    x, y = ponto
    return (x, tx, y + ty)

def transladar_objeto(objeto, tx, ty):
    return [transladar_ponto(ponto, tx, ty) for ponto in objeto]

quadrado = [
    (50, 50),
    (150, 50),
    (150, 150),
    (50, 150)
]

tx, ty = 0, 0

def main():
    global tx, ty, quadrado

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    tx += 20
                    ty += 20
                    quadrado = transladar_objeto(quadrado, 20, 20)
        
        screen.fill(BRANCO)
        pygame.draw.polygon(screen, VERMELHO, quadrado, 2)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()