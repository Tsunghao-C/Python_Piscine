from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


def thousand_formatter(x, pos):
    """
    retrun number in thousands end with 'k'
    """
    return f'{x / 1000:.0f}k'


def main():
    """
    print scatter plot at year 1900
    """
    try:
        # load data
        in_path = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        df_life = load("life_expectancy_years.csv")
        df_income = load(in_path)
        if df_life.empty or df_income.empty:
            raise AssertionError("Failed to load Data")
        # print(df_life.head())
        # print(df_income.head())

        # set get the year 1900 data and combine dataframe
        # print(df_life['1900'].dtype)
        # print(df_income['1900'].dtype)
        # df_life = df_life.loc[:, ['country', '1900']]
        # df_income = df_income.loc[:, ['country', '1900']]
        df = df_life.loc[:, ['country', '1900']]
        df.columns = ['country', 'Life Expectancy']
        df['Gross domestic product'] = df_income[['1900']]

        # filter all the rows with NaN
        # print(df.isna().sum())
        # print(df[df['Life Expectancy'].isna()])
        df.dropna(inplace=True)
        # print(df.isna().sum())

        # draw the scatter plot
        fig, ax = plt.subplots()
        ax.scatter(df.iloc[:, 2], df.iloc[:, 1])
        plt.xscale('log')
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(thousand_formatter))
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.title('1900')
        plt.show()

    except AssertionError as e:
        print("AssertionError", e)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        plt.close()


if __name__ == "__main__":
    main()
