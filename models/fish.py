class Fish:
    def __init__(self,reproduce, x_coordinate, y_coordinate):
        self.age = 1
        self.reproduce = reproduce
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def spawn(self, x, y):
        return Fish(x, y, self.reproduce)