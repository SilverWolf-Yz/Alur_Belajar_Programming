#Level 4 - MENUJU PROYEK NYATA 

#       ~ ~ ~ ~ ~ / A / ~ ~ ~ ~ ~

# Penanganan Error (Exception Handling)
# Saat kamu menjalankan program dan saat dijalankan ada input yang salah (misal, harusnya angka (int) malah di isi huruf (str)).
# pesanmu langsung "mati mendadak" dengan pesan error merah yang panjang? 

# Itulah kenapa kita butuh Exception Handling menggunakan 'try' dan 'except'. 
# ini adalah jaring pengaman agar program tetap berjalan meski ada kesalahan.

# Konsep try dan error :
#try    : kita mencoba menjalankan kode yang berpotensi error.
#except : jika terjadi error dalam try, program akan lompat ke sini alih_alih crash.

#Contoh:

try:
    angka = int(input("Masukan angka untuk dibagi 10: "))
    hasil = 10 / angka
    print(f"Hasilnya: {hasil}")

except ZeroDivisionError:
    print("Error : Tidak bisa membagi dengan nol!")
except ValueError:
    print("Error: Kamu harus memasukkan angka, bukan huruf!")

#Keterangan:
#try untuk melakukan operasi
#except untuk memberi hasil jika input salah/menghasilkan error

#       ~ ~ ~ ~ ~ / B / ~ ~ ~ ~ ~ 

# Tantangan BAB 8 : Aplikasi Anti Crash
# Tantangan: menyempurnakan fungsi kalkulator pembagian sederhana.

def bagi_angka(dibagi, pembagi):                            #operasi hitung
    hasil = dibagi / pembagi
    return hasil                                            #mengirim hasil keluar defb dan mendarat ke variabel hasil_bagi

while True:                                                 #mengulangi
    try:                                                    #mencoba
        dibagi = float(input("masukkan yang dibagi: "))     #meminta input dibagi pengguna
        pembagi = float(input("masukan pembagi: "))         #meminta input pembagi

        hasil_bagi = bagi_angka(dibagi, pembagi)            #return masuk kesini melalui bagi_angka
        print(f"hasil nya: {hasil_bagi}")                   #print hasil bagi
        break                                               #mengakhiri perulangan selama bernilai True (benar dan tidak error)

    except ZeroDivisionError:                               #jika error karena mengisi nilai 0
        print("Error : Tidak bisa membagi dengan nol!")
    except ValueError:                                      #jika error karena mengisi nilai huruf
        print("Error: Kamu harus memasukkan angka, bukan huruf!")

#Keterangan:
#ingat jangan masukan def seperti ini kedalam while true lagi T-T
#dan jangan lupa break agar kipas laptop aman :v

#jujur agak pusing sih ini...