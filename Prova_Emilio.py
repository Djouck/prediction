#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:50:08 2023
@author: emilio
"""

import pandas as pd
import copy


class CreateEventObject:
    def __init__(self, c):  # , case, activity, timestamp):
        cID = c.iloc[0]  # .CaseID
        cAct = c.iloc[1]  # .Activity
        cTime = c.iloc[3]  # .CompleteTimestamp


fname = "finale_SE_short.csv"
df = pd.read_csv(fname, delimiter=",", header=0)

# Rename df columns without blanks:
## Case ID >> CaseID
## Complete Timestamp >> CompleteTimestamp
df = df.rename(columns={"Case ID": "CaseID", "Complete Timestamp": "CompleteTimestamp"})

# Order the dataset by timestmap
df = df.sort_values(by=['CompleteTimestamp'])
print(df)

df['EventObj'] = df.apply(lambda x: CreateEventObject(x), axis=1)

# crea il dizionario evento_stato
# key = evento
# value = stato >>> list of past events

stato = []


def aggiungi_al_diz(e):
    if len(evento_stato) == 0:
        evento_stato[e] = [e]
        stato = evento_stato[e]
    else:
        evento_stato[e] = evento_stato[e].append(e)
        stato = evento_stato[e]
    return ()


evento_stato = {}
indice = 0
previous = ""
for e in df['EventObj']:
    if len(evento_stato) == 0:
        evento_stato[e] = [e]
        previous = e
    else:
        s = copy.deepcopy(evento_stato[previous])
        s.append(e)
        evento_stato[e] = s
        previous = e
    indice += 1

# els = list(evento_stato.items())
# print(els[-1])


df['Status'] = df['EventObj'].apply(lambda x: evento_stato[x])

# stampa l'ultimo
#print(df.loc[df["CaseID"] == "Case 595"])

print(df['Status'][1]==df['Status'][4])

pippo = df['Status'][61]
pluto = df['Status'][17]

print(pippo)
print(pluto)

print(len(pippo))
