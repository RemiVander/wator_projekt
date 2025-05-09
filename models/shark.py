from models.fish import Fish

class Shark(Fish):
    def __init__(self, x_coordinate, y_coordinate):
        super().__init__( x_coordinate, y_coordinate)
        self.energy = 9
        self.max_age = 12
        self.reproduce_interval = 10

    
    def spawn(self, x, y):
        return Shark(x, y)