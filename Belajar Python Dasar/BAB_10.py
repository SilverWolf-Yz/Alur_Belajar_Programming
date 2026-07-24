#Selamat, kamu sudah sampai ke python dasar BAB 10, BAB terakhir..

#BAB 10 - MODUL DAN LIBRARY (Final Chapter)

#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~ 

#Meminjam Kekuatan Komunitas - (import)
# Sampai saat ini, kita menulis semua logika dari nol. Di dunia nyata, programmer jarang melakukan itu.
# Kita menggunakan kode yang sudah dibuat orang lain agar lebih cepat dam aman.

#[1] Modul Bawaan - (Standard Library)
# Python punya banyak alat yang sudah terpasang didalam dirinya. kita cukup memanggilnya dengan import.
# Contoh:

import math
import random
import time

#Menggunakan modul math - (matematika)
print(math.sqrt(16))    #Hasil 4.0

#Menggunakan modul random 
print(random.randint(1, 10))        #mengeluarkan angka random

#Menggunakan modul time (untuk jeda program) 
print("Loading...")
time.sleep(2) #program berhenti selama 2 detik
print("Selesai")

#[2] PIP & Library Eksternal
# Jila modul bawaan tidak cukup, kita bisa mengunduh library buatan komunitas global menggunakan PIP (Manajer Paket Python)
# Contoh: jika kamu ingin membuat aplikasi cangih seperti AI, Web, atau Otomasi, kamu akan menggunakan PIP untuk menginstalnya ke komputermu.

#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~

#Tantangan Terakhir: Simulator Tebak Angka

# ​Gunakan import random untuk membuat angka rahasia antara 1 sampai 20.

# ​Gunakan import time untuk memberikan jeda 1 detik sebelum memberikan hasil tebakan (agar terasa seperti aplikasi profesional).

# ​Gunakan while True dan try-except (ingat pelajaran Bab 8!) agar program tidak crash jika user salah input.

# ​Buat logika: Jika tebakan benar, ucapkan selamat dan break. Jika salah, beritahu apakah tebakannya terlalu tinggi atau terlalu rendah.

#Mulai:

print("--Simulator Tebak Angka--")                          #judul

while True:                                                 #perulangan
    try:
        tebakan = int(input("Masukan angka 1-20: "))        #meminta input user
        jawaban = random.randint(1, 20)                     #mesin mengacak 1-20
        print("Loading..")                                  #loading selama 1 detik
        time.sleep(1)

        if tebakan == jawaban:                              #jika tebakan benar
            print(f"Kamu benar! jawabannya {jawaban}")
            break

        elif tebakan < 1 or tebakan > 20:                   #jika tebakan kurang dari 1 atau lebih dari 20
            print("Hanya jawab 1 - 20!")
        else:                                               #jika tebakan salah
            print(f"Salah! Jawabannya: {jawaban}")

    except ValueError:                                      #jika user memasukkan huruf atau simbol
        print("Masukan Angka Ya!")

#Keterangan
# angka jawaban akan selalu berubah, peluang benar 1 : 20.
# jika jawaban diletakkan diluar while True, user sudh dipastikan benar karena jawaban tidak di acak ulang. 

# Yah.. udah selesai.. Selamat ya.. sekarang kamu resmi jadi programmer Python Pemula ^_^
