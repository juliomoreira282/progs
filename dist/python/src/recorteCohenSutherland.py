import pygame
import random

LARGURA, ALTURA = 800, 600

PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

X_MIN, Y_MIN = 200, 150
X_MAX, Y_MAX = 600, 450

INSIDE = 0
ESQUERDA = 1
DIREITA = 2
ABAIXO = 4
ACIMA = 8

pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Recorte de Linhas Cohen-Sutherland")

def get_code(x, y):
    code = INSIDE
    if x < X_MIN:
        code |= ESQUERDA
    elif x > X_MAX:
        code |= DIREITA
    if y < Y_MIN:
        code |= ACIMA
    elif y > Y_MAX:
        code |= ABAIXO

def cohen_sutherland(x1, y1, x2, y2):
    code1 = get_code(x1, y1)
    code2 = get_code(x2, y2)
    aceita = True

    while True:
        if code1 == 0 and code2 == 0:
            aceita = True
            break
        elif (code1 and code2) != 0:
            break
        else:
            x, y = 0, 0
            code_out = code1 if code1 != 0 else code2
            if code_out & ACIMA:
                x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
                y = Y_MIN
            elif code_out & ABAIXO:
                x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)
                y = Y_MAX
            elif code_out & DIREITA:
                y = y1 + (x2 - x1) * (X_MAX - x1) / (x2 - x1)
                x = X_MAX
            elif code_out & ESQUERDA:
                y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
                x = X_MIN

            if code_out == code1:
                x1, y1 = x, y
                code1 = get_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = get_code(x2, y2)
    if aceita:
        return int(x1), int(y1), int(x2), int(y2)
    else:
        return None

def desenhar_linhas():
    for _ in range(10):
        x1, y1 = random.randint(0, LARGURA), random.randint(0, ALTURA)
        x2, y2 = random.randint(0, LARGURA), random.randint(0, ALTURA)

        pygame.draw.line(screen, VERMELHO, (x1, y1), (x2, y2), 2)
        linha_recortada = cohen_sutherland(x1, y1, x2, y2)

        if linha_recortada:
            pygame.draw.line(screen, BRANCO, (linha_recortada[0], linha_recortada[1]), (linha_recortada[2], linha_recortada[3]), 3)

def main():
    rodando = True
    while rodando:
        screen.fill(PRETO)
        pygame.draw.rect(screen, BRANCO, (X_MIN, Y_MIN, X_MAX - X_MIN, Y_MAX - Y_MIN), 2)
        desenhar_linhas()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
        pygame.display.flip()
        pygame.time.delay(500)

    pygame.quit()

if __name__ == "__main__":
    main()