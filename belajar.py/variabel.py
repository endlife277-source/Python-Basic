#membuat variabel sederha
nama = "budi"  # kota berisi budi berlabel nama
tinggi = 120.5
kota = 'palangkaraya'
saldo = 50
puisi = """
ini adalah diriku
aku senang sama diri ku
"""
is_married = True
is_employed = False

a, b, c = 1, 2, 3

print(type(saldo))  #class int
print(type(tinggi)) #class float
print(type(puisi)) #class str
print(type(is_employed)) #class bool
print(saldo)


nama =input("masukan nama anda: ")
print("hello", nama) #gunakan koma untuk melakukan print dalam 1 baris

umur_text =input("masukan umur anda: ")
umur =int(umur_text) #untuk mengubah str jadi int
print("umur anda", umur)
print("tipe umur", type(umur))

