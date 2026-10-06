angka = int(input("masukkan angka: "))

# #dengan if else biasa
if angka >0:
    hasil = "positif"
else:
    hasil = "negatif"

#dengan ternary operator (lebih mudah)
hasil = "positif" if angka > 0 else "non-positif"
print("Angka tersebut: ",hasil)

