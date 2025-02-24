from abc import ABC, abstractmethod


class Character(ABC):
    """
    An Abstract base class inherited from ABC
    """
    def __init__(self, name: str, is_alive: bool = True):
        """
        Initializes the character with name and alive or not

        :param name: The first name of the character
        :param is_alive: Boolean indicating dead or alive
        """
        self.first_name = name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to handle death"""
        pass


class Stark(Character):
    """Your docstring for Class"""
    def __init__(self, name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(name, is_alive)

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False
