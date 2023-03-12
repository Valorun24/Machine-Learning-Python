from pandas import DataFrame
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

#baca file dataset
df = pd.read_csv("Apartemen_ok.csv")
print(df)
df.info()

#Membuat list yang akan ditambahkan menjadi kolom tambahan
label_kelas = ["Murah", "Murah", "Mahal", "Murah", "Mahal", "Mahal", "Mahal", "Murah", "Murah"]
df["Label"] = label_kelas
print(df)

#Menampilkan statistik deskriptif
print(df.describe())

#Mengeksplore lebih dalam untuk atribut wilayah
df.Wilayah.unique()
valueCount = df.Wilayah.value_counts()
print(valueCount)

#visualisasi dalam diagram batang kolom wilayah
sns.set(style = "darkgrid")
ax = sns.countplot(x="Wilayah", data=df)

plt.figure(figsize=(5,5))

#total = float(Len(df["Label"]))
ax = sns.countplot(x="Wilayah", data=df)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x()+p.get_width()/2., 
    height,
    '{:1.0f}'.format((height)),
    ha="center")

plt.show()

#menampilkan histogram untuk semua atribut numerik
numerik_df = df.select_dtypes(include=['float64'])
numerik_index = numerik_df.columns
numerik_index
df.hist(column=numerik_index, figsize=(10,20), layout=(5,1))
plt.show()

#menampilkan histogram untuk atribut numerik
numerik_df = ["Jum_kamar"]
numerik_index = numerik_df
numerik_index
df.hist(column=numerik_index, figsize=(10,20), layout=(5,1))
plt.show()

#menampilkan histogram untuk atribut numerik
numerik_df = ["KodeApt"]
numerik_index = numerik_df
numerik_index
df.hist(column=numerik_index, figsize=(10,20), layout=(5,1))
plt.show()

#boxplot with matplotlib, melihat outliner yang dapat terjadi misalnya karena kesalahan ketik
plt.boxplot(df.KodeApt)
plt.plot()
plt.show()