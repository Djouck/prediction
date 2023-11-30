import csv
import pandas as pd

# importing datetime class from datetime module
from datetime import datetime


def to_time_stamp(stringa):
    # Step 1: convert string to datetime object
    dt = datetime.strptime(stringa, "%Y-%m-%d %H:%M:%S.%f")
    # Step 2: convert datetime object to timestamp
    timestamp = dt.timestamp()
    return timestamp


def remaining_time(timestamp_1, timestamp_2):
    # calcola la differenza tra i due timestamps (in valore assoluto)
    result = abs(timestamp_1 - timestamp_2)
    return result


def to_date_time(timestamp):
    result = datetime.fromtimestamp(timestamp)
    return result


timestamp = 1545730073
dt_obj = datetime.fromtimestamp(1140825600)

print("date_time:", dt_obj)
print("type of dt:", type(dt_obj))





# importo il file csv in un dataframe di pandas
df = pd.read_csv('finale_SE.csv')
print(df)

# cambio il nome della colonna Complete Timestamp in uno senza spazi in mezzo
df.rename(columns={'Complete Timestamp': 'timestamp'}, inplace=True)

# Seleziono le colonne Case ID e timestamp
df1 = df.loc[:, ['Case ID', 'timestamp']]
print(df1)

# Seleziono le righe corrispondenti a Case 1
df2 = df1.loc[df1['Case ID'] == 'Case 1']
print(df2)

# salvo in una variabile l'ultimo timestamp della colonna timestamp,
# che quindi è riferito all'ultimo timestamp della traccia.
# la cosa migliore sarebbe però prendere il timestamp maggiore
# ma essendo che il dataframe è già stato ordinato per ora va bene così
tot_time = df2['timestamp'].iat[-1]
print(tot_time)

last_timestamp = [tot_time for i in range(0, len(df2['timestamp']))]
print(last_timestamp)

# print(len(last_timestamp))
# print(len(df2['timestamp']))

# df3 = df2.assign(last_time=lambda x: x.timestamp)
# print(df3)

# df2['last_timestamp'] = last_timestamp
# print(df2)

# ex = to_time_stamp(tot_time) -
# print(ex)




