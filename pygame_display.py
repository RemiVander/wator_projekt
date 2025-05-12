import pygame
from models.fish import Fish
from models.shark import Shark
from models.trawler import Trawler 

# Couleurs
BLUE = (0, 105, 148)    # Mer
YELLOW = (255, 255, 0)  # Poisson
RED = (255, 0, 0)       # Requin

class PygameDisplay:
    def __init__(self, width, height, cell_size=20, fps=5, title="Simulation Wator - Pygame"):
        """Initialise la fenêtre Pygame."""
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.sidebar_width = 180
        self.fps = fps
        self.title = title
        self.paused = False

        # Chargement des images
        self.fish_image = pygame.transform.scale(pygame.image.load("assets/fish.png"), (cell_size, cell_size))
        self.shark_image = pygame.transform.scale(pygame.image.load("assets/shark.png"), (cell_size, cell_size))
        self.trawler_image = pygame.transform.scale(pygame.image.load("assets/trawler.png"), (cell_size, cell_size))
        self.water_image = pygame.Surface((cell_size, cell_size))
        self.water_image.fill(BLUE)

        # Initialisation Pygame
        pygame.init()
        self.screen = pygame.display.set_mode(
            ((width * cell_size) + self.sidebar_width, height * cell_size)
        )
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def draw(self, sea_grid):
        """Dessine la grille de la mer."""
        self.screen.fill((0, 0, 0))  # Clear screen

        for x in range(len(sea_grid)):
            for y in range(len(sea_grid[0])):
                rect = pygame.Rect(y * self.cell_size, x * self.cell_size, self.cell_size, self.cell_size)
                entity = sea_grid[x][y]

                self.screen.blit(self.water_image, rect.topleft)  # Fond bleu pour images transparentes

                if isinstance(entity, Fish) and not isinstance(entity, Shark):
                    self.screen.blit(self.fish_image, rect.topleft)
                elif isinstance(entity, Shark):
                    self.screen.blit(self.shark_image, rect.topleft)
                elif isinstance(entity, Trawler):
                    self.screen.blit(self.trawler_image, rect.topleft)

        pygame.display.flip()

    def tick(self):
        """Limite le framerate."""
        self.clock.tick(self.fps)

    def handle_events(self):
        """Gère les événements Pygame."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
        return True

    def close(self):
        """Ferme proprement Pygame."""
        pygame.quit()
