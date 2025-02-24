from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, name, is_alive=True):
        """Baratheon Constructor"""
        super().__init__(name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """User-Friendly String Representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Developer-Friendly Representation"""
        return self.__str__()

    def die(self):
        """Baratheon die method"""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """User-Friendly String Representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Developer-Friendly Representation"""
        return self.__str__()

    def die(self):
        """Lannister die method"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name, is_alive):
        """Classmethod to create new instance"""
        # A class method received cls (the clas itself) as first argument
        # this allows it to create new instances dynamically
        return cls(name, is_alive)

# Note about decorator in Python
# A 'decorator in Python is a special type of function that allows you to
# modify the behavior of another function or method without changing its
# actual code. It's like an extension you applied to another target function

# You can think of decorator as 'Wrapping a function' with additional
# functionality (ex. logging, auth, timer, etc...)

# Common use cases for decorator:
# 1. Logging: log every time a function is called
# 2. Memoization: Cache the results of expensive function calls
# 3. Acess Control: Restrict function usage based on user roles
# 4. Validation: Check arguments before running a function
