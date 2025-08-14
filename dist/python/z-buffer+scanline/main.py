import pygame
import sys 
from polygon import Polygon
from layers import handle_layers
from pygame.locals import *
import numpy as np 

pygame.init()

width = 800
height = 600
FPS  = 60

zBuffer = np.full((width, height), float('inf'))

pygame.display.set_caption("Atividade Z-buffer")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

running = True

polygon_points1 = [
    (400, 200, 1), 
    (495, 262, 1),   
    (459, 370, 1),   
    (341, 370, 1),   
    (305, 262, 1)    
]

polygon_points2 = [
    (390, 210, 0.8),
    (480, 270, 0.8),
    (450, 355, 0.8),
    (350, 355, 0.8),
    (315, 270, 0.8)
]

polygon_points3 = [
    (410, 190, 1.2),
    (500, 260, 1.2),
    (470, 380, 1.2),
    (330, 380, 1.2),
    (295, 260, 1.2)
]

polygon_points4 = [
    (375, 230, 0.6),
    (455, 260, 0.6),
    (430, 330, 0.6),
    (350, 330, 0.6),
    (325, 260, 0.6)
]

polygon_points5 = [
    (395, 215, 0.95),
    (485, 265, 0.95),
    (455, 360, 0.95),
    (345, 360, 0.95),
    (310, 265, 0.95)
]


polygon1 = Polygon(polygon_points1, screen, zBuffer, (143,205,155), "")
polygon2 = Polygon(polygon_points2, screen, zBuffer, (0,0,0), "")
polygon3 = Polygon(polygon_points3, screen, zBuffer, (143,90,200), "")
polygon4 = Polygon(polygon_points4, screen, zBuffer, (143,90,0), "")
polygon5 = Polygon(polygon_points5, screen, zBuffer, (0,90,200), "")

def drawButton(layers):
    font = pygame.font.SysFont(None, 18)
    width, height = 100, 40
    x, y = 20, 20 

    btns = []

    for layer in layers:
        btn = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, layer._color, btn)
        text = font.render(layer._name, True, (11,11,11))
        screen.blit(text, (x + 20, y + 14))

        btns.append({
            "rect": btn, 
            "layer": layer
        })

        y +=60
    

    return btns


#area de teste 
while running:
    
    mouse_pos = pygame.mouse.get_pos()
    screen.fill((0, 0, 0))
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    polygon1.draw()
    polygon2.draw()
    polygon3.draw()
    polygon4.draw()
    polygon5.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()