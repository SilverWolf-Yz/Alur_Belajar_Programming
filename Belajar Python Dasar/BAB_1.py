#LEVEL 1 Fondasi Dasar

#BAB 1 - Aturan Main & Output Pertama

#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~

#print 
#print adalah sebuah perintah untuk menampilkan hasil code kita di display, contohnya:

print("Halo Dunia, saya adalah hasil program pertama dari pembuat saya")

#bisa juga menggunakan petik tunggal ('...') nilainya sama-sama untuk string

print('Pembuat saya adalah seorang yang punya ambisi untuk menjadi programmer profesional')

#kenapa kebanyakan programmer menggunakan petik ganda ("...")? 
#karena penggunaan petik tunggal bisa mengganggu jalannya program jika kamu menggunakan kata yang menggunakan petik tunggal eperti i'm, don't, it's, dan lainnya. contohnya:

#print('i'm learning python') 

#print tersebut akan mengalami error karena bagian 'i' karena ' setelah i akan mengakhiri teksnya


#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~


#- Aturan Main Syntax Dasar -

# 1. Syntax atau sintaks adalah tata bahasa
#seperti bahasa manusia yang punya tata bahasa misalnya: subjek + predikat + objek
#benar = Saya Makan Nasi 
#salah = Makan Saya Nasi

#dalam pemrograman:
#benar = print("Hello World")
#salah = Hello World("print")



# 2. Case Sensitivity atau peka huruf besar/kecil
#python membedakan huruf besar dan kecil
#itulah sebabnya pyhon sangat sensitif terhadap huruf besar/kecil. contohnya:

#benar = print("Artoria")
#salah = Print("Artoria")

#itulah python, hanya karena perbedaan satu huruf besar/kecil bisa membuat error



# 3. Indentasi atau kerapian baris
#jangan sembarangan memberi spasi di awal baris kode semua kode dasar harus dimulai dari kiri
#spasi di awal baris memiliki arti logis tersendiri. 

#salah:
#  print("agus lapar buk")
#benar:
#print("agus lapar buk")

#nanti kita bisa bahas lebih lanjut di BAB 4 (Pengkondisian) dan BAB 5 (Perulangan)


#       ~ ~ ~ ~ ~ / C / ~ ~ ~ ~ ~


#- Menggunakan Komentar -

#komentar atau (#) seperti yang kita lihat selama ini bertujuan untuk menulis pengingat atau penjelasan di dalam file kode kita agar tidak lupa
#di python kita menggunakan simbol pagar (#). apapun yang ditulis dengan simbol pagar tidak akan dijalankan oleh program
#contohnya seperti pembicaraan kita ini, coba tekan logo ▷ dengan kursor yang akan menjalankan (Run) kode ini
#hasilnya komentar (#) tidak akan muncul di Terminal / display