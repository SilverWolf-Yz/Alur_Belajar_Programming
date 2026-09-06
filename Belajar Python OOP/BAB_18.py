# BAB 18 - Multiple Inheritance & MRO (Method Resolution Order)


#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~ 


#Penjelasan
# Biasanya, sebuah class anak hanya mewarisi sifat dari satu class induk saja (Single Inheritance / pewarisan tunggal). tapi di Python, kamu bisa melakukan 
# hal yang lebih canggih : Multiple Inheritance.

#Apa itu?
# Kemampuan sebuah class anak untuk mewarisi sifat dari dua atau lebih class induk sekaligus.

#Tantangan (MRO)
# Jika ada 2 Class induk yang punya fungsi dengan nama yang sama, mana yang akan dipanggil duluan oleh python? Disinilah MRO (Method Resolution Order)
# bekerja sebagai sistem penentu urutan prioritas pencarian fungsi oleh Python.


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~


#Contoh
# Perhatikan bagaimana cara menggabungkan 2 kemampuan dari class induk yang berbeda ke dalam satu class anak:

#Class induk 1
class BisaTerbang:
    def bergerak(self):
        return "Terbang melayang di udara!"

#Class induk 2
class BisaBerenang:
    def bergerak(self):
        return "Berenang dengan cepat di dalam air!"

#Class anak mewarisi keduanya sekaligus (Multiple Inheritance)
#Urutan di dalam kurung menentukan prioritas MRO (Mana yang dibaca duluan)
class MonsterLautUdara(BisaTerbang, BisaBerenang):
    pass

#membuat objek
monster = MonsterLautUdara()

#fungsi mana yang akan dipanggil? berdasarkan MRO, karena BisaTerbang ada di urutan pertama :
print(monster.bergerak())

#kamu bisa mengecek urutan MRO menggunakan perintah:
print(MonsterLautUdara.__mro__)

#Keterangan
# Dengan Multiple Inheritance, kamu bisa merakit fitur-fitur unik layaknya merakit komponen robot dari berbagai sumber yang berbeda.


#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~


#Praktik Mandiri

# [1] Buat class induk pertama bernama Pekerja dengan method bekerja() yang mencetak "Sedang mengerjakan proyek...".
# [2] Buat class induk kedua bernama Gamer dengan method main_game() yang mencetak "Sedang mabar game gacha...".
# [3] Buat class anak bernama AnakIT yang mewarisi kedua-duanya sekaligus (class AnakIT(Pekerja, Gamer):).
# [4] Buat objek dari class AnakIT, lalu panggil kedua method (bekerja() dan main_game()) secara bergantian menggunakan objek tersebut.

class Pekerja:              #Class
    def bekerja(self):      #Method
        return "Sedang mengerjakan proyek sistem monitoring daerah."        #menyimpan data

class Gamer:
    def main_game(self):
        return "Sedang mabar game gacha, Genshin Impact."

class AnakIT(Pekerja, Gamer):   #gabungan 2 class
    pass

Silver_Wolf = AnakIT()

print(Silver_Wolf.bekerja())        #panggil bekerja
print(Silver_Wolf.main_game())      #panggil main_game


print(AnakIT.__mro__) #daftar urutannya


