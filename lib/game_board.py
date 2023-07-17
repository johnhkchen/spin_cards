from lib.ring import Ring


class GameBoard:
    def __init__(self, p1_rings, p2_rings):
        self.p1_rings = p1_rings
        self.p2_rings = p2_rings
        self.rings = {
            "p1": {
                "attack": Ring(p1_rings[0]),
                "defense": Ring(p1_rings[1]),
                "health": Ring(p1_rings[2]),
            },
            "p2": {
                "attack": Ring(p2_rings[0]),
                "defense": Ring(p2_rings[1]),
                "health": Ring(p2_rings[2]),
            },
        }

    def rotate_ring(self, player, ring, n=1, reverse=False):
        self.rings[player][ring].rotate(n, reverse)
