import pygame, sys

# --- configuração inicial ------------------------------------
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Desenho de Polígono interativo")
clock = pygame.time.Clock()

vertices = []          
polygon_closed = False 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not polygon_closed:
                vertices.append(event.pos)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            if len(vertices) >= 3:         
                polygon_closed = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            vertices.clear()
            polygon_closed = False

    screen.fill((255, 255, 255))           
    
    for vx, vy in vertices:
        pygame.draw.circle(screen, (255, 0, 0), (vx, vy), 5)

    if len(vertices) >= 2:
        pygame.draw.lines(
            screen,
            (0, 0, 255),
            polygon_closed,                
            vertices,
            2                             
        )

    if not polygon_closed and len(vertices) >= 1:
        pygame.draw.line(screen, (0, 0, 255), vertices[-1],
                         pygame.mouse.get_pos(), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
