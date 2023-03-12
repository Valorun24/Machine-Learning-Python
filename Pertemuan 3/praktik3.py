from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from pandas import DataFrame
import pandas as pd
import numpy as np

#baca file dataset
df = pd.read_csv("Apartemen_numerik.csv")
print(df)

#Menampilkan statistik deskriptif
print(df.describe())

#Mengganti lokasi spesifik
df.loc[2, "Jum_kamar"] = 100
print(df)
print(df.shape)
print(df.Jum_kamar)

fitur_minmax =df.copy()
kol_minmax = ["Jum_kamar"]
features = fitur_minmax[kol_minmax]
min_max=MinMaxScaler()
kamar_minmax=min_max.fit_transform(features.values)

print(kamar_minmax)

fitur_minmax[kol_minmax] = kamar_minmax
print(fitur_minmax)

df = fitur_minmax

df.to_csv("Apartemen_minmax.csv", header=True, index=False)