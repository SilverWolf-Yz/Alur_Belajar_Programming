print("~ ~ ~ ~ ~ / Selamat datang di Kominfo / ~ ~ ~ ~ ~")

#nilai dalam sistem login
ussername = "Samuel Abrijani"
pasword = "Admin123"
max_percobaan = 3
percobaan = 0
login_sukses = False #== agar tidak langsung ke login_sukses

while percobaan < max_percobaan:
    input_name = input("Masukkan Nama: ")
    input_pass = input("Masukkan Pasword: ")

    if input_name == ussername and input_pass == pasword:
        print("Selamat datang Dirjen Aptika dari kominfo")
        login_sukses = True #jika benar lanjut ke if login_sukses
        break
    
    else:
        percobaan = percobaan + 1
        sisa = max_percobaan - percobaan
        print("Login Gagal, Hacker kalau bisa jangan menyerang.")
        print(f"sisa percobaan: {sisa}")

else:
    print("percobaan habis, anda kami tangkap")

#lanjut kesini
if login_sukses == True:
    jumlah_anggota = int(input("Masukkan jumlah anggota: "))        #masukkan banyak anggota agar mengulang sebanyak jumlah_anggota

    for anggota in range(jumlah_anggota):
        nama = input("Masukkan nama anggota: ")                             #masukkan nama angota
        lama_bekerja = int(input("Masukan seberapa lama ia bekerja: "))     #masukkan seberapa lama ia bekerja

        if 0 < lama_bekerja <= 1:       #0-1 ia staf
            jabatan = "Staf"

        elif 1 < lama_bekerja <= 3:     #2-3 ia pengawas
            jabatan = "Pengawas"

        elif 3 < lama_bekerja <= 7:     #4-7 ia manajer tingkat menengah
            jabatan = "manajer Tingkat Menengah"

        elif 7 < lama_bekerja <= 10:    #8-10 ia manager tingkat atas
            jabatan = "Manajer Tingkat Atas"

        elif 10 < lama_bekerja:         #lebih dari 10 ia pensiun
            jabatan = "Pensiun"

        else:
            jabatan = "anda bukan siapa-siapa" #buat yang aneh-aneh kalau ngasih nilai -1
            
        print(f"Nama: {nama} | Jabatan: {jabatan}, pengalaman: {lama_bekerja} Tahun")

print("Sistem Anggota Kominfo Selesai")

#walau satu-satu... agak pusing awalnya, aku buka materi sebelumnya.. 