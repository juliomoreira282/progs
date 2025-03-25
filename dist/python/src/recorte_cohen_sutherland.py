import pygame
from pygame.locals import *

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM= 4
TOP = 8

def compute_code(x, y, ret):
    code = INSIDE
    if x < ret[0]:
        code |= LEFT
    elif x > ret[2]:
        code |= RIGHT
    if y < ret[1]:
        code |= TOP
    elif y > ret[3]:
        code |= BOTTOM
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, ret):
    code1 = compute_code(x1, y1, ret)
    code2 = compute_code(x2, y2, ret)
    accept = False
    points = []

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 and code2:
            break
        else:
            x, y = 0, 0
            outcode = code1 if code1 else code2

            if outcode and TOP:
                x = x1 + (x2 - x1) * (ret[1] - y1) / (y2 - y1)
                y = ret[1]
            elif outcode and BOTTOM:
                x = x1 + (x2 - x1) * (ret[3] - y1) / (y2 - y1)
                y = ret[3]
            elif outcode and RIGHT:
                y = y1 + (y2 - y1) * (ret[2] - x1) / (x2 - x1)
                x = ret[2]
            elif outcode and LEFT:
                y = y1 + (y2 - y1) * (ret[0] - x1) / (x2 - x1)
                x = ret[0]

            points.append((x, y))

            if outcode == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, ret)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, ret)
    
    if accept:
        return (x1, y1, x2, y2), points
    return None, points

def main():
    pygame.init()
    largura, altura = 800, 600
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Recorte de Cohen-Sutherland")

    PRETO = (0, 0, 0)
    BRANCO = (255, 255, 255)
    VERMELHO = (255, 0, 0)
    AZUL = (0, 0, 255)
    CINZA = (100, 100, 100)

    des_ret = False
    ret = [0, 0, 0, 0]
    ret_definido = False

    des_linha = False
    linhas = []
    linha_temp = False

    rodando = True
    while rodando:
        screen.fill(PRETO)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == MOUSEBUTTONDOWN:
                if not ret_definido:
                    ret[:2] = event.pos
                    des_ret = True
                else:
                    linha_temp = [event.pos[0], event.pos[1], event.pos[0], event.pos[1]]
                    des_linha = True
            elif event.type == MOUSEBUTTONUP:
                if des_ret:
                    ret[2:] = event.pos
                    ret_definido = True
                    des_ret = False
                elif des_linha:
                    linhas.append(tuple(linha_temp))
                    des_linha = False
            elif event.type == MOUSEMOTION:
                if des_ret:
                    ret[2:] = event.pos
                elif des_linha:
                    linha_temp[2:] = event.pos
        
        if ret_definido:
            pygame.draw.rect(screen, BRANCO, pygame.Rect(*ret), 2)

            for linha in linhas:
                linha_cortada, interseccoes = cohen_sutherland_clip(*linha, ret)
                pygame.draw.line(screen, VERMELHO, (linha[0], linha[1]), (linha[2], linha[3]), 2)
                for point in interseccoes:
                    pygame.draw.circle(screen, AZUL, (int(point[0]), int(point[1])), 4)
                if linha_cortada:
                    pygame.draw.line(screen, BRANCO, (linha_cortada[0], linha_cortada[1]), (linha_cortada[2], linha_cortada[3]), 2)
        
        if des_ret:
            pygame.draw.rect(screen, CINZA, pygame.Rect(*ret), 1)
        
        if des_linha and linha_temp:
            pygame.draw.line(screen, VERMELHO, (linha_temp[0], linha_temp[1]), (linha_temp[2], linha_temp[3]), 2)
        
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()