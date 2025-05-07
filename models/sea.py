from models.fish import Fish
from models.shark import Shark
import random

class Sea:

    def __init__(self, width=50, height=30):
        self.width = width
        self.height = height
        self.sea = [[None for _ in range(self.width)] for _ in range(self.height)]

    def wrap_coordinates(self, x, y):
        return x % self.height, y % self.width

    def add_entity(self, entity):
        x, y = self.wrap_coordinates(entity.x_coordinate, entity.y_coordinate)
        if self.sea[x][y] is None:
            self.sea[x][y] = entity

    def move_entity(self, entity, new_x, new_y, grid):
        old_x, old_y = self.wrap_coordinates(entity.x_coordinate, entity.y_coordinate)
        new_x, new_y = self.wrap_coordinates(new_x, new_y)
        entity.age += 1

        target_entity = self.sea[new_x][new_y]
        if isinstance(entity, Shark) and isinstance(target_entity, Fish):
            entity.energy += 2 
            self.sea[new_x][new_y] = None 
        if grid[new_x][new_y] is None:
            if entity.age < entity.reproduce:
                grid[new_x][new_y] = entity
            elif entity.age == entity.reproduce:
                new_entity = entity.spawn(old_x, old_y)
                new_entity.age = 0
                grid[old_x][old_y] = new_entity
                grid[new_x][new_y] = entity
                entity.age = 0
            entity.x_coordinate, entity.y_coordinate = new_x, new_y

    def get_entity(self, x, y):
        x, y = self.wrap_coordinates(x, y)
        return self.sea[x][y]

    def print_sea(self):
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

    def get_random_empty_neighbor(self, x, y, sea_snapshot):
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx = (x + dx) % self.height
            ny = (y + dy) % self.width
            if sea_snapshot[nx][ny] is None and self.sea[nx][ny] is None:
                return nx, ny
        return x, y

    def find_nearest_fish(self, shark):
        min_dist = float('inf')
        nearest = None
        for row in self.sea:
            for cell in row:
                if isinstance(cell, Fish) and not isinstance(cell, Shark):
                    dist = ((shark.x_coordinate - cell.x_coordinate) ** 2 +
                            (shark.y_coordinate - cell.y_coordinate) ** 2) ** 0.5
                    if dist < min_dist:
                        min_dist = dist
                        nearest = cell
        return nearest 

    def get_step_towards(self, x1, y1, x2, y2):
        dx = (x2 - x1)
        dy = (y2 - y1)
        step_x = 0 if dx == 0 else int(dx / abs(dx))
        step_y = 0 if dy == 0 else int(dy / abs(dy))
        return self.wrap_coordinates(x1 + step_x, y1 + step_y)

    def update(self):
        new_sea = [[None for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.height):
            for y in range(self.width):
                entity = self.sea[x][y]

                if isinstance(entity, Fish) and not isinstance(entity, Shark):
                    new_x, new_y = self.get_random_empty_neighbor(x, y, new_sea)
                    self.move_entity(entity, new_x, new_y, new_sea)

                elif isinstance(entity, Shark):
                    entity.energy -= 1
                    if entity.energy <= 0:
                        continue 

                    target = self.find_nearest_fish(entity)
                    if target:
                        dx = target.x_coordinate - entity.x_coordinate
                        dy = target.y_coordinate - entity.y_coordinate
                        step_x = entity.x_coordinate + (1 if dx > 0 else -1 if dx < 0 else 0)
                        step_y = entity.y_coordinate + (1 if dy > 0 else -1 if dy < 0 else 0)

                        step_x, step_y = self.wrap_coordinates(step_x, step_y)

                        target_cell = self.sea[step_x][step_y]

                        if isinstance(target_cell, Fish) and not isinstance(target_cell, Shark):
                            entity.energy += 4
                            self.sea[step_x][step_y] = None  
                            self.move_entity(entity, step_x, step_y, new_sea)
                        elif new_sea[step_x][step_y] is None and self.sea[step_x][step_y] is None:
                            self.move_entity(entity, step_x, step_y, new_sea)
                        else:
                            self.move_entity(entity, x, y, new_sea)
                    else:
                        new_x, new_y = self.get_random_empty_neighbor(x, y, new_sea)
                        self.move_entity(entity, new_x, new_y, new_sea)

        self.sea = new_sea
