from models.fish import Fish
from models.shark import Shark

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
                    print('\033[44m🌊\033[0m ', end='')
                elif isinstance(cell, Fish):
                    print('\033[43m🐟\033[0m ', end='')
                elif isinstance(cell, Shark):
                    print('\033[41m🦈\033[0m ', end='')
                else:
                    print(f'\033[45m{type(cell).__name__[0]}\033[0m ', end='')
            print()