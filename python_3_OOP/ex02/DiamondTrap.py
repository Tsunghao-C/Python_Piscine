from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King is a mixed blood"""
    def __init__(self, name, is_alive=True):
        """King Constructor"""
        super().__init__(name, is_alive)

    def set_eyes(self, color: str):
        """eyes setter method"""
        self.eyes = color

    def set_hairs(self, color: str):
        """hairs setter method"""
        self.hairs = color

    def get_eyes(self):
        """eyes getter method"""
        return self.eyes

    def get_hairs(self):
        """hairs getter method"""
        return self.hairs
