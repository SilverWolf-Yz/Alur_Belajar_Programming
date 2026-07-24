#BAB 2 - Tempat Penyimpanan (Variabel & Tipe Data)

#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~

#Apa itu variabel?
#Bayangkan variabel itu seperti *sebuah kotak penyimpanan atau laci berlabel* di dalam memori komputer.
#kamu bisa memasukkan barang (Nilai / data) ke dalam laci (Variabel) tersebut, lalu kapanpun kamu butuh barang (Nilai / Data) itu, kamu tinggal memanggil nama labelnya (nama variabelnya).
#contoh nya:

nama = "Artoria Pendragon" 
gender = "perempuan"
umur = 15
tinggi_badan = 154.5

#cara menjalankannya:
print("Data Pribadi")
print(nama)
print(umur)
print(tinggi_badan)

#keterangan:
#laci/lbel (variabel) = nama, umur, tinggi_badan
#barang (nilai/data)  = "Artoria Pendragon", 15, 154.5

#nama variabel tidak boleh diawali dengan angka, tetapi diperbolehkan dibelakang huruf, contohnya
#benar: bab1 = "Aturan Main"
#salah: 1bab = "Aturan main"

#kenapa pakai garis bawah/underscore? (_), karena spasi dipakai python untuk memisahkan perintah / kata kunci. misalnya:

#nama pengguna = "Saber"

#itu akan menyebabkan error karena python menganggap 'nama' dan 'pengguna' adalah dua hal yang berbeda

#kenapa ada nilai yang pakai "", ada yang tidak, dan kenapa pakai (.) bukan (,)? 
#kita akan bahas di bagian selanjutnya

#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~

#Mengenal 4 Tipe Data Dasar
#isi dari kotak variabel tersebut terdapat berbagai macam bentuknya, Di python ada 4 tipe data dasar yang paling sering digunakan. diantaranya:

#Tipe Data          Nama di python      Contoh          Penjelasan
#Teks/Huruf         String (str)        "Lancer"        harus dibungkus kutip dua ("") / tunggal ('')
#Angka Bulat        Integer (int)       24              angka tanpa (""), (''), desimal, dan koma 
#Angka Desimal      Float (float)       171.5           angka yang memiliki koma (ditulis pakai titik (.))
#Logika             Boolean (bool)      wanita = True   hanya bernilai benar/salah (huruf awal wajib kapital/besar)
#                                       pria = False   

#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~

#Praktik simple

#(1) deklarasi variabel dengan berbagai tipe data
nama_karakter = "Saber"     #str
level = 45                  #int
attack = 102.7              #float
apakah_hidup = True         #bool

#(2) menampilkan isi variabel ke layar
print("--- STATUS KARAKTER ---")
print("Nama:", nama_karakter)
print("level:", level)
print("Attack:", attack)
print("Status:", apakah_hidup)

#(2) dengan cara yang keren ^-^
print("--- STATUS KARAKTER ---")
print(f"Nama Karakter: {nama_karakter}")
print(f"level: {level}")
print(f"attack: {attack}")
print(f"Status: {apakah_hidup}")

#kenapa pakai f?
#itu disebut f-string dimana adalah fitur untuk merubah tipe data menjadi string secara sementara
#lebih tepatnya saat kita memanggil data tersebut menggunakan print