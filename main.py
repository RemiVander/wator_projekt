import pygame
import random
from models.sea import Sea
from models.fish import Fish
from models.shark import Shark
from pygame_display import PygameDisplay 


CELL_SIZE = 20
FPS = 5
WINDOW_TITLE = "Simulation Wator - Pygame"

def init_entities(sea, num_fish=20, num_sharks=5):
    """Ajoute des poissons et des requins à des positions aléatoires dans la mer."""
    for _ in range(num_fish):
        x = random.randint(0, sea.height - 1)
        y = random.randint(0, sea.width - 1)
        fish = Fish(x_coordinate=x, y_coordinate=y)
        sea.add_entity(fish)

    for _ in range(num_sharks):
        x = random.randint(0, sea.height - 1)
        y = random.randint(0, sea.width - 1)
        shark = Shark(x_coordinate=x, y_coordinate=y)
        sea.add_entity(shark)

def main():
    """Fonction principale pour lancer la simulation avec Pygame."""
    width, height = 75, 45
    sea = Sea(width=width, height=height)
    display = PygameDisplay(width=width, height=height, cell_size=20, fps=5)
    init_entities(sea, num_fish=30, num_sharks=5)

    running = True
    while running:
        if not display.handle_events():
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            sea = Sea(width=width, height=height)
            init_entities(sea, num_fish=30, num_sharks=5)
            display.population_history.clear()
            display.paused = False

        if not display.paused:
            sea.update()

        display.draw(sea.sea)
        display.tick()

    display.close()


if __name__ == "__main__":
    main()
