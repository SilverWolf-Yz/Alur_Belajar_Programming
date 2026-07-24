#Level 3 - (Struktur Data)
#Selamat, sudah level 3 nya~

#BAB 6 - wadah data (koleksi)

#       ~ ~ ~ ~ ~ / Koleksi / ~ ~ ~ ~ ~

#Di bab ini, kita akan membedah 3 jenis koleksi utama di python:

#[1] list       ([...]) : Seperti daftar belanja. urut, bisa diubah, dan datanya bermacam-macam.
#[2] Tuple      ((...)) : Seperti list, tapi permanen. sekali dibuat tidak bisa diubah (data nya terkunci)
#[3] Dictionary ({...}) : Seperti kamus atau buku telepon. data disimpan dengan sistem "key (label) : value (isi)". ini adalah struktur paling powerfull untuk apk nyata.

#       ~ ~ ~ ~ ~ / Contoh List / ~ ~ ~ ~ ~

# Membuat list
daftar_skill = ["Magic Arrow", "Heal", "Shield"]

# Mengakses data (indeks dimulai dari 0)
print(daftar_skill[0])          #memunculkan Magic Arrow
print(daftar_skill[2])          #memunculkan Shield

#Mengubah data di dalam list
daftar_skill[1] = "Mega Heal"   #mengubah Heal menjadi Mega Heal

#Note: Python menghitung Posisi data (indeks) dari 0, bukan 1.

#       ~ ~ ~ ~ ~ / Praktik / ~ ~ ~ ~ ~

print(" ~ ~ ~ ~ ~ list 5 teman ~ ~ ~ ~ ~ ") 
teman_sma = ["Arfio", "Candra", "Fahri", "Bintang", "Revan"]

#Akses data 
print(teman_sma[0])
print(teman_sma[-4])

#ubah
teman_sma[4] = "Aziz"
print(teman_sma[4])

#tips mengetahui panjang list
print(teman_sma)
jumlah_teman = len(teman_sma)
print(f"Jumlah teman saya ada: {jumlah_teman}")

#menambah data diakhir list
teman_sma.append("Udin")
print(teman_sma)

jumlah_baru = len(teman_sma)
print(f"Sekarang jumlah teman saya : {jumlah_baru}")


# Membuat tuple
#contoh angka favorit
angka_favorit = (7, 4, 9)
print(angka_favorit[0]) 


# Membuat dictionary
print("Karakter Game")

char = {
    "nama": "Raiden Ei",
    "jabatan": "Archon",
    "level": 80,
    "is_active" : True,
}


# Mengakses data
print(char["nama"])  #output : Raiden Ei

#Menambah variabel
char["senjata"] = "Polearm"

print(char["senjata"])

#gabungin dengan list
inventori = ["Engulfing", "Artifact", "Primogem"]
char["inventori"] = inventori

print(char["inventori"][1]) 


