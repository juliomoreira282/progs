import pygame 
import sys
import numpy as np 
from class_polygon_gouraud import Polygon
from polygons_gouraud import polygons
from pygame.locals import *

pygame.init()

FPS = 60
width = 800
height = 600
zBuffer = np.full((width, height), 999.99)

pygame.display.set_caption("Revisão")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

colors = [
    (255, 0, 0),     # Vermelho
    (255, 165, 0),   # Laranja
    (255, 255, 0),   # Amarelo
    (0, 255, 0),     # Verde
    (0, 0, 255),     # Azul
    (128, 0, 128) 
]

p1 = Polygon(1, "Azul", screen, polygons[0], (zBuffer,1), colors)

polygons_arr = [p1]

running = True

print(p1.edges)

while running: 
    screen.fill((255,255,255))
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for layer in polygons_arr:
        layer.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()



