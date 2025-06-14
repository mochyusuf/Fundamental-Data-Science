import pandas as pd

# Ganti 'Data_Nasabah.csv' dengan path yang benar ke file CSV Anda
data = pd.read_csv('Data_Nasabah.csv', delimiter=";")

# Jumlah data (baris dan kolom)
print("Jumlah data (baris, kolom):", data.shape)

# Informasi tentang tipe data dan skema pengkodean
print("\nInformasi tipe data dan skema pengkodean:")
print(data.info())

# Statistik deskriptif untuk data numerik
print("\nStatistik deskriptif untuk data numerik:")
print(data.describe())

# Melihat beberapa baris pertama data
print("\nBeberapa baris pertama data:")
print(data.head())

# Melakukan pengkodean pada kolom kategorikal
data['jenis_kelamin'] = data['jenis_kelamin'].map({'Laki-Laki': 1, 'Perempuan': 2})
data['jenis_produk'] = data['jenis_produk'].map({'tabungan': 1, 'kartu_kredit': 2, 'deposito': 3})
data['pengguna_mobile_banking'] = data['pengguna_mobile_banking'].map({'YA': 1, 'TIDAK': 2})
print(data.head()) # Memastikan perubahan

# Menampilkan jumlah nilai unik untuk setiap kolom (untuk memahami kategori)
print("\nJumlah nilai unik untuk setiap kolom:")
for column in data.columns:
  print(f"{column}: {data[column].nunique()}")