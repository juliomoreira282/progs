import pygame
from pygame.locals import *

INSIDE = 0  
LEFT = 1 
RIGHT = 2 
BOTTOM = 4 
TOP = 8     

def compute_code(x, y, rect):
    code = INSIDE
    if x < rect[0]:
        code |= LEFT
    elif x > rect[2]:
        code |= RIGHT
    if y < rect[1]:
        code |= TOP
    elif y > rect[3]:
        code |= BOTTOM
    return code

def cohen_sutherland_clip(x1, y1, x2, y2, rect):
    code1 = compute_code(x1, y1, rect)
    code2 = compute_code(x2, y2, rect)
    accept = False
    points = []
    
    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2:
            break
        else:
            x, y = 0, 0
            outcode = code1 if code1 else code2
            
            if outcode & TOP:
                x = x1 + (x2 - x1) * (rect[1] - y1) / (y2 - y1)
                y = rect[1]
            elif outcode & BOTTOM:
                x = x1 + (x2 - x1) * (rect[3] - y1) / (y2 - y1)
                y = rect[3]
            elif outcode & RIGHT:
                y = y1 + (y2 - y1) * (rect[2] - x1) / (x2 - x1)
                x = rect[2]
            elif outcode & LEFT:
                y = y1 + (y2 - y1) * (rect[0] - x1) / (x2 - x1)
                x = rect[0]
            
            points.append((x, y))
            
            if outcode == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1, rect)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2, rect)
    
    if accept:
        return (x1, y1, x2, y2), points
    return None, points

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Recorte de Cohen-Sutherland")
    
    des_ret = False
    ret = [0, 0, 0, 0]
    ret_definido = False
    
    desLinha = False
    linhas = []
    linhaTemp = None
    
    rodando = True
    while rodando:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                rodando = False
            elif event.type == MOUSEBUTTONDOWN:
                if not ret_definido:
                    ret[:2] = event.pos
                    des_ret = True
                else:
                    linhaTemp = [event.pos[0], event.pos[1], event.pos[0], event.pos[1]]
                    desLinha = True
            elif event.type == MOUSEBUTTONUP:
                if des_ret:
                    ret[2:] = event.pos
                    ret_definido = True
                    des_ret = False
                elif desLinha:
                    linhas.append(tuple(linhaTemp))
                    desLinha = False
            elif event.type == MOUSEMOTION:
                if des_ret:
                    ret[2:] = event.pos
                elif desLinha:
                    linhaTemp[2:] = event.pos
        
        if ret_definido:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(*ret), 2)
            
            for linha in linhas:
                linhaCortada, interseccoes = cohen_sutherland_clip(*linha, ret)
                pygame.draw.line(screen, (255, 0, 0), (linha[0], linha[1]), (linha[2], linha[3]), 2)
                for point in interseccoes:
                    pygame.draw.circle(screen, (0, 0, 255), (int(point[0]), int(point[1])), 4)
                if linhaCortada:
                    pygame.draw.line(screen, (255, 255, 255), (linhaCortada[0], linhaCortada[1]), (linhaCortada[2], linhaCortada[3]), 2)
        
        if des_ret:
            pygame.draw.rect(screen, (100, 100, 100), pygame.Rect(*ret), 1)
        
        if desLinha and linhaTemp:
            pygame.draw.line(screen, (255, 0, 0), (linhaTemp[0], linhaTemp[1]), (linhaTemp[2], linhaTemp[3]), 2)
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
