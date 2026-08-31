# BAB 15 - Polymorphism (Puncak Arsitektur OOP)


#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~


#Penjelasan
# Dalam dunia pemrograman OOP, Polymorphism adalah konsep di mana beberapa class yang berbeda memiliki nama method yang sama, 
# tetapi melakukan aksi yang berbeda-beda. Bayangkan perintah "bersuara!". jika perintah itu diberikan ke kucing, ia akan mengeong ("Nyan~").
# jika diberikan ke anjing, ia akan menggonggong ("Woof!"). Perintahnya sama (method bersuara), tapi wujud atau hasil aksinya berbeda 
# tergantung siapa objek yang menerimanya.


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~ 


#Contoh
# Perhatikan bagaimana method yang sama menghasilkan perilaku yang berbeda pada class yang berbeda :

class kucing:
    def bersuara (self):
        return "Nyan~"

class anjing:
    def bersuara(self):
        return "Woof!"

# Fungsi yang menerima objek apa saja, asalkan punya method 'bersuara' 
def cetak_suara(objek_hewan):
    print(objek_hewan.bersuara)

# Membuat objek
hewan1 = kucing()       # tanda kurung supaya memuat fungsi di dalamnya
hewan2 = anjing()

# Memanggil fungsi yang sama, tapi hasilnya berbeda!
cetak_suara(hewan1) # Output "Nyan~"
cetak_suara(hewan2) # Output "Woof!"

#Keterangan : 
# Meskipun fungsi cetak_suara tidak tahu apakah yang masuk itu objek kucing atau anjing, selama objek tersebut memiiki method bernama bersuara(),
# program akan berjalan mulus dan menyesuaikan sendiri. inilah kekuatan besar polymorphism dalam membuat kode yang fleksibel.


#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~


#Praktik Mandiri
# 1. Buat dua class yang berbeda.
# 2. Di dalam kedua class tersebut, buat method dengan nama yang sama persis.
# 3. Buat di kedua class tersebut untuk mencetak hasil yang berbeda.
# 4. Buat objek masing-masing class, lalu jalankan method yang kamu buat dari masing-masing objek tersebut 
#    (boleh menggunakan fungsi luar atau dipanggil langsung).

class stat_umum:                    #kasih stat umum kayak nama
    def __init__(self, nama):
        self.nama = nama

class Saber(stat_umum):                                     # Saber keluar Excalibur
    def serangan_khusus(self):
        return (f"{self.nama} menggunakan Excalibur!")

class Jalter(stat_umum):                                    # Jalter keluar La Grondement Du Haine
    def serangan_khusus(self):
        return (f"{self.nama} menggunakan La Grondement Du Haine!")

def aksi(char):                                             # Buat aksi agar keduanya jalan walau beda
    print(char.serangan_khusus())

char1 = Saber("Altria")                                     # Objek
char2 = Jalter("Jeanne Alter")

aksi(char1)                                                 # Tampilin di layar (btw disini hampir tanpa print)
aksi(char2)


