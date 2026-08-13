# BAB 13 - Inheritance (Pewarisan)


#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~


#Penjelasan
# Bayangkan kamu punya beberapa jenis karakter game: karakter biasa, karakter boss, dan karakter NPC (non player character). 
# mereka sama-sama punya atribut dasar seperti nama dan hp. 
# Daripada kamu menulis ulang kode nama dan hp di setiap class yang berbeda, kamu bisa menggunakan inheritance (perawisan).

# Class induk (Parent / Super class): Class utama yang memiliki sifat umum.

# Class Anak (Child / Sub class)    : Class turunan yang mewarisi semua class sifat induk, dan bisa ditambah sifat khususnya sendiri.


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~


#Contoh
# Perhatikan bagaimana class anak bisa "Mewarisi" apa yang dimiliki oleh class induk:

#Class induk
class karakter_umum:
    def __init__(self, nama, hp, level):
        self.nama = nama
        self.hp = hp
        self.level = level

    def info(self):
        print(f"{self.nama} Lv. {self.level}\n Hp: {self.hp}")      # anggap stat dasar di game

#class anak (child) mewarisi karakter_umum menggunakan tanda kurung
class penyihir(karakter_umum):
    def sihir_khusus(self):
        print(f"{self.nama} mengeluarkan sihir inferno!")          # ini kemampuan yang dimiliki tiap character penyihir


penyihir1 = penyihir("Frieren", 5000, 60)

# objek anak bisa mengakses method dari induknya!
penyihir1.info()

# objek anak juga bisa mengakses method miliknya sendiri
penyihir1.sihir_khusus()

#Keterangan:
# Dengan menulis class penyihir(karakter_umum):, secara otomatis class penyihir mendapatkan semuaatribut dan fungsi yang ada di karakter_umum tanpa harus menulis ulang.
# ini membuat kode jauh lebih efisien.


#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~ 


# Praktik Mandiri
# 1. buat class induk bernama kendaraan_darat dengan atribut nama dan kecepatan, serta method jalan().
# 2. buat class anak bernama super_car yang mewarisi kendaraan_darat, dan tambahkan method khusus di dalamnya bernama turbo().
# 3. Buat objek dari super_car, lalu panggil fungsi jalan() (milik induk) dan turbo() (milik anak) secara berurutan.

class kendaraan_darat:                      #induk
    def __init__(self, nama, kecepatan):    #stat umum
        self.nama = nama                    #atribut
        self.kecepatan = kecepatan          #atribut

    def jalan(self):
        print(f"{self.nama} bergerak dengan kecepatan: {self.kecepatan} km/h")

class super_car (kendaraan_darat):
    def turbo(self):
        print(f"{self.nama} menggunakan Turbo!")

super_car1 = super_car("Revuelto", 350)

super_car1.jalan()

super_car1.turbo()