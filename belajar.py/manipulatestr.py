nama = "budi"
#konversi int ke str dan fungsi +
umur = 30

#cara yang benar harus di konversi dari int ke str
pesan = "nama saya " + nama + ", umur " + str(umur) #fungsi + adalah untuk menambah
print(pesan)

panjang_nama = len(nama) #fungsi len untuk mengetahui panjang pesan
panjang_pesan = len(pesan)

print(panjang_nama)
print(panjang_pesan)

#index
nama = "lulak"

print(nama[0])
print(nama[-1]) #ini untuk indexing nama karakter jadi kita bisa mengetahui nomor namanya

#string slice
print(nama[0:3]) # yang di ambil 0,1,2 ini string slice mengambil sebagian
print(nama[:3]) #jika tidak ada awalnya maka dia dimulai dari 0 sampe 2
print(nama[2:]) #jika tidak ada akhirnya maka dia akan sampai akhir
print(nama[:]) #seluruh namanya 

#string methods 

nama = "joko"
nama_upper = nama.upper() #untuk memperbesar kata dari kecil ke besar
print(nama_upper)
nama_lower = nama.lower() #untuk mengecilkan kata dari kata besar
print(nama_lower)

nama = "joko gendeng"
nama_title = nama.title() #untuk mengkapitalkan kata awal jadi besar
print(nama_title)
nama_capitalize = nama.capitalize() #ini untuk memperbesar kata awalnya aja kata ke kedua gak
print(nama_capitalize)

nama = "  joko   "
nama_strip = nama.strip()
print(nama_strip) # untuk menghapus spasi kanan kiri

kalimat = "i love java"
kalimat_baru = kalimat.replace("java", "kalimantan") #untuk mengganti kata baru

print(kalimat_baru)

nama = "joko salesmak gigi"
jumlah_k = nama.count("k") #untuk menghitung jumk=lah kata ato kalimat
print(jumlah_k)

kalimat = "gigi tonggos"
posisi = kalimat.find("tonggos") #untuk mencari posisi katanya
print(posisi)

#escape character

kalimat = "baris pertama\nbari kedua" #untuk meng enter kalimatnya jadi gak satu baris gitu
print(kalimat)

data = "nama:\tJoko\nUmur:\t30" #\t itu buat meng tab katanya jadi di kasi spasi       
print(data)

path ="C\\user\\Joko\\File" #ini membuat backslahnya jadi 1x semua kalo mau dua bikin jadi 4
print(path)

kalimat2 = "dia berkata \"hello\" kepada saya" #biar membuat "di akhir tetap kebaca"
print(kalimat2)

#string interpolation

nama = "koko"
umur = 40
kota = "solo"

#gunakann f string
profil = f"halo nama saya {nama}, umur {umur}, kota saya di {kota}" #{}ini untuk mengambil variabel
print(profil) #ini lebih mudah gak usah di konversi

harga = 500
jumlah = 3

total = f"total : RP {harga * jumlah}" #bisa juga langsung membuat penjumlahan pake f
print(total)




