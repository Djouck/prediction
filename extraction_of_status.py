import csv
import pandas as pd

#example
filename = 'PrepaidTravelCost.csv'
outputname = 'mapping.csv'

df = pd.read_csv(filename)

mapping = df[["case:Rfp-id", "case_number_id_graphs"]].drop_duplicates()
print(mapping)

for i in range(len(df)):
    print(df.loc[i]['Status_ALL'])

mapping.to_csv(outputname)
