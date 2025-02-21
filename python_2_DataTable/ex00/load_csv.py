import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load csv file
    """
    try:
        if not path or not isinstance(path, str):
            raise AssertionError("bad input")
        if not path.lower().endswith(".csv"):
            raise AssertionError("bad input, only accept .csv")
        loaded_data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {loaded_data.shape}")
        return loaded_data
    except AssertionError as e:
        print("AssertionError:", e)
    except FileNotFoundError as e:
        print("FileNotFound:", e)
    return None
