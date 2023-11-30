import pandas as pd

dates = ["April-10", "April-11", "April-12", "April-13", "April-14", "April-16"]
income1 = [10, 20, 10, 15, 10, 12]
income2 = [20, 30, 10, 5, 40, 13]

df = pd.DataFrame({"Date": dates, "Income_1": income1, "Income_2": income2})

for i in df.index:
    print(
        "Total income in "
        + df["Date"][i]
        + " is:"
        + str(df["Income_1"][i] + df["Income_2"][i])
    )

import pandas as pd

dates = ["April-10", "April-11", "April-12", "April-13", "April-14", "April-16"]
income1 = [10, 20, 10, 15, 10, 12]
income2 = [20, 30, 10, 5, 40, 13]

df = pd.DataFrame({"Date": dates, "Income_1": income1, "Income_2": income2})

for i in range(len(df)):
    print(
        "Total income in "
        + df.loc[i, "Date"]
        + " is:"
        + str(df.loc[i, "Income_1"] + df.loc[i, "Income_2"])
    )

import pandas as pd

dates = ["April-10", "April-11", "April-12", "April-13", "April-14", "April-16"]
income1 = [10, 20, 10, 15, 10, 12]
income2 = [20, 30, 10, 5, 40, 13]

df = pd.DataFrame({"Date": dates, "Income_1": income1, "Income_2": income2})

for i in range(len(df)):
    print(
        "Total income in " + df.iloc[i, 0] + " is:" + str(df.iloc[i, 1] + df.iloc[i, 2])
    )

import pandas as pd

dates = ["April-10", "April-11", "April-12", "April-13", "April-14", "April-16"]
income1 = [10, 20, 10, 15, 10, 12]
income2 = [20, 30, 10, 5, 40, 13]

df = pd.DataFrame({"Date": dates, "Income_1": income1, "Income_2": income2})


for index, row in df.iterrows():
    print(
        "Total income in "
        + row["Date"]
        + " is:"
        + str(row["Income_1"] + row["Income_2"])
    )