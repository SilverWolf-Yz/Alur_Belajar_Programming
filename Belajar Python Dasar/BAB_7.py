#BAB 7 - BLOK KODE MANDIRI (Fungsi/Function)
#Bayangkan kamu punya "resep" untuk melakukan tugas tertentu, misalnya menghitung total damage karakter seperti yang kamu lakukan di BAB 3.
#Daripada menulis ulang kode perhitungan tersebut setiap kali ada karakter baru, kamu bisa membungkusnya kedalam sebuah  fungsi  

#       ~ ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~

#Sintaks Dasar Fungsi
#kita menggunakan kata kunci def (singkatan define / mendefinisikan) untuk membuat fungsi.
#contoh:

#[1] mendefinisikan fungsi
def sapa_pemain(nama):
    print(f"Halo {nama}, selamat datang di dunia Python")

#[2] Memanggil fungsi
sapa_pemain("Naufal")
sapa_pemain("Arfio")

#keterangan:
#sapa_pemain adalah label yang bisa diubah begitu juga dengan isi (nama)
#print(f"") untuk memanggil isi, yakni {nama}
#kenapa label/isi nya dibawah, tidak diatas seperti kita sedang membuat tempat penyimpanan variabel?
#karena itu untuk menjelaskan kepada mesin seberapa banyak kita ingin memanggil variabel def sapa_pemain(nama), disitu kita tinggal tulis nama_pemain("...")

#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~

#Parameter : input dinamis (bisa diubah) yang masuk ke dalam fungsi agar fungsi bisa bekerja dengan data yang berbeda-beda.
#Return    : Digunakan untuk mengirimkan hasil pemrosesan keluar dari fungsi agar hasilnya bisa disimpan dalam variabel / digunakan oleh kode lain.

#contoh (1 parameter):

def hitung_luas_persegi(sisi):
    hasil = sisi * sisi
    return hasil                             #mengirim hasil keluar

#pemanggilan fungsi & penggunaan variabel 
luas_meja = hitung_luas_persegi(5)           #(5) adalah sisi seperti yang kita nyatakan di hitung_luas_persegi(sisi)
print(f"luas persegi adalah: {luas_meja}")

#Keterangan:
# def disini untuk melakukan operasi hitung,
# sementara bagian pemangilan untuk memasukkan angka sekaligus hasilnya masuk ke luas_meja dan di print agar muncul di layar.



#Contoh (2 parameter):
# 1. Membuat rumus dengan dua parameter
def hitung_luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil  # Mengembalikan hasil perkalian ke luar fungsi

# 2. Memasukkan angka sekaligus menyimpan hasilnya ke dalam variabel
luas_karpet = hitung_luas_persegi_panjang(10, 5)

# 3. Mencetak hasil ke layar
print(f"Luas persegi panjang adalah: {luas_karpet}")

#Keterangan
# sama seperti keteranganku sebelumnya
# kali ini dengan menambahkan , agar menjadi 2 parameter (jangan lupa di masukan angka juga harus 2)

#kalau kita ingin jadikan input agar bisa diubah pengguna kita tambah prosesnya di sela-sela 1 dan 2 dan ubah (10 , 5) menjadi laci yang kita buat
#contohnya dengan menambahkan ]

#input_panjang = float(input("Panjang: "))
#input_lebar = float(input("Lebar: "))

#(10 ,5) diubah menjadi (input_panjang, input_lebar)

#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~

#Praktik:

def hitung_pangkat(angka, pangkat):
    proses_pangkat = angka ** pangkat
    return proses_pangkat

perpangkatan = hitung_pangkat(5, 2)
print(f"Hasil pangkat: {perpangkatan}")

