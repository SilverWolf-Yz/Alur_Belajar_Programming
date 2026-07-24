## SELAMAT KAMU TELAH MASUK KE LEVEL 2 DALAM PEMBELAJARAN PYTHON
# LELEL 2 Kontrol Alur (Logic & Flow)

#BAB 4 - Pengkondisian (Percabangan Logika)
#Di bab ini kita akan membuat program kita punya otak untuk memilih jalur berasarkan kondisi tertentu

#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~

# [1] Operator Perbandingan (Alat Cek Kondisi)
# Sebelum membuat percabangan, program harus bisa membandingkan sesuatu. Hasil dari perbandingan ini selalu bernilai boolean (True & False).

#   ==  :   Sama dengan
#   !=  :   Tidak Sama Dengan
#   >   :   Lebih Dari
#   <   :   Kurang Dari
#   >=  :   Lebih dari atau sama dengan
#   <=  :   Kurang dari atau sama dengan

#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~

#Logika 'pintu gerbang' (and, or, not)

#and - (semua harus benar)
#hanya bernilai true jika semua kondisi di kiri dan kanannya benar. contoh:
nilai = int(input("nilai: "))
alfa = int(input("alfa: "))

if nilai >= 60 and alfa < 25:   #jika nilai lebih dari/sama dengan 60 'DAN' alfa kurang dari 25 = lulus
    print("Lulus")
else:
    print("gagal")

#or - (salah satunya benar)
diskon = "VIP"
member = "GOLD" 

if diskon == "VIP" or member == "GOLD":
    print("potongan harga 10%")
else:
    print("harga normal")

#not - (kebalikan dari hasil)

is_locked = True

if not is_locked:
    print("akses terbuka")

else:
    print("akses ditolak")
#hasil True akan menjadi False begitu juga sebaliknya

#       ~ ~ ~ ~ ~ / c / ~ ~ ~ ~ ~

#Struktur if, elif, dan else

#Di sinilah aturan indentasi (spasi di awal baris) yang kamu catat di bab 1 akan mulai terpakai
#Contoh logika dasar interaksi nilai SNBT

nilai_siswa = int(input("masukkan nilai SNBT kamu (0-1000): "))     #meminta user mengisi nilai mereka

if 0 <= nilai_siswa <= 200: #dibaca nilai_siswa lebih dari 0 atau sama dengan nol dan kurang dari atau sama dengan 200
    print("Wah, anda jenius, bahkan profesor tidak akan memahami 'kejeniusan' anda!")   #agak satir :v


elif 200 < nilai_siswa <= 400:  #nilai_siswa lebih dari 200 dan kurang dari 400
    print("Jangan menyerah, belajar akan membuatmu lebih baik")


elif 400 < nilai_siswa <= 600:  #nilai_siswa lebih dari 400 dan kurang dari 600
    print("wow, anda cukup pintar dan memiliki kesempatan untuk masuk ptn")


elif 600 < nilai_siswa <= 800:  #nilai_siswa lebih dari 600 dan kurang dari 800
    print("wih, jenius nih, dengan nilai ini kamu bisa lebih leluasa untuk mendaftar di PTN terkenal")


elif 800 < nilai_siswa <= 1000:  #nilai_siswa lebih dari 800 dan kurang dari 1000
    print("waduh, ketemu calon profesor, anda tidak akan kesulitan mendaftar di PTN manapun")


else:
    print("maaf, nilai anda tidak ada di dartar, siahkan masukkan nilai sesuai aturan")

#Penjelasan:
#1. if wajib dan jumlahnya hanya boleh 1 (untuk 1 logika)
#2. elif opsional dan terserah berapa banyaknya
#3. else opsional tapi jumlah max nya 1(untuk 1 logika)

#struktur diatas aku gabungin dengan materi-materi sebelumnya, sekaligus jadi bahan praktek buatku