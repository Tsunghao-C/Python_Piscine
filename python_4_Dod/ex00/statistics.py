class Statistics():
    """Class that do no instatiate and do statistic calculations"""
    @staticmethod
    def mean(arr: list[int | float]) -> float:
        """returns mean of the arr"""
        if not arr:
            raise ValueError("Empty list")
        return sum(arr) / len(arr)

    @staticmethod
    def median(arr: list[int | float]) -> float | int:
        """returns median value of the sorted arr"""
        if not arr:
            raise ValueError("Empty list")
        arr = sorted(arr)
        n = len(arr)
        mid = n // 2
        return (arr[mid] if n % 2 != 0 else (arr[mid - 1] + arr[mid]) / 2)

    @staticmethod
    def quartile(arr: list[int | float]) -> list[float, float]:
        """returns the range from 1/4 to 3/4 of the arr"""
        if not arr:
            raise ValueError("Empty list")
        arr = sorted(arr)
        n = len(arr)
        quar_1 = float(arr[n // 4])
        quar_3 = float(arr[(n * 3) // 4])
        return [quar_1, quar_3]

    @staticmethod
    def std(arr: list[int | float]) -> float:
        """returns standard deviation of the arr"""
        if not arr:
            raise ValueError("Empty list")
        mean = sum(arr) / len(arr)
        var = sum((x - mean) ** 2 for x in arr) / len(arr)
        return var ** 0.5

    @staticmethod
    def var(arr: list[int | float]) -> float:
        """returns the variance of the arr"""
        if not arr:
            raise ValueError("Empty list")
        mean = sum(arr) / len(arr)
        return sum((x - mean) ** 2 for x in arr) / len(arr)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """
    Display Statistics

    1. *args: an unkown quantity of numbers as input data
    2. **kwargs: an unknown quantity of key and value pairs
    to find the statistical metrics
    """
    stats_map = {
        "mean": Statistics.mean,
        "median": Statistics.median,
        "quartile": Statistics.quartile,
        "std": Statistics.std,
        "var": Statistics.var
    }

    for x in kwargs.values():
        func = stats_map.get(x)
        if func:
            try:
                print(f"{x} : {func(list(args))}")
            except ValueError:
                print("Error")
