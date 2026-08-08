# BAB 12 - METHODS & ATRIBUTES (Perilaku Objek)


#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~


#Penjelasan
# Di Bab 11, Objek kita (m1 atau kucing1) baru sebatas menyimpan data (atribut nama dan NIM). Tapi di dunia nyata, Objek tidak cuma diam, 
# Objek bisa melakukan sesuatu (berkelakuan / memiliki aksi).

# Attributes : Variabel yang menempel didalam objek, contohnya nama, warna, umur.

# Methods    : Fungsi yang ada di dalam class yang digunakan untuk memberikan "aksi" atau perilaku pada objek tersebut, misalnya kucing bisa mengeong, 
#              mahasiswa bisa belajar.


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~


#Contoh
# Perhatikan bagaimana kita menambah fungsi kedalam class :

class kendaraan:
    def __init__(self, nama, jenis):
        # ini adalah Attributes:
        self.nama = nama
        self.jenis = jenis
        self.mesin_nyala = False    # mesinnya mati

    # Ini method (fungsi perilaku objek)
    def nyalakan_mesin(self):
        self.mesin_nyala = True
        print(f"mesin {self.nama} sekarang NYALA")

# Membuat Objek
mobil1 = kendaraan("Avanza", "Mobil Keluarga")

# Memanggil method
# print(f"Status awal mesin: {mobil1.mesin_nyala}")
# mobil1.nyalakan_mesin()     # Menjalankan aksi
# print(f"Status akhir mesin: {mobil1.mesin_nyala}.")

#Keterangan
# Setiap fungsi di dalam class wajib mencantumkan self sebagai parameter pertamanya, agar Python tahu objek mana yang sedang memanggil fungsi tersebut.


#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~


#Praktik Mandiri
# 1. buat class bernama karaktergame dengan atribut nama, level, dan hp (health point)
# 2. buat sebuah method di dalam class tersebut bernama serang() yang mencetak kalimat: f"{self.nama} menyerang dengan kekuatan penuh!"
# 3. buatlah minimal 1 objek dari class tersebut, lalu panggil method serang miliknya.

class karaktergame:
    def __init__(self, nama, level, hp):
        self.nama = nama
        self.level = level
        self.hp = hp
        self.Hidup = True

    def serang(self):
        print(f"{self.nama} menyerang dengan kekuatan penuh")

    def menghindar(self):
        print(f"{self.nama} menghindari serangan musuh")

player1 = karaktergame("Silver Wolf lv 999", 80, 7000)
bos1 = karaktergame("Aha", 90, 10000)

print(f"{bos1.nama} Lv. {bos1.level}\n HP: {bos1.hp}")
bos1.serang()

print(f"{player1.nama} Lv. {player1.level}\n HP: {player1.hp}")
player1.menghindar()

#note: aku rasa aku mulai bisa membuat game sendiri ^_^ tapi tujuanku membuat AI sendiri.