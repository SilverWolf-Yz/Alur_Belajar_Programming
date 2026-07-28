#BAB 11 - (Class & Object dasar)
# Sekarang dan seterusnya kita akan mendalami python melebihi materi dasar kemarin, kita akan masuk ke materi OOP (Object-Oriented Programming).


#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~


#Penjelasan

#Apa itu OOP (Object-Oriented Programming)?
# OOP dalam Python adalah paradigma pemrograman yang menyusun kode berdasarkan objek. konsep ini menghubungkan konsep Data (Atribut) dan Fingsi (Method)
# Ke dalam satu wadah terorganisir. Pendekatan ini membantu 'memodelkan skenario dunia nyata ke dalam kode pemrograman'.

#Komponen Utama OOP
# Untuk memahami OOP, Kamu harus memahami 2 komponen paling dasar :
# Class : Cetak Biru (Blueprint) atau template atau 'denah' yang mendefinisikan struktur dan perilaku objek.
# Object : Bentuk nyata (instance) atau 'Rumah' hasil cetakan dari sebuah class.

#Sebagai analogi, 'Class' adalah cetakan kue, sedangkan 'Object' adalah kue-kue nyata yang dihasilkan dari cetakan tersebut.
#Di dalam Python, kita menggunakan 'class' untuk mendefinisikan denah ini. kemudian, __init__ adalah fungsi "pemberi nyawa" yang dijalankan saat rumah (objek) dibangun.


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~


#Contoh

# Pertama Buat class/denah nya
class kucing:
    def __init__(self, nama, warna):    # Self untuh mewakili Object, pernyataan 1 yaitu nama, pernyataan 2 yaitu warna
        self.nama = nama                # Atribut (data milik object)
        self.warna = warna              # Atribut

# Sekarang kita buat object/rumah-rumah nya
kucing1 = kucing("Luna", "Putih")       # mengikuti pernyataan
kucing2 = kucing("Milo", "Oranye")

# Terakhir, Panggil dengan print
print(f"Kucing Chika namanya {kucing1.nama}, warnanya {kucing1.warna}.")
print(f"Kucing Ibnu namanya {kucing2.nama}, Warnanya {kucing2.warna}.")


#           ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~

#Praktik
# Membuat class mahasiswa dengan atribut nama dan nim. lalu buat 3 objek mahasiswa yang berbeda menggunakan class tersebut, dan cetak datanya ke layar.

class mahasiswa:
    def __init__(self,nama, nim):
        self.nama = nama
        self.nim = nim

m1 = mahasiswa("Bintang", 902900)
m2 = mahasiswa("Revan", 902901)
m3 = mahasiswa("Taqqiyyuddin", 902902)

print("===== Daftar Mahasiswa Berpotensi =====")
print("Siswa         NIM\n")
print(f"{m1.nama} , {m1.nim}")
print(f"{m2.nama} , {m2.nim}")
print(f"{m3.nama} , {m3.nim}")

#Bedanya apa dengan list dan dictionary?
# Bedanya, class digunakan untuk kebutuhan data yang besar, banyak, dan kompleks. class juga bisa ditambahkan aksi 
# (merujuk pada apa yang bisa dilakukan oleh objek tersebut) yang akan kita bahas di bab 12. selain itu dengan class code jadi lebih aman, kenapa? karena kamu bisa memasang "satpam" 
# (menggunakan setter dan enkapsulasi, yakni cara kita mengunci data agar tidak bisa diubah sembarangan dari luar).

#Note : Aku ubah dikit struktur pembelajaran ku:
# A = Penjelasan
# B = Contoh
# C = Praktik mandiri