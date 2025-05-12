class Fish:
    def __init__(self, x_coordinate, y_coordinate):
        """
        Initialise un poisson avec ses caractéristiques de base.

        Args:
            x_coordinate (int): Abscisse de la position initiale du poisson.
            y_coordinate (int): Ordonnée de la position initiale du poisson.
        """
        self.age = 0
        self.reproduce_interval = 2  
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.max_age = 5

    def spawn(self, x, y):
        """
        Crée un nouveau poisson à une position donnée.

        Args:
            x (int): Abscisse de la position où le poisson doit apparaître.
            y (int): Ordonnée de la position où le poisson doit apparaître.

        Returns:
            Fish: Un nouvel objet de type `Fish` créé à la position spécifiée.
        """
        return Fish(x, y)
