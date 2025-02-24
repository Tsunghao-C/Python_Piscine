from load_csv import load
import sys
import matplotlib.pyplot as plt


def main():
    """
    Take two input arguments: The coutries you want to compare
    It will call the data from "life_expectancy_years.csv, and then
    draw a line chart if the data is available in the datasource.
    """
    try:
        # input check
        if len(sys.argv) != 3:
            raise AssertionError("Bad input, need two arguments")
        # This check is not necessary since all input are string
        if not all(isinstance(c, str) for c in sys.argv[1:]):
            raise AssertionError("Bad input, must all be string")
        # value check
        country_list = [c.title() for c in sys.argv[1:]]

        # load data
        data = load("life_expectancy_years.csv")
        if data.empty:
            raise AssertionError("Failed to load source data")
        if 'country' not in data.columns:
            raise AssertionError("Column 'country not found")
        
        print("here")
        print(type(data['country'].str.title()))
        # retrieve requested data
        data_y = data[data['country'].str.title().isin(country_list)]
        print(data_y)
    except AssertionError as e:
        print("AssertionError:", e)
    except ValueError as e:
        print("ValueError:", e)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        plt.close()

if __name__ == "__main__":
    main()
