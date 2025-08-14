# transform_simple.py
import pygame, sys, math
pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
clock  = pygame.time.Clock()

verts   = []      # vértices
closed  = False
R       = 6       # raio visível

def centro(pts):
    xs, ys = zip(*pts)
    return sum(xs)/len(xs), sum(ys)/len(ys)

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

        # cliques só antes de fechar
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and not closed:
            verts.append(ev.pos)

        # teclas
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN and len(verts) >= 3:
                closed = True
            if ev.key == pygame.K_c:            # limpar
                verts.clear(); closed = False
            if closed:
                cx, cy = centro(verts)
                if ev.key == pygame.K_r:        # rota 15°
                    ang = math.radians(15)
                    cos, sin = math.cos(ang), math.sin(ang)
                    verts = [(cx + (x-cx)*cos + (y-cy)*sin,
                              cy - (x-cx)*sin + (y-cy)*cos) for x, y in verts]
                if ev.key == pygame.K_t:        # move +10 px em X
                    verts = [(x+10, y) for x, y in verts]
                if ev.key == pygame.K_s:        # escala +10 %
                    verts = [(cx + 1.1*(x-cx), cy + 1.1*(y-cy)) for x, y in verts]

    # -------- desenhar ----------
    screen.fill("white")
    for x, y in verts:
        pygame.draw.circle(screen, "red", (int(x), int(y)), R)
    if len(verts) > 1:
        pygame.draw.lines(screen, "blue", closed,
                          [(int(x), int(y)) for x, y in verts], 2)
    if not closed and verts:
        pygame.draw.line(screen, "blue", verts[-1], pygame.mouse.get_pos())

    pygame.display.flip(); clock.tick(60)

pygame.quit(); sys.exit()
