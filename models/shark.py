from models.fish import Fish

class Shark(Fish):
    def __init__(self,reproduce, x_coordinate, y_coordinate,energy):
        super().__init__(reproduce, x_coordinate, y_coordinate)
        self.energy = energy