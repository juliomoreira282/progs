import pygame
import sys

pygame.init()

LARGURA, ALTURA = 1200, 700
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Visualização de Camadas Geológicas")
fonte = pygame.font.SysFont("Arial", 16)

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CORES_TERRENO = {
    "Argila": (150, 111, 51),
    "Rocha": (128, 128, 128),
    "Areia": (237, 201, 175),
    "Calcário": (210, 210, 255),
    "Turfa": (85, 60, 42)
}
TIPOS_TERRENO = list(CORES_TERRENO.keys())

class Camada:
    def __init__(self, vertices, tipo_terreno, elevacao):
        self.vertices = vertices
        self.tipo_terreno = tipo_terreno
        self.cor = CORES_TERRENO[tipo_terreno]
        self.elevacao = elevacao

    def mover(self, dx, dy):
        self.vertices = [(x + dx, y + dy) for (x, y) in self.vertices]

    def desenhar_legenda(self, superficie):
        centro = sum(self.vertices, (0, 0))
        cx = centro[0] / len(self.vertices)
        cy = centro[1] / len(self.vertices)
        texto = fonte.render(f"{self.tipo_terreno} (Z={self.elevacao})", True, PRETO)
        superficie.blit(texto, (cx - texto.get_width() // 2, cy - texto.get_height() // 2))

class ZBuffer:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.z = [[float('inf')] * largura for _ in range(altura)]
        self.cores = [[PRETO] * largura for _ in range(altura)]

    def limpar(self):
        for y in range(self.altura):
            for x in range(self.largura):
                self.z[y][x] = float('inf')
                self.cores[y][x] = PRETO

    def ponto_dentro(self, ponto, vertices):
        x, y = ponto
        dentro = False
        j = len(vertices) - 1
        for i in range(len(vertices)):
            xi, yi = vertices[i]
            xj, yj = vertices[j]
            if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-6) + xi):
                dentro = not dentro
            j = i
        return dentro

    def renderizar(self, camadas):
        for camada in sorted(camadas, key=lambda c: c.elevacao):
            min_x = max(0, int(min(v[0] for v in camada.vertices)))
            max_x = min(self.largura - 1, int(max(v[0] for v in camada.vertices)))
            min_y = max(0, int(min(v[1] for v in camada.vertices)))
            max_y = min(self.altura - 1, int(max(v[1] for v in camada.vertices)))
            for y in range(min_y, max_y + 1):
                for x in range(min_x, max_x + 1):
                    if self.ponto_dentro((x, y), camada.vertices):
                        if camada.elevacao < self.z[y][x]:
                            self.z[y][x] = camada.elevacao
                            self.cores[y][x] = camada.cor

    def desenhar(self, superficie):
        for y in range(self.altura):
            for x in range(self.largura):
                superficie.set_at((x, y), self.cores[y][x])

def desenhar_legenda():
    y_offset = 10
    for tipo, cor in CORES_TERRENO.items():
        pygame.draw.rect(tela, cor, (10, y_offset, 20, 20))
        texto = fonte.render(tipo, True, BRANCO)
        tela.blit(texto, (35, y_offset))
        y_offset += 30

def main():
    relogio = pygame.time.Clock()
    camadas = []
    zbuffer = ZBuffer(LARGURA, ALTURA)
    camada_selecionada = None
    tipo_terreno_atual = 0
    criando = False
    novos_vertices = []

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                elif evento.key == pygame.K_n:
                    criando = True
                    novos_vertices = []
                elif evento.key == pygame.K_RETURN and criando and len(novos_vertices) >= 3:
                    nova_camada = Camada(novos_vertices[:], TIPOS_TERRENO[tipo_terreno_atual], elevacao=5)
                    camadas.append(nova_camada)
                    criando = False
                elif evento.key == pygame.K_BACKSPACE:
                    if camadas:
                        camadas.pop()
                elif evento.key == pygame.K_TAB:
                    tipo_terreno_atual = (tipo_terreno_atual + 1) % len(TIPOS_TERRENO)
                elif evento.key == pygame.K_UP and camada_selecionada:
                    camada_selecionada.elevacao -= 1
                elif evento.key == pygame.K_DOWN and camada_selecionada:
                    camada_selecionada.elevacao += 1
                elif evento.key == pygame.K_RIGHT and camada_selecionada:
                    camada_selecionada.mover(5, 0)
                elif evento.key == pygame.K_LEFT and camada_selecionada:
                    camada_selecionada.mover(-5, 0)
                elif evento.key == pygame.K_s and camadas:
                    camada_selecionada = camadas[-1]

            elif evento.type == pygame.MOUSEBUTTONDOWN and criando:
                novos_vertices.append(evento.pos)

        zbuffer.limpar()
        zbuffer.renderizar(camadas)

        tela.fill(PRETO)
        zbuffer.desenhar(tela)

        for camada in camadas:
            camada.desenhar_legenda(tela)

        if criando and len(novos_vertices) > 1:
            pygame.draw.lines(tela, CORES_TERRENO[TIPOS_TERRENO[tipo_terreno_atual]], False, novos_vertices, 2)

        desenhar_legenda()

        instrucoes = [
            "N: Nova camada (clique nos pontos, ENTER para finalizar)",
            "TAB: Trocar tipo de terreno",
            "← → ↑ ↓: Mover/Alterar elevação da camada selecionada (pressione S para selecionar)",
            "BACKSPACE: Remover última camada",
            "ESC: Sair"
        ]
        for i, linha in enumerate(instrucoes):
            texto = fonte.render(linha, True, BRANCO)
            tela.blit(texto, (LARGURA - 525, 10 + i * 20))

        pygame.display.flip()
        relogio.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()