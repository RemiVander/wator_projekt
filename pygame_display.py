import pygame
from models.fish import Fish
from models.shark import Shark
from models.trawler import Trawler

# Couleurs
BLUE = (0, 105, 148)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

class PygameDisplay:
    def __init__(self, width, height, cell_size=20, fps=5, title="Simulation Wator - Pygame"):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.sidebar_width = 220
        self.fps = fps
        self.title = title
        self.paused = False

        # Historique pour les graphes
        self.population_history = []
        self.max_history_length = 300

        # Images
        self.fish_image = pygame.transform.scale(pygame.image.load("assets/fish.png"), (cell_size, cell_size))
        self.shark_image = pygame.transform.scale(pygame.image.load("assets/shark.png"), (cell_size, cell_size))
        self.trawler_image = pygame.transform.scale(pygame.image.load("assets/trawler.png"), (cell_size, cell_size))
        self.water_image = pygame.Surface((cell_size, cell_size))
        self.water_image.fill(BLUE)

        # Init pygame
        pygame.init()
        self.screen = pygame.display.set_mode(
            ((width * cell_size) + self.sidebar_width, height * cell_size)
        )
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 18)

    def draw(self, sea_grid):
        """Affiche la mer et la barre latérale."""
        self.screen.fill((0, 0, 0))

        fish_count, shark_count = 0, 0

        # Affichage des entités
        for x in range(self.height):
            for y in range(self.width):
                rect = pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size)
                entity = sea_grid[x][y]
                self.screen.blit(self.water_image, rect.topleft)

                if isinstance(entity, Fish) and not isinstance(entity, Shark):
                    fish_count += 1
                    self.screen.blit(self.fish_image, rect.topleft)
                elif isinstance(entity, Shark):
                    shark_count += 1
                    self.screen.blit(self.shark_image, rect.topleft)
                elif isinstance(entity, Trawler):
                    self.screen.blit(self.trawler_image, rect.topleft)

        # Enregistrement pour le graphique
        self._update_population_history(fish_count, shark_count)
        self._draw_sidebar(fish_count, shark_count)

        pygame.display.flip()

    def _update_population_history(self, fish, sharks):
        self.population_history.append((fish, sharks))
        if len(self.population_history) > self.max_history_length:
            self.population_history.pop(0)

    def _draw_sidebar(self, fish_count, shark_count):
        """Affiche les stats texte et le graphe sur le côté droit."""
        sidebar_x = self.width * self.cell_size
        pygame.draw.rect(self.screen, (30, 30, 30), (sidebar_x, 0, self.sidebar_width, self.height * self.cell_size))

        # Texte
        fish_text = self.font.render(f"Poissons : {fish_count}", True, YELLOW)
        shark_text = self.font.render(f"Requins  : {shark_count}", True, RED)
        self.screen.blit(fish_text, (sidebar_x + 10, 20))
        self.screen.blit(shark_text, (sidebar_x + 10, 50))

        # Graphique
        graph_x = sidebar_x + 10
        graph_y = 100
        graph_w = self.sidebar_width - 20
        graph_h = 300  # ← Zone plus grande

        pygame.draw.rect(self.screen, (20, 20, 20), (graph_x, graph_y, graph_w, graph_h))

        # Lignes horizontales d’aide
        for i in range(6):
            y = graph_y + i * (graph_h // 5)
            pygame.draw.line(self.screen, (50, 50, 50), (graph_x, y), (graph_x + graph_w, y), 1)

        # Tracé du graphe
        if len(self.population_history) >= 2:
            max_val = max(
                max(f for f, _ in self.population_history),
                max(s for _, s in self.population_history),
                1
            )
            scale_y = graph_h / max_val
            scale_x = graph_w / self.max_history_length

            for i in range(1, len(self.population_history)):
                x1 = graph_x + int((i - 1) * scale_x)
                x2 = graph_x + int(i * scale_x)

                f1, s1 = self.population_history[i - 1]
                f2, s2 = self.population_history[i]

                y1_f = graph_y + graph_h - int(f1 * scale_y)
                y2_f = graph_y + graph_h - int(f2 * scale_y)
                y1_s = graph_y + graph_h - int(s1 * scale_y)
                y2_s = graph_y + graph_h - int(s2 * scale_y)

                pygame.draw.line(self.screen, YELLOW, (x1, y1_f), (x2, y2_f), 2)
                pygame.draw.line(self.screen, RED, (x1, y1_s), (x2, y2_s), 2)

    def tick(self):
        self.clock.tick(self.fps)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
        return True

    def close(self):
        pygame.quit()
