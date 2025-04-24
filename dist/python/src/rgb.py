import pygame
import colorsys

pygame.init()

LARGURA, ALTURA = 800, 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Modelos de Cores")

cor_rgb = (255, 0, 0) # Vermelho
modo_cor = "RGB"

def rgb_para_cmy(rgb):
    r, g, b = rgb
    return (255 - r, 255 - g, 255 - b)

def rgb_para_hsv(rgb):
    r, g, b = rgb
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    return (int(h * 360), int(s * 100), int(v * 100))

def hsv_para_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)
    return (int(r * 255), int(g * 255), int(b * 255))

def desenha_interface():
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, cor_rgb, (250, 150, 300, 300))
    fonte = pygame.font.Font(None, 36)
    texto_rgb = fonte.render(f"RGB: {cor_rgb}", True, (255, 255, 255))
    screen.blit(texto_rgb, (50, 500))

    if modo_cor == "RGB":
        texto_rgb = fonte.render(f"RGB: {cor_rgb}", True, (255, 255, 255))
        screen.blit(texto_rgb, (50, 500))

    elif modo_cor == "CMY":
        cor_cmy = rgb_para_cmy(cor_rgb)
        texto_cmy = fonte.render(f"CMY: {cor_cmy}", True, (255, 255, 255))
        screen.blit(texto_cmy, (50, 500))
    
    elif modo_cor == "HSV":
        cor_hsv = rgb_para_hsv(cor_rgb)
        texto_hsv = fonte.render(f"HSV: {cor_hsv}", True, (255, 255, 255))
        screen.blit(texto_hsv, (50, 500))

    pygame.display.flip()

def main():
    global cor_rgb, modo_cor
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_r:
                    cor_rgb = (255, 0, 0)
                elif event.key == pygame.K_g:
                    cor_rgb = (0, 255, 0)
                elif event.key == pygame.K_b:
                    cor_rgb = (0, 0, 255)
                elif event.key == pygame.K_c:
                    modo_cor = "CMY"
                elif event.key == pygame.K_h:
                    modo_cor = "HSV"
                elif event.key == pygame.K_m:
                    modo_cor = "RGB"

        desenha_interface()
    pygame.quit()

if __name__ == "__main__":
    main()