def square(x: int | float) -> int | float:
    """return square of the input"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """return the power of input itself"""
    return x ** x


def outer(x: int | float, function) -> object:
    """returns a function object inner"""
    count = 0

    def inner() -> float:
        """
        innter function is called everytime outer is called

        use "nonlocal" keyword to make the variable persistant
        """
        nonlocal count
        if count == 0:
            count = x
        count = function(count)
        return count

    return inner
