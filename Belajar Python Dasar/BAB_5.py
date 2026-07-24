#BAB 5 - Perulangan (Looping)
#Jika kamu ingin mencetak angka 1 sampai 100, apakah kamu akan menulis print 100 kali?
#Tentu tidak! Disinilah looping bekerja.

#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~

#While Loop - (Mengulang selama kondisi benar)

#While akan terus mengulang blok kodenya selama kondisi yang diberikan bernilai True. 
#Perulangan ini sangat bergantung pada kondisi logika. Contoh:


hitung_mundur = 5                                   #jumlah hitungan masukkan ke label

while hitung_mundur > 0:                            #selama hitung mundur lebh dari 0 ia akan menghasilkan True
    print(f"Peluncuran Dalam: {hitung_mundur}")     #mencetak "Peluncuran Dalam: {angka}" di layar
    hitung_mundur = hitung_mundur - 1               #mengurangi angka pada label hitung_mundur sebanyak 1

print("Memulai Peluncuran")                         #mencetak "Memulai Peluncuran" setelah proses while selesai


#jika - diubah menjadi + ia akan menjalankan angka 1 sampai jutaan atau tak terhingga sampai laptop/pc mampus :v
#jangan dilakukan!

#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~

#for loop - (Mengulang berdasarkan rentang / koleksi)

#for loop paling sering digunakan untuk mengulang kode dengan jumlah yang sudah diketahui sebelumnya.
#atau untuk menelusuri isi suatu data (seperti daftar/list).

for i in range(5):
    print(f"perulangan ke-{i}")

#keterangan:
#1. i bisa diganti karena ia adalah variabel / nama (mirip label)
#2. in - kata kunci penghubung, untuk memberitahu perulangan for  darimana sumber data atau rentang angka yang harus diambil
#3. range(5) - membuat perulangan 5 kali, dimulai dari angka 0 hasilnya 0, 1, 2, 3, 4 (tidak ada 5 karena jumlah angkanya 5)

#(start, stop, step)

for n in range(1, 10, 2):
    print(f"angka: {n}")

#start di 1 artinya angka bermulai dari angka 1
#stop di 10 artinya berhenti saat mencapai 10
#step di 2 artinya melompati 1 angka dan mencetak angka berikutnya / angka ke 2     mirip materi baris/deret mat kelas 10 sma

#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~

#kontrol perulangan - (break & continue)
#untuk memaksa prulangan untuk:

#break : menghentikan perulangan secara paksa dan keluar dari blok perulangan
#continue : melompati sisa kode di dalam satu perulangan ini. lanjut ke putaran berikutnya.
#contoh:

for y in range(12):
    if y == 6 or y == 7:
        continue

    print(f"angka ke-{y}")


print("setengah peleton berisi:")
for z in range(1, 14):
    if z == 8:
        break

    print(f"Peleton: {z}")


#       ~ ~ ~ ~ ~ / praktik singkat / ~ ~ ~ ~ ~


print("--- Latihan Perulangan ---")

# 1. Menggunakan while loop
i = 1
while i <= 3:
    print(f"Looping while ke-{i}")
    i += 1  # Singkatan dari i = i + 1


# 2. Menggunakan for loop
for angka in range(1, 4):
    print(f"Looping for ke-{angka}")


# 3. Tantangan: Menggunakan break
print("--- Percobaan Break ---")
for x in range(1, 10):
    if x == 5:
        print("Ketemu angka 5, berhenti!")
        continue
    print(f"Angka: {x}")

#antara while dan for, hasilnya tidak ada bedanya kecuali penulisanya
#no 3 jika menggunakan break ia akan berhenti di no 5, juka continue ia akan melakukan print "ketemu angka 5, berhenti!"

