class Alien:
    health = 3
    total_aliens_created = 1
    def __init__(self, location_x, location_y):
        self.x_coordinate = location_x
        self.y_coordinate = location_y
        self.increment_aliens()
        
    def hit(self):
        self.health -= 1

    def is_alive(self):
        return (self.health > 0)

    def teleport(self, new_location_x, new_location_y):
        self.x_coordinate = new_location_x
        self.y_coordinate = new_location_y

    def collision_detection(self, other_object):
        pass

    def increment_aliens(self):
        Alien.total_aliens_created += 1 

def new_aliens_collection(positions):
    """Function taking a list of position tuples, creating one Alien instance per position.

    :param positions: list - A list of tuples of (x, y) coordinates.
    :return: list - A list of Alien objects.
    """
    return [Alien(position[0], position[1]) for position in positions]
