from models.fish import Fish
from models.shark import Shark
import random

class Sea:

    def __init__(self, width = 50, height = 30):
        self.width = width
        self.height = height
        self.sea = [[None for i in range(self.width)] for j in range(self.height)]

    
    def wrap_coordinates(self, x, y):
        return x % self.height , y % self.width

    def add_entity(self, entity):
        x, y = self.wrap_coordinates(entity.x_coordinate, entity.y_coordinate)
        if self.sea[x][y] is None :
            self.sea[x][y] = entity
        else:
            pass
    
    def move_entity(self, entity, new_x, new_y):
        old_x, old_y = self.wrap_coordinates(entity.x_coordinate, entity.y_coordinate)
        new_x, new_y = self.wrap_coordinates(new_x, new_y)
        entity.age += 1
        if self.sea[new_x][new_y] is None:
            if entity.age != entity.reproduce:
                self.sea[old_x][old_y] = None
                self.sea[new_x][new_y] = entity
            if entity.age == entity.reproduce:
                self.sea[old_x][old_y] = self.add_entity(entity)
                self.sea[new_x][new_y] = entity
            entity.x_coordinate, entity.y_coordinate = new_x, new_y
        else:
            pass

    def get_entity(self, x, y):
        x, y = self.wrap_coordinates(x, y)
        return self.sea[x][y]
    
    def print_sea(self):
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

    def get_random_empty_neighbor(self, x, y, sea_snapshot):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx = (x + dx) % self.height
            ny = (y + dy) % self.width
            if sea_snapshot[nx][ny] is None:
                return nx, ny
        return x, y

    def find_nearest_fish(self, shark):
        min_dist = float('inf')
        nearest = None
        for row in self.sea:
            for cell in row:
                if isinstance(cell, Fish):
                    dist = ((shark.x_coordinate - cell.x_coordinate) ** 2 +
                            (shark.y_coordinate - cell.y_coordinate) ** 2) ** 0.5
                    if dist < min_dist:
                        min_dist = dist
                        nearest = cell
        return nearest 

    def update(self):
        new_sea = [[None for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.height):
            for y in range(self.width):
                entity = self.sea[x][y]
                if isinstance(entity, Fish) and not isinstance(entity, Shark):
                    new_x, new_y = self.get_random_empty_neighbor(x, y, new_sea)
                    entity.x_coordinate = new_x
                    entity.y_coordinate = new_y
                    new_sea[new_x][new_y] = entity

        for x in range(self.height):
            for y in range(self.width):
                entity = self.sea[x][y]
                if isinstance(entity, Shark):
                    entity.energy -= 1
                    if entity.energy <= 0:
                        continue
                    target = self.find_nearest_fish(entity)
                    if target:
                        new_x, new_y = target.x_coordinate, target.y_coordinate
                        entity.energy += 2
                        new_sea[new_x][new_y] = entity
                    else:
                        new_x, new_y = self.get_random_empty_neighbor(x, y, new_sea)
                        entity.x_coordinate = new_x
                        entity.y_coordinate = new_y
                        new_sea[new_x][new_y] = entity

        self.sea = new_sea