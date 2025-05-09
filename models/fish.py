class Fish:
    def __init__(self, x_coordinate, y_coordinate):
        self.age = 0
        self.reproduce_interval = 2  
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.max_age = 5

    def spawn(self, x, y):
        return Fish(x, y)
