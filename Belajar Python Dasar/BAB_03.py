#BAB 3 - Interaksi & Matematika Dasar

#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~

# [1] Mengambil input dari pengguna
#Jika print() digunakkan untuk mengeluarkan data dari program ke layar, maka input() adalah kebalikannya. input() mengambil data dari pengguna di keyboard untuk dimasukkan kedalam program.
#setiap data yang ditangkap oleh fungsi input() secara otomatis akan dianggap sebagai tipe data string (Teks). meskipun pengguna mengetikkan angka.
#contoh penggunaan input:

print("Halo, aku lihat kamu sedang belajar python? siapa namamu?")
nama_user = input("Masukkan nama kamu:")
print(f"wah, semangat ya {nama_user}, lanjut gih belajarnya~ tapi jangan lupa istirahat.")

#keterangan:
#disitu aku menggunakan print untuk sapaan awal sebelum meminta user untuk memasukkan nama
#aku memasukkan input nama tersebut ke label nama_user dan aku panggil di print selanjutnya
# mudah dijelaskan, tapi terkadang kita merasa sulit jika kita lihat T-T

#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~

# [2] Konversi tipe data
# Karena fungsi input() selalu menghasilkan strung (teks) kita bisa mengubahnya menjadi tipe data lain dengan:

#int(input( ))          =>      mengubah yang awalnya string menjati integer (angka)

#float(input( ))        =>      mengubah yang awalnya string menjadi float (angka desimal)

#boolean, disini agak rumit,kita tidak bisa mengonversikannya secara langsung dengan cara diatas. tapi dengan cara/logika:

#meminta input penguna / user
user_next = input("Apakah anda ingin melanjutkan? (ya/tidak): ")

#mengubah bool berdasarkan kondisi
is_continue = user_next == "ya"

print(is_continue) #menghasilkan True jika jawab yes dan False jika jawab no

#       ~ ~ ~ ~ ~ / c/ ~ ~ ~ ~ ~        

# [3] Operator aritmatika Python
#berikut simbol-simbol matematika yang digunakan di python

#Operator           Simbol          Contoh          Hasil           Keteramgan
#Penjumlahan        +               5+2             7               seperti biasa
#Pengurangan        -               5-3             2               seperti biasa
#perkalian          *               5*3             15              menggunakan simbol bntang (*)
#Pembagian          /               5/2             2.5             menggunakan simbol garis miring (/)
#Pembagian bulat    //              5//2            2               dua (//) membulatkan hasil, koma (.) tidak dianggap
#Modulus            %               5%2             1               sisa dari hasil pembagian (5/2 = 2, dengan sisa 1)
#Perpangkatan       **              5**2            25              5 pangkat 2 (pangkat dengan simbol bintang 2 (**))

#       ~ ~ ~ ~ ~ / ? / ~ ~ ~ ~ ~
# Tes kecil-kecilan ^-^

print("=== PROGRAM REKAP DAMAGE KARAKTER ===")

# 1. Mengambil input dari pengguna (dengan konversi ke tipe angka dan desimal
nama_skill = input("Masukkan nama skill: ")
damage_dasar = int(input("Masukkan Damage Dasar (Angka Bulat): "))
critical = float(input("Masukkan Pengali Critical (Contoh: 1.5): "))

# 2. Melakukan perhitungan matematika 
total_damage = damage_dasar * critical

# 3. Menampilkan hasil perhitungan menggunakan f-string
print("--- HASIL REKAP ---")
print(f"Skill {nama_skill} menghasilkan total damage: {total_damage}")

# 4. Eksperimen Tambahan
# Coba hitung sisa bagi (Modulus)
sisa_bagi = 20 % 3
print(f"Sisa bagi dari 10 dibagi 3 adalah: {sisa_bagi}")