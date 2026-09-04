# BAB 16 - Magic Methods (Dunder Methods)


#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~


#Penjelasan
# Apa itu Magic Methods? sering juga disebut Dunder Methods (Double Underscore) nama fungsinya diapit oleh dua garis bawah di depan dan di belakang, contoh:
# __init__ , __str__ , atau __len__.

#Fungsi Utama: ini adalah metode "rahasia" yang dipanggil secara otomatis oleh python ketika objekmu berinteraksi dengan fungsi bawaan atau operator matematika.

#Contoh paling sering: kalau kamu membuat objek lalu di-print, biasanya python hanya menampilkan alamat memori yang jelek (misal <__main__.item objek at 0x7f..) 
#                      dengan Dunder Method __str__ kamu bisa mengatur agar objek tersebut menampilkan teks yang rapi dan mudah dibaca manusia.


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~


#Contoh
# Perhatikan bagaimana __str__ mengubah cara python menampilkan objekmu.

class ItemGame:
    def __init__(self, nama, harga):
        self.nama = nama        #self.nama untuk memberikan data nama pada ItemGame
        self.harga = harga

    # Dunder Method untuk representasi string objek
    def __str__(self):
        return f"item: {self.nama} | {self.harga} Gold"     #return untuk mengembalikan nilai / data, juga bisa mengirim hasil keluar dari fungsi
    
    # Dunder Method untuk menghubungkan 2 objek jika ditambah (+)
    def __add__(self, objek_lain):
        return self.harga + objek_lain.harga

# Buat objek
item1 = ItemGame("Pedang Kayu", 100)
item2 = ItemGame("Potion Hp", 50)

# memanggil __str__ otomatis saat dipanggil 
print(item1)
print(item2)

# memanggil __add__ otomatis saat objek dijumlahkan (+)
total_harga = item1 + item2
print(f"total harga kedua item: {total_harga} Gold")


#Keterangan
# kamu tak perlu mengetik print(item1.__str__()) secara manual. kamu cukup ketik print(item1) dan python akan otomatis menjalankan fungsi __str__ di dalamnya


#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~


#Praktik Mandiri
# ​Tantangan untukmu di file BAB_16.py

# [1] ​Buat class bernama Buku dengan atribut judul dan penulis.
# [2] ​Gunakan dunder method __str__ di dalam class tersebut agar ketika objeknya dicetak menggunakan print(), keluar format teks: f"Buku '{self.judul}' karya {self.penulis}".
# [3] ​Buat sebuah objek dari class Buku dengan judul dan penulis pilihanmu.
# [4] ​Cetak objek tersebut menggunakan print() dan buktikan apakah dunder method-nya berjalan otomatis!

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def __str__(self):
        return f"Buku '{self.judul}' karya {self.penulis}"

buku1 = Buku("Pick Me Up", "U-Ne Cho")

print(buku1)

# mulai mudah nih