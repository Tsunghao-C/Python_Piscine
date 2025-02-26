class calculator:
    """Class docstring here"""
    def __init__(self, array=[]):
        """calculator constructor docstring"""
        self.array = array

    def __add__(self, object) -> None:
        """vector addition with a scalar"""
        self.array = [x + object for x in self.array]
        print(self.array)

    def __mul__(self, object) -> None:
        """vector multiplication with a scalar"""
        self.array = [x * object for x in self.array]
        print(self.array)

    def __sub__(self, object) -> None:
        """vector subtraction with a scalar"""
        self.array = [x - object for x in self.array]
        print(self.array)

    def __truediv__(self, object) -> None:
        """vector division with a scalar"""
        if object == 0:
            print("ValueError: cannot divide by zero")
            return None
        self.array = [x / object for x in self.array]
        print(self.array)

# Dunder methods (double underscore) __init__, __str__, __add__
# They are called by many Python built-in functions, similar to
# C++ operator overload that developer can customize behaviors

# This exercise is overloading the + - * / operators using
# Dunder Methods
