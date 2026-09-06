#BAB 17 - Abstract Class (Kelas Abstrak)


#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~


#Penjelasan
# Bayangkan kamu sedang membuat sebuah game atau sistem besar yang dengan banyak jenis karakter atau alat. kamu ingin memastikan bahwa semua class anak wajib memiliki fungsi
# tertentu (misalnya fungsi serang() atau jalan()), dan jika ada class anak yang lupa membuatnya, python akan menegurmu (error).

#Disinilah Abstract class (Kelas Abstrak) berperan untuk:

# Kerangka Kasar                    : Ia adalah sebuah class khusus yang berfungsi sebagai standar atau aturan wajib bagi class turunannya.

# Tidak bisa dibuat objek langsung  : Kamu tidak bisa membuat objek langsung dari class abstrak ini. ia hanya boleh diwarisi (inherit.)

# Untuk membuatnya, kita butuh modul bawaan python bernama 'abc' (Abstract Base Classes).


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~


#Contoh
# Perhatikan bagaimana class abstrak memaksa class anak untuk patuh pada aturan:

from abc import ABC, abstractmethod     # Panggil modul pakai from (dari) abc import (kirim ke sini) ABC (kotaknya), abstractmethod (barangnya) (untuk menetapkan aturan wajib yang harus dipatuhi oleh setiap class turunan)

# Class induk abstrak  (kerangka utama)
class Karakter(ABC):

    @abstractmethod
    def serang(self):
        pass            # Tidak ada isi, hanya sebagai aturan wajib

# Class anak 1
class Pemanah(Karakter):
    # wajib membuat fungsi serang, jika tidak = error
    def serang(self):
        return "Menembakkan panah jarak jauh!"

# Class anak 2
class Guard(Karakter):
    def serang(self):
        return "Memukul dengan kekuatan penuh!"

# Membuat objek dari class pemanah (berhasil)
pemanah1 = Pemanah()
print(pemanah1.serang())

# Jika kamu mencoba membuat objek langsung dari class Karakter (Karakter())
# Python akan menolaknya karena bersifat abstrak.

#Keterangan:
# @abstractmethod adalah penanda khusus (decorator) yang memaksa setiap class turunan untuk wajib menulis ulang (mengimplementasikan) fungsi serang(). ini sangat berguna ketika
# kamu bekerja dalam tim atau membuat sistem yang kompleks agar tidak ada fungsi yang terlewat.


#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~


#Praktik Mandiri
#Tantangan untukmu di file BAB_17.py:

# [1] Import modul abstrak dengan menuliskan: from abc import ABC, abstractmethod.
# [2] Buat class abstrak bernama AlatElektronik yang mewarisi ABC.
# [3] Di dalam class tersebut, buat sebuah method abstrak bernama nyalakan() menggunakan dekorator @abstractmethod.
# [4] Buat class anak bernama Laptop yang mewarisi AlatElektronik, dan isi method nyalakan() dengan mencetak kalimat: "Laptop menyala, menampilkan logo OS!".
# [5] Buat objek dari class Laptop, lalu panggil fungsi nyalakan() tersebut.


from abc import ABC, abstractmethod     # modul abstraknya

class AlatElektronik(ABC):

    @abstractmethod
    def nyalakan(self):
        pass

# class anak
class Laptop(AlatElektronik):
    def nyalakan(self):
        return "Laptop menyala, menampilkan logo OS!"

Pixwar = Laptop()
print(Pixwar.nyalakan())

# Singkat ya ^_^