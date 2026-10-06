#tanda tanda buat memakai penjumlahan
#- kurang, + tambah,* kali, / bagi
#pembagian bulat //,% modulo, berpangkat **

a = 10
b = 50

print(a / b)

#operator penugasan penjumlahan=
koka = 9
print(koka)


#operator perbandingan
print(a<b) #lebih kecil dari b true
print(a>b) #lebih dari b false
print(a<=b) #lebih kecil atau sama true
print(a>=b) #lebih besar atau sama false
print(a==b) #sama dengan false
print(a != b) #tidak sama dengan true

#kalo tipe str hanya bisa == != itu saja

#operator logika
#and (dan) menghasilkan true jika dua kondisi true 
#or (atau) menghasilkan true jika salah satu kondisi true
#not (tidak) membalik boolian 

umur = 70
print(umur > 60 and umur <80)

hari = "jumat"
print(hari == "jumat" or hari == "sabtu")

aktif = True
print(not aktif)

#operator string
# concatenion(+) menambah str
# repetion(*) mengulang str jumlah angka
# membership(in) mengecek apakah text berada dalam str

nama_depan = "joe"
nama_belakang = "berkin"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

kata = "hi"
print(kata * 3)

kalimat = "python itu bahasa"
print("bahasa" in kalimat) #true karena bahasa memang ada di variabel kalimat



