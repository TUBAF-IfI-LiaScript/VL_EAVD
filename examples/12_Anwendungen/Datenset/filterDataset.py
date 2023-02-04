import pandas as pd

df=pd.read_csv("distanceMeasurements.csv", sep=',', header = 0)
# Löschen der irrelevanten Spalten aus dem Datensatz
df.drop(['entry_id', 'latitude', 'longitude', 'elevation', 'status'], axis=1, inplace=True)
# Entfernen aller Messungen mit geradem Index 
df_filtered = df[df.reset_index().index % 2 != 0]  .copy()
df_filtered.head(5)


df_filtered.reset_index(drop=True, inplace = True)
# Umbenennen der Spaltennamen
df_filtered.rename(columns = {'field1':'Temperature', 
                              'field2':'Humidity',
                              'field3':'US_duration'}, inplace = True)
df_filtered.head(5)

# Speichern als neue csv Datei
df_filtered.to_csv("distanceMeasurements_filtered.csv", index= False)