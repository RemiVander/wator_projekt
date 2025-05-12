
class Trawler:
    """
    Représente un chalutier qui se déplace horizontalement dans la mer
    et détruit les poissons sur son passage.

    Attributes:
        x (int): Ligne du chalutier dans la grille.
        y (int): Colonne actuelle du chalutier.
        direction (int): Direction du déplacement (1 pour droite, -1 pour gauche).
    """

    def __init__(self, x=0, y=0, direction=1):
        """
        Initialise le chalutier avec sa position et sa direction.

        Args:
            x (int): Ligne où le chalutier commence (défaut: 0).
            y (int): Colonne initiale (défaut: 0).
            direction (int): Direction de déplacement (1 pour droite, -1 pour gauche).
        """
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, width):
        """
        Déplace le chalutier horizontalement sur une ligne,
        en tenant compte du rebouclage (mer torique).

        Args:
            width (int): Largeur de la mer.
        """
        self.y += self.direction
