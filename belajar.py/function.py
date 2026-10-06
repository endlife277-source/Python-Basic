def nama_function():
    print("aku tampan")

nama_function()
nama_function()

#memanggil function dengan parameter
def nama(nama):
    print("nama aku:",nama)

nama("kanjut")

def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi panjang:",luas)

hitung_luas_persegi_panjang(10,8)
hitung_luas_persegi_panjang(9,3)

def hitung_luas_lingkaran(radius):
    pi = 3.14159
    luas = pi * radius *radius
    return luas

luas1 = hitung_luas_lingkaran(5)
luas2 = hitung_luas_lingkaran(10)

print("luas lingkaran radius 5:",luas1)
print("luas lingkaran radius 10:",luas2)
print("total luas:", luas2 + luas1)

#default parameter harus di belakang dan memakai=
def sapa(nama, sapaan="halo"):
    print(sapaan, nama)

sapa("joko, Hi") #defaultnya menggunakan halo 

#keyword argument

def perkenalan(nama, umur, kota):
    print("Nama:", nama)
    print("Umur:", umur, "tahun")
    print("asal:", kota)
    print("---")


#postional argument (urutan harus selese)
perkenalan("joko", 25, "solo")

#keyword arguments (urutan bebas)
perkenalan(kota="jogja", nama="non", umur=30)

def buat_profil(nama, umur, kota="jogja", pekerjaan="kuli"):
    print(f"=== PROFIL {nama.upper()} ===")
    print(f"umur: {umur} tahun")
    print(f"kota: {kota}")
    print(f"pekerjaan: {pekerjaan}")

#positional + argument 
buat_profil("joko", 25) #menggunakan depault
buat_profil("bob", 30, kota="jaya")

#local variabel

def fungsi_test():
    x = 10
    print("nilai x di dalam funsi:", x)

fungsi_test()
#print(x) tidak bisa karena di luar function

nama_global = "joko" #global variable

def tampilkan_nama():
    print("nama:", nama_global)

def ubah_nama():
    global nama_global
    nama_global = 'bob' #mengubah global variable

tampilkan_nama()
ubah_nama()
tampilkan_nama()

#parameter dinamis

def cetak_biru(*list):
    for item in list:
        print(item)


cetak_biru(1, 2, 3, 4, 5)

def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")

cetak_dict(nama="joko", umur=20, kota="jogja")

