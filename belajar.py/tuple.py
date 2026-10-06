point = (5, 10)
print(point[5])
print(point[10]) #untuk memanggil data tuple

#untuk data yang tidak berubah
tanggal_lahir = (10, 8, 2001)
print("Tanggal lahir:", tanggal_lahir)

#iterasi di tuple
for e in tanggal_lahir:
    print(e)

#iterasi di tuple dengan index
for i in range(len(tanggal_lahir)):
    print(tanggal_lahir[i])