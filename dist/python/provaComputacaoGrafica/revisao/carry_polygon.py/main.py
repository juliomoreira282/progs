# drag_simple.py
import pygame, sys, math
pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
clock  = pygame.time.Clock()

vertices = []          # pontos clicados
closed   = False       # já apertou Enter?
drag_idx = None        # índice do ponto que está sendo arrastado
R = 6                  # raio visível e de clique

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

        # clique esquerdo
        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            if not closed:                     # ainda criando
                vertices.append(ev.pos)
            else:                              # polígono fechado → tentar pegar um vértice
                for i, v in enumerate(vertices):
                    if math.dist(ev.pos, v) < R + 2:
                        drag_idx = i
                        break

        # solta o botão → para arraste
        if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
            drag_idx = None

        # move mouse enquanto arrasta
        if ev.type == pygame.MOUSEMOTION and drag_idx is not None:
            vertices[drag_idx] = ev.pos

        # Enter fecha; C limpa
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RETURN and len(vertices) >= 3:
                closed = True
            if ev.key == pygame.K_c:
                vertices.clear(); closed = False

    # -------- desenhar ----------
    screen.fill("white")
    for x, y in vertices:                       # círculos vermelhos
        pygame.draw.circle(screen, "red", (x, y), R)
    if len(vertices) > 1:                       # contorno azul
        pygame.draw.lines(screen, "blue", closed, vertices, 2)
    if not closed and vertices:                 # linha provisória
        pygame.draw.line(screen, "blue", vertices[-1], pygame.mouse.get_pos())

    pygame.display.flip(); clock.tick(60)

pygame.quit(); sys.exit()
