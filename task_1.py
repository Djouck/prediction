import pandas as pd
from datetime import datetime
import pm4py
import graphviz


class Event:
    def __init__(self, case, activity, timestamp):
        self.case = case
        self.activity = activity
        self.timestamp = timestamp


# Aprire l'event log Il nome del file in una variabile da richiamare in seguito:

fname = "finale_SE.csv"

# apre il file e lo memorizza in un dataframe pandas
df = pd.read_csv(fname, delimiter=",", header = 0)

# print(df.keys())
# Case ID,Activity,Resource,Complete Timestamp,Variant,Variant index,variant,variant-index,
# creator,lifecycle:transition,workgroup,Resource,Activity

# Stampa le singole occorrenze di ogni label
# for k in df.keys():
#    print(k, ":", df[k].unique())

# Stampa le singole occorrenze di ogni label
# for k in df.keys():
#    print(k, ":", len(df[k].unique()))

## 1 ## COMPUTE THE REMAINING TIME

# create a dictionary:
# keys  -> Case ID
# value -> last event's timestamp of the corresponding Case ID

# create dictionary
dCaTi = {}

# compute a list of all the Case ID
listaCaseID = df["Case ID"].unique()

# insert last element as a string value
for c in listaCaseID:
    dCaTi[c] = str(max(df.loc[ df["Case ID"] == c] ["Complete Timestamp"]))#.split(".")[0]


# create a new dataframe (this is not necessary but we can remove this step later) to add the column with the remaining time

#add a column with remaining time
df['remainingTime'] = [(datetime.strptime(dCaTi[r[1]["Case ID"]], '%Y-%m-%d %H:%M:%S.%f') - datetime.strptime(r[1]["Complete Timestamp"], '%Y-%m-%d %H:%M:%S.%f')).total_seconds()  for r in df.iterrows() ]

print(df[0:20])

# visualize DFG

#event_log = pm4py.format_dataframe(df, case_id='Case ID', activity_key='Activity', timestamp_key='Complete Timestamp')

#dfg, start_activities, end_activities = pm4py.discover_dfg(event_log)
#fig = pm4py.view_dfg(dfg, start_activities, end_activities)


