from load_csv import load
import sys
import matplotlib.pyplot as plt


def main():
    """
    Take one input argument (str), and draw the life expectancy graph
    """
    try:
        # input check
        if len(sys.argv) != 2:
            raise AssertionError("Bad input, need one argument")

        # value check
        country = str(sys.argv[1]).title()

        # load data
        data = load("life_expectancy_years.csv")
        # cannot use "if not data" because data is a pd.DataFrame type
        if data.empty:
            raise AssertionError("Failed to load source data")

        # retrieve required data
        if 'country' not in data.columns:
            raise AssertionError("Column 'country' not found")
        data_y = data[data['country'].str.title() == country]
        if data_y.empty:
            raise AssertionError(f"{country} data not found")

        # make the plot
        data_y = data_y.iloc[:, 1:].T
        data_y.columns = ['Life Expectancy']
        data_y.plot(
            title=f"{country} Life expectancy Projections",
            ylabel="Life expectancy",
            xlabel="Year",
            legend=None
        )
        print(data_y)
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
