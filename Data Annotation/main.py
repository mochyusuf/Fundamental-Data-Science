# Identifikasi data target dan lakukan pelabelan

# Dalam dataset iris, kolom 'target' sudah mewakili label kelas (0, 1, 2).

# Namun, jika diperlukan pelabelan yang lebih spesifik berdasarkan SOP,

# kita bisa melakukan mapping label sesuai dengan kebutuhan.


# Misalnya, jika SOP menentukan bahwa:

# - target 0: Setosa

# - target 1: Versicolor

# - target 2: Virginica

# Kita bisa membuat mapping label seperti ini:


label_mapping = {

    0: 'Setosa',

    1: 'Versicolor',

    2: 'Virginica'

}


# Buat kolom baru 'target_label' yang berisi label teks

df['target_label'] = df['target'].map(label_mapping)


# Tampilkan data dengan label baru

print("\nData dengan label berdasarkan SOP:")

print(df.head())