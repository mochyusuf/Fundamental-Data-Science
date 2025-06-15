import pandas as pd
from sklearn.datasets import load_iris


# Muat dataset iris

iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

df['target'] = iris.target


# Identifikasi jumlah data

print("Jumlah data:", df.shape[0])


# Identifikasi tipe data

print("\nTipe data:")

print(df.dtypes)


# Identifikasi nilai yang hilang

print("\nJumlah nilai yang hilang:")

print(df.isnull().sum())


# Identifikasi outlier (menggunakan IQR)

for column in df.columns[:-1]:  # Loop melalui fitur numerik

  Q1 = df[column].quantile(0.25)

  Q3 = df[column].quantile(0.75)

  IQR = Q3 - Q1

  lower_bound = Q1 - 1.5 * IQR

  upper_bound = Q3 + 1.5 * IQR

  outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

  print(f"\nOutlier pada kolom {column}:")

  print(outliers)


# Deskripsi statistik data

print("\nDeskripsi statistik:")

print(df.describe())



# Pembersihan data

# 1. Pengisian nilai yang hilang (jika ada)

# Dalam dataset iris, tidak ada nilai yang hilang, jadi bagian ini bisa dilewati.

# Namun, jika ada, Anda bisa menggunakan:

# df['sepal length (cm)'].fillna(df['sepal length (cm)'].mean(), inplace=True) 

# df['sepal width (cm)'].fillna(df['sepal width (cm)'].median(), inplace=True)

# df['petal length (cm)'].fillna(df['petal length (cm)'].mode()[0], inplace=True)


# 2. Menghapus baris dengan data yang salah (jika ada)

# Dalam dataset iris, tidak ada data yang salah secara jelas.

# Namun, jika ada, Anda bisa menggunakan:

# df.drop(df[df['sepal length (cm)'] < 0].index, inplace=True)


# 3. Mengoreksi nilai outlier

for column in df.columns[:-1]:

  Q1 = df[column].quantile(0.25)

  Q3 = df[column].quantile(0.75)

  IQR = Q3 - Q1

  lower_bound = Q1 - 1.5 * IQR

  upper_bound = Q3 + 1.5 * IQR

  df[column] = df[column].clip(lower_bound, upper_bound)


# Setelah pembersihan data

print("\nDeskripsi statistik setelah pembersihan:")

print(df.describe())