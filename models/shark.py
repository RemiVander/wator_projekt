from models.fish import Fish

class Shark(Fish):
    def __init__(self,reproduce, x_coordinate, y_coordinate):
        super().__init__(reproduce, x_coordinate, y_coordinate)
        self.energy = 5