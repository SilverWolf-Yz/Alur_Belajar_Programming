# BAB 14 - Encapsulation (Pembungkusan & Proteksi Data)


#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~


#Penjelasan
# Di dunia nyata, tidak semua informasi atau bagian dalam sistem boleh diakses atau diubah oleh orang lain. Misalnya, saldo ATM atau password akun kita,
# Kita tidak ingin orang lain bisa mengubah nominal saldonya dari luar. Dalam OOP konsep ini dinamakan Encapsulation (Pembungkusan). Tujuannya adalah 
# membatasi akses langsung ke data atau metode di dalam class untukmenjaga keamanan dan integritas data.

#Di python, pembagian tingkat akses ini disimbolkan dengan penamaan :

# Public (self.nama)        : Bisa diakses dan diubah secara bebas diluar class.

# Protected (self._nama)    : Diberi tanda garis bawah satu (_), menandakan data ini sebaiknya tidak diubah dari luar (bersifat internal).

# Private (self.__nama)     : Diberi tanda garis bawah dua (__), Menandakan data ini 'Dikunci Rapat' dan sama sekali tidak bisa diakses atau 
#                             diubah langsung dari luar class. Untuk melihat / mengubahnya kita butuh 'pintu khusus' yang biasa disebut Getter dan Setter.


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~


#Contoh
# Perhatikan bagaimana cara mengunci data agar aman dari intervensi luar :

class rekening_bank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik                  # Public (Bebas diakses)
        self.__saldo = saldo_awal               # Privat (Dikunci rapat dengan double underscore)

    # Getter : Fungsi khusus untuk melihat data private dari luar
    def cek_saldo (self):
        return self.__saldo

    def setor_uang (self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil setor! Saldo anda sekarang : {self.__saldo}")

        else:
            print("Jumlah setor tidak valid!")

# Membuat objek 
akunku = rekening_bank("Ibnu", 2400000)

# Mengakses data publik
print(f"Pemilik akun : {akunku.pemilik}")

# Mengakses data Private dari luar AKAN ERROR :
#print(akunku.__saldo)

# Cara aman melihat saldo menggunakan Getter :
print(f"Saldo saat ini : {akunku.cek_saldo()}")

# Cara aman mengubah saldo menggunakan Setter :
akunku.setor_uang(10000) 

# Atau
akunku.setor_uang(int(input("Masukkan jumlah setor: ")))

# Keterangan:
# Dengan __saldo (private), data di dalamnya terlindungi dari perubahan ilegal di luar class. jika ingin mengubah atau melihatnya, 
# wajib menggunakan method di dalam class itu sendiri, yang disini (setor_uang atau cek_saldo).


#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~


#Praktik Mandiri
# 1. Buat class bernama hero_ml dengan atribut public 'nama' dan atribut private '__hp'.
# 2. Berikan nilai awal __hp sebesar 3000 di dalam __init__.
# 3. Buat method (Getter) bernama 'lihat_hp()' untuk mencetak sisa hp hero tersebut.
# 4. Buat method (Setter) bernama 'kena_damage(jumlah)' untuk mengurangi __hp saat hero diserang.
# 5. Buat objek, lalu coba kurangi hp nya menggunakan method 'kena_damage()' dan lihat hasilnya menggunakan 'lihat_hp()'.

class hero_ml:
    def __init__(self, nama):
        self.nama = nama
        self.__hp = 3400

    def lihat_hp(self):          # Getter
        return self.__hp

    def kena_damage(self, jumlah):     # Setter
        if jumlah > 0:
            self.__hp -= jumlah

        else:
            print("bruh, masa damage nambah darah? ada sih, tergantung hero nya")

# objek
hero = hero_ml("Yu Zhong")

# gunakan method
hero.kena_damage(1000)


print(f"{hero.nama}")
print(f"Hp: {hero.lihat_hp()}")
