class calculator:
    """calculator class docstring"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """static dotproduct method"""
        dot = 0
        for x, y in zip(V1, V2):
            dot += x * y
        print(f"Doc product is: {dot}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """static add_vec method"""
        print(f"Add Vector is : {[float(x + y) for x, y in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """static sous_vec method"""
        print(f"Sous Vector is: {[float(x - y) for x, y in zip(V1, V2)]}")
