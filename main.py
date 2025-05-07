import time
import random
from models.sea import Sea
from models.fish import Fish
from models.shark import Shark

def init_entities(sea, num_fish=10, num_sharks=5):
    """Ajoute des poissons et des requins à des positions aléatoires dans la mer."""
    for _ in range(num_fish):
        x = random.randint(0, sea.height - 1)
        y = random.randint(0, sea.width - 1)
        fish = Fish(reproduce=4, x_coordinate=x, y_coordinate=y)
        sea.add_entity(fish)

    for _ in range(num_sharks):
        x = random.randint(0, sea.height - 1)
        y = random.randint(0, sea.width - 1)
        shark = Shark(reproduce=8, x_coordinate=x, y_coordinate=y)
        sea.add_entity(shark)

def main():
    my_sea = Sea() 
    init_entities(my_sea, num_fish=20, num_sharks=5)

    try:
        while True:
            my_sea.print_sea()
            my_sea.update()
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nSimulation arrêtée.")

if __name__ == "__main__":
    main()
