def callLimit(limit: int):
    """decorater function to limit the called times"""
    count = 0

    def callLimiter(function):
        """1st tier decorator wrapping the target func"""
        def limit_function(*args: any, **kwds: any):
            """2nd tier decorator taking the arguments of target func"""
            nonlocal count
            count += 1
            if count > limit:
                print(f"Error: {function} call too many times")
                return None
            return function(*args, **kwds)
        return limit_function
    return callLimiter

# Decorator uses "Wrapper" to modify the behavior of other function
# It take the target func object as argument, and wrapp it up
# to add more rules or behaviour before returning the original func
