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

prova1 = {
    'request for payment 73550': ['START', 'PermitSUBMITTEDbyEMPLOYEE', 'PermitFINAL-APPROVEDbySUPERVISOR'],
    'request for payment 73552': ['START', 'PermitSUBMITTEDbyEMPLOYEE', 'PermitFINAL-APPROVEDbySUPERVISOR'],
    'request for payment 76316': ['START', 'PermitSUBMITTEDbyEMPLOYEE', 'PermitAPPROVEDbySUPERVISOR', 'PermitFINAL-APPROVEDbyDIRECTOR'],
    'request for payment 73536': ['START', 'PermitSUBMITTEDbyEMPLOYEE', 'PermitAPPROVEDbySUPERVISOR'],
    'request for payment 185372': ['START', 'RequestForPaymentSUBMITTEDbyEMPLOYEE', 'RequestForPaymentFINAL-APPROVEDbySUPERVISOR'],
    'request for payment 76195': ['START', 'PermitSUBMITTEDbyEMPLOYEE', 'PermitFINAL-APPROVEDbySUPERVISOR'],
    'request for payment 73737': ['START', 'PermitSUBMITTEDbyEMPLOYEE', 'PermitFINAL-APPROVEDbySUPERVISOR'],
    'request for payment 77107': ['START', 'PermitSUBMITTEDbyEMPLOYEE']
}

mapping = pd.read_csv('mapping.csv')
# devo capire come trasformare prova in dict
for key in prova1.keys():
    print(key)
    graph = mapping.loc[mapping["case:Rfp-id"] == key]["case_number_id_graphs"].tolist()[0]
    graph_path = f'Instance_graphs/{graph}'
    with open(graph_path, 'r') as file:
        testo = file.readlines()
        print(testo)
        print(prova1[key])
        inner_list = []
        for i in testo:
            for j in prova1[key]:
                if j in i:
                    if i not in inner_list:
                        inner_list.append(i)
        print(inner_list)

# how to eliminate relationships with only one node in the list?