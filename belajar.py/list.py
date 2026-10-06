#list kosong
daftar_kosong = [] #list itu harus memakai [] dan bisa menggabungkan str dan int

#list dengan angka
angka = [1, 2, 3]
print(angka)

nama = ["apep", "koko"]
print(nama)

campuran = ["joko", 50]
print(campuran)

#mengakses elemen
buah = ["apel", "jeruk", "pisang"]
print(buah[0])
print(buah[1])
print(buah[2])

#mengubah elemen
warna = ["merah", "biru", "hijau"]
print(warna)
warna[1] = "kuning"
print(warna) #mengubah yang tengah

buah = ["apel", "jeruk"]
print(buah)
buah.append("durian") #append untuk menambahkan
print(buah)
buah.insert(1, "buah naga") #untuk menyisipkan suatu data
print(buah)

buah.remove("jeruk") #untuk menghapus suatu datanya
print(buah)

buah.pop() #remove paling belakang
print(buah)

del buah[0] #untuk menghapus
print(buah)

#untuk menghitung panjang data list
buah = ["apel", "jeruk", "mangga"]
print(len(buah))

#untuk menggabungkan data list
satu = [1,2,3,4]
print(satu)
dua = [5,6,7]
print(dua)

gabungan = satu + dua
print(gabungan)

#memakai perulangan di data list
banyak_buah = ["jeruk", "anggur", "apel"]
for buah in banyak_buah:
    print(buah)

for i in range(0, len(banyak_buah)):
    print(banyak_buah) #menghitung panjang

#if else di data list
if "apel" in banyak_buah:
    print("ada apel")
else:
    print("tidak ada apel")