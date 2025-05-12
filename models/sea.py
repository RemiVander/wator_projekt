from models.fish import Fish
from models.shark import Shark
import random

class Sea:

    def __init__(self, width=50, height=30):
        """Initialisation de la grille qui représente la mer

        Args:
            width (int, optional): fixée par défaut à  50.
            height (int, optional): _fixeé par défaut à 30.
        """
        self.width = width
        self.height = height
        self.sea = [[None for _ in range(self.width)] for _ in range(self.height)]

    def wrap_coordinates(self, x, y):
        """Permet de déplacer l'entité autour de la grille, dans un environnement toroîdal

        Args:
            x (int): abscisse
            y (int): ordonnées

        Returns:
            int: nouvelles coordonnées mise à jour au besoin avec le tor
        """
        return x % self.height, y % self.width

    def add_entity(self, entity):
        """Ajoute une nouvelle entité à la grille

        Args:
            entity (_type_): la nouvelle entité à créer

        Returns: une nouvelle entité du type défini dans l'objet, aux coordonnées de l'objet
        """
        x, y = self.wrap_coordinates(entity.x_coordinate, entity.y_coordinate)
        if self.sea[x][y] is None:
            self.sea[x][y] = entity

    def print_sea(self):
        """Affichage de la grille en fonction des objets qui se trouvent dans les différentes cellules.
        Chaque type d'entité est représenté par un symbole spécifique.
        """
        print('\n' + '🪸 ' * self.width + '\n')
        for row in self.sea:
            for cell in row:
                if cell is None:
                    print('\033[44m🌊\033[0m', end='')
                elif isinstance(cell, Fish) and not isinstance(cell, Shark):
                    print('\033[43m🐟\033[0m', end='')
                elif isinstance(cell, Shark):
                    print('\033[41m🦈\033[0m', end='')
                else:
                    print(f'\033[45m{type(cell).__name__[0]}\033[0m ', end='')
            print()

    def get_empty_neighbors(self, x, y, sea_snapshot, distance=1):
        """
        Retourne les voisins vides (cellules sans entité) autour de la position donnée 
        dans un rayon spécifié.

        Args:
            x (int): Abscisse de la cellule de départ.
            y (int): Ordonnée de la cellule de départ.
            sea_snapshot (list): Représentation actuelle de la mer.
            distance (int, optional): Distance maximale (en cellules) pour chercher les voisins (par défaut 1).

        Returns:
            list: Liste de tuples représentant les coordonnées des voisins vides.
        """
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        neighbors = []
        for dx, dy in directions:
            for step in range(1, distance+1):
                nx = (x + dx * step) % self.height
                ny = (y + dy * step) % self.width
                if sea_snapshot[nx][ny] is None and self.sea[nx][ny] is None:
                    neighbors.append((nx, ny))
        random.shuffle(neighbors)
        return neighbors

    def get_fish_neighbors(self, x, y, distance=1):
        """
        Retourne les voisins qui sont des poissons (et non des requins) autour de la position donnée 
        dans un rayon spécifié.

        Args:
            x (int): Abscisse de la cellule de départ.
            y (int): Ordonnée de la cellule de départ.
            distance (int, optional): Distance maximale (en cellules) pour chercher les poissons voisins (par défaut 1).

        Returns:
            list: Liste de tuples représentant les coordonnées des poissons voisins.
        """
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        fish_neighbors = []
        for dx, dy in directions:
            for step in range(1, distance+1):
                nx = (x + dx * step) % self.height
                ny = (y + dy * step) % self.width
                if isinstance(self.sea[nx][ny], Fish) and not isinstance(self.sea[nx][ny], Shark):
                    fish_neighbors.append((nx, ny))
        random.shuffle(fish_neighbors)
        return fish_neighbors

    def move_entity(self, entity, new_x, new_y, grid):
        """
        Déplace une entité à une nouvelle position sur la grille, en prenant en compte 
        les règles d'âge, de reproduction et d'énergie des entités.

        Args:
            entity (Entity): L'entité à déplacer.
            new_x (int): Nouvelle abscisse où déplacer l'entité.
            new_y (int): Nouvelle ordonnée où déplacer l'entité.
            grid (list): La grille de la mer représentant l'état actuel de la mer.

        Returns:
            None: La fonction modifie directement la grille et l'entité.
        """
        old_x, old_y = self.wrap_coordinates(entity.x_coordinate, entity.y_coordinate)
        new_x, new_y = self.wrap_coordinates(new_x, new_y)
        target = self.sea[new_x][new_y]
        entity.age += 1

        if entity.age >= entity.max_age:
            self.sea[old_x][old_y] = None
            return

        if isinstance(entity, Shark):
            if isinstance(target, Fish) and not isinstance(target, Shark):
                entity.energy += 5
            elif target is not None:
                return
        elif isinstance(entity, Fish):
            if target is not None:
                return

        if grid[new_x][new_y] is None:
            if entity.age % entity.reproduce_interval != 0:
                grid[new_x][new_y] = entity
            else:
                new_entity = entity.spawn(old_x, old_y)
                new_entity.age = 0
                grid[old_x][old_y] = new_entity
                grid[new_x][new_y] = entity
                entity.age = 0
            entity.x_coordinate, entity.y_coordinate = new_x, new_y
            self.sea[old_x][old_y] = None

    def update(self):
        """
        Met à jour l'état de la mer en faisant évoluer les entités selon leurs comportements 
        (déplacement, reproduction, vieillissement, etc.).

        Ce processus inclut la gestion de l'énergie des requins, le déplacement des poissons, 
        ainsi que la mise à jour de la grille avec les nouvelles positions des entités.
        """
        new_sea = [[None for _ in range(self.width)] for _ in range(self.height)]
        for x in range(self.height):
            for y in range(self.width):
                entity = self.sea[x][y]
                if entity is None:
                    continue
                if new_sea[x][y] is not None:
                    continue
                if isinstance(entity, Shark):
                    entity.energy -= 1
                    if entity.energy <= 0 or entity.age >= entity.max_age:
                        continue
                    fish_targets = self.get_fish_neighbors(x, y, distance=1)
                    if fish_targets:
                        new_x, new_y = fish_targets[0]
                    else:
                        empty_moves = self.get_empty_neighbors(x, y, new_sea, distance=1)
                        if empty_moves:
                            new_x, new_y = empty_moves[0]
                        else:
                            new_x, new_y = x, y
                    self.move_entity(entity, new_x, new_y, new_sea)
                elif isinstance(entity, Fish):
                    if entity.age >= entity.max_age:
                        continue
                    empty_moves = self.get_empty_neighbors(x, y, new_sea, distance=1)
                    if empty_moves:
                        new_x, new_y = empty_moves[0]
                    else:
                        new_x, new_y = x, y
                    self.move_entity(entity, new_x, new_y, new_sea)
        self.sea = new_sea
