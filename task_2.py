# Per ogni evento, rispetto al timestamp, calcolare:
## 1 ## il remaining time
## 2 ## tutti quelli che sono esistiti fino al tempo del timestamp
## 3 ## tutti quelli “running” nel momento del timestamp

import pandas as pd
import copy

fname = "finale_SE.csv"
df = pd.read_csv(fname, delimiter=",", header = 0)

# rename df columns without blanks:
# Case ID >> CaseID
# Complete Timestamp >> CompleteTimestamp
df = df.rename(columns={"Case ID": "CaseID", "Complete Timestamp": "CompleteTimestamp"})

#Order the dataset by timestmap
df = df.sort_values(by=['CompleteTimestamp'])

df.loc[df["CaseID"] == "Case 595"]

# TODO1
# classe EVENT per creare un evento con case, nome dell'attività e timestamp
class Event:
    def __init__(self, case, activity, timestamp):
        self.case = case
        self.activity = activity
        self.timestamp = timestamp


# classe status per creare oggetto status con elemento da appendere in una lista che sarà poi la pandas serie per status ALL

#class Status:
    #def __init__(self, status):
        #self.status = status

# Ogni colonna finale "Status_ALL" conterrà tale dizionario aumentato ad ogni iterazione

# (TODO2)
# add new column "Status_ALL"
df["Status_ALL"] = None

dCaLE = {}  # dictionary of Cases and List of Events occurred
i = 0
inner_list = []  # dizionario che si trasforma in pandas serie

for r in df.iterrows():
    print(i)
    # <class 'tuple'> 24071 Case ID  Case 3608, Activity  START, Complete Timestamp  2010-01-13 08:40:24.999, ...
    cID = r[1].CaseID
    act = r[1].Activity
    date = r[1].CompleteTimestamp

    ev = Event(cID, act, date)

    if cID in dCaLE:
        l = copy.deepcopy(dCaLE[cID])  # .append(ev)
        newL = []
        for item in l:
            newL.append(item)
        newL.append(ev)

        dCaLE[cID] = copy.deepcopy(newL)
    else:
        dCaLE[cID] = copy.deepcopy([ev])
    if ev.activity == 'END':
        del dCaLE[ev.case]

    state = copy.deepcopy(dCaLE)

    inner_list.append(state)



    # QUI DA RIVEDERE
    # print(dCaLE)
    # df["Status_ALL"] = dCaLE
    #
    # if i == 10:
    #    print(df.loc[df["CaseID"] == "Case 3608"])
    #    #print(df["Case 3608"]["Status_ALL"])
    #    rrr

    i += 1

print(type(inner_list[7]))

#print(inner_list[24071])
df["Status_ALL"] = inner_list
print(inner_list[0] == inner_list[4])
print(df[0:20])

