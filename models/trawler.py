class Trawler:
    def __init__(self, x, y, direction, radius=2):
        """
        Initialise le chalutier.
        
        Args:
            x (int): Position verticale
            y (int): Position horizontale
            direction (int): +1 (vers la droite) ou -1 (vers la gauche)
            radius (int): Rayon d'effet du chalutier (zone = (2*radius + 1)^2)
        """
        self.x = x
        self.y = y
        self.direction = direction
        self.radius = radius

    def move(self, width):
        """Fait avancer le chalutier horizontalement d'une case selon sa direction."""
        self.y += self.direction
        if self.y < 0 or self.y >= width:
            # Le chalutier quitte la grille
            self.y = -1
