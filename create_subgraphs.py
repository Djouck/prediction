# We want to create a function that creates subgraphs of instance graphs
import csv
import pandas as pd


# We need to open the csv file and access the status_ALL column
df = pd.read_csv('PrepaidTravelCost.csv')

status = df['Status_ALL'].tolist()
#print(type(status))
#print(list_status)

prova = status[23]
print(type(prova))

mapping = pd.read_csv('mapping.csv')
# devo capire come trasformare prova in dict
for key in prova.keys():
    print(key)
    #graph = mapping.loc[mapping["case:Rfp-id"] == key]["case_number_id_graphs"]
    #print(graph)
