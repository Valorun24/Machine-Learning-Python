#libraries
import pandas as pd
import numpy as np

#baca file data set
df = pd.read_csv("apartemen2.csv")

#melihat semua isi data
print(df)

#cek missing value
print(df.isnull().values.any())

#banyaknya missing values
print(df.isnull().sum().sum())

#melihat kolom kodeAPT
print(df['KodeApt'])
print(df['KodeApt'].isnull())

#melihat kolom Jum_kamar
print(df["Jum_kamar"].isnull())

#membuat daftar missing value
missing_values = ["n/a", "na", "--"]
df = pd.read_csv("apartemen2.csv", na_values = missing_values)

print(df["Jum_kamar"])
print(df["Jum_kamar"].isnull())
#pada hasil running nomor 7 dan 8 "NaN" artinya adalah bukan angka

#cek data kolom St_Milik
print(df["St_Milik"])
print(df["St_Milik"].isnull())

#Deteksi Angka
cnt=0
for row in df["St_Milik"]:
    try:
        df["St_Milik"].isnull()
        int(row)
        df.loc[cnt, "St_Milik"]=np.nan
    except ValueError:
        pass
    cnt+=1

print(df["St_Milik"].isnull())

#Total missing values setiap kolom
print(df.isnull().sum())
#banyaknya missing values
print(df.isnull().sum().sum())

#mengganti missing values dengan sebuah angka
df['KodeApt'].fillna(837, inplace=True)
print(df.KodeApt)

#mengganti pada lokasi spesifik
df.loc[2,"KodeApt"] = 8837
print(df.KodeApt)

#mengganti missing value dengan median
median = df["Jum_kamar"].median()
df['Jum_kamar'].fillna(median, inplace=True)
print(df.Jum_kamar)

#melihat data keseluruhan
print(df)

#mengganti pada lokasi spesifik pada kolom st_milik
df.loc[3, "St_Milik"] = "N"
df.loc[6, "St_Milik"] = "Y"
print(df.St_Milik)
print(df)

#simpan data
#df.to_csv("Apartemen_ok.csv")




