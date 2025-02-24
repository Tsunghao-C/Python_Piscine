from load_csv import load
import sys
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def convert_pop(value):
    """
    convert string type population into numbers
    """
    if isinstance(value, str):
        if 'M' in value:
            return float(value.replace('M', '')) * 1e6
        elif 'k' in value:
            return float(value.replace('k', '')) * 1e3
    return value


def millions_formatter(x, pos):
    """
    Used by matplotlib.ticker.FuncFormatter to dynamically format
    the y-axis lables.

    'x' parameter represents the tick value
    'pos' parameter represents the tick position (not used here)
    """
    return f'{x / 1_000_000:.0f}M'


def main():
    """
    Take two input arguments: The coutries you want to compare
    It will call the data from "population_total.csv, and then
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
        data = load("population_total.csv")
        if data.empty:
            raise AssertionError("Failed to load source data")
        if 'country' not in data.columns:
            raise AssertionError("Column 'country not found")

        # Convert data into numbers
        data.iloc[:, 1:] = data.iloc[:, 1:].applymap(convert_pop)
        data.columns = ['country'] + [int(col) for col in data.columns[1:]]
        # print(data.head())

        # retrieve requested data: select rows
        data_y = data[data['country'].str.title().isin(country_list)]
        # Select columns up to year 2050
        data_y = data_y.loc[:, 'country':2050]

        # DataTable manipulation before plotting
        df = data_y.set_index("country").T
        print(df)
        # Make the plot with y-ticker formatted
        fig, ax = plt.subplots()
        ax.plot(df)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter))
        plt.ylabel("Population")
        plt.xlabel("Year")
        plt.title("Population Projection")
        plt.legend(country_list)
        plt.show()

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
