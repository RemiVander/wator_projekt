from models.fish import Fish

class Shark(Fish):
    def __init__(self, x_coordinate, y_coordinate):
        """
        Initialise un requin avec ses caractéristiques spécifiques, tout en héritant des propriétés de la classe `Fish`.

        Args:
            x_coordinate (int): Abscisse de la position initiale du requin.
            y_coordinate (int): Ordonnée de la position initiale du requin.
        """
        super().__init__( x_coordinate, y_coordinate)
        self.energy = 9
        self.max_age = 12
        self.reproduce_interval = 10

    
    def spawn(self, x, y):
        """
        Crée un nouveau requin à une position donnée.

        Args:
            x (int): Abscisse de la position où le requin doit apparaître.
            y (int): Ordonnée de la position où le requin doit apparaître.

        Returns:
            Shark: Un nouvel objet de type `Shark` créé à la position spécifiée.
        """
        return Shark(x, y)