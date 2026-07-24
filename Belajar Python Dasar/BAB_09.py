#BAB 9 - BEKERJA DENGAN FILE (FILE I/O)

#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~

#Membaca & Menulis File
# Python bisa membuka file teks biasa (.txt) untuk mengambil data (membaca) atau menyimpan data (menulis) ke dalamnya.

#[1] Menulis ke File ('w')
# Gunakan mode 'w' (write). 
# hati-hati, mode ini akan menghapus isi file lama dan menggantikannya dengan file yang baru.

#Membuka file dengan with (cara paling aman)
with open("catatan.txt", "w") as file:                              #buka catatan.txt mode w sebagai file
    file.write("Halo, ini data yang tersimpan secara permanen.\n")    #tulis file


#[2] Membaca File ('r')
# Gunakan mode 'r' (read) hanya untuk membaca (tidak bisa diubah)

with open("catatan.txt", "r") as file:                              #buka catatan.txt mode r sebagai file
    isi = file.read()                                               #masukkan sebagai variabel, () menunjukan isinya
    print(isi)                                                      #menampilkan isi 

#Keterangan:
# with aman karena ia bisa menghindari kebocoan data, kebal terhadap error (jika error akan otomatis keluar, tidak menggantung.
# campuran _enter_ otomatis menyimpan/membuka file dan _exit_ otomatis membersihkan memori dan menutup file (baik program sukses/error)
# \n adalah cara untuk menambahkan newline atau baris baru

#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~ 

#Tantangan BAB 9 : Jurnal Digital

# [1] buat program yang meminta input nama pengguna
# [2] simpan nama tersebut ke dalam file bernama daftar_user.txt (gunakan mode 'a' alias append supaya tidah terhapus, tapi menambah kebawah)
# [3] setelah tersimpan, buat program mu membaca kembali file daftar_user.txt tersebut dan menampilkannya ke layar

print("--- Halo Selamat Datang Pengguna ---")
nama_user = input("Mohon masukan nama anda: ")

with open("daftar_user.txt", "a") as file:
    file.write("Nama Pengguna:\n")
    file.write(f"{nama_user}\n")

with open("daftar_user.txt", "r") as file:
    isi1 = file.read()
    print(isi1)

#nah ini, ini lebih gampang masuk otak :)