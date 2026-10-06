angka_rahasia = 7

while True:
    tebakan = int(input("Tebak angka (1-10): "))

    if tebakan == angka_rahasia:
        print("Berhasil")
        break #break ini untuk menghentikan perulangan
    else:
        print("Gagal")

#continue

for i in range(10):
    if i % 2 == 0: #jika genap 
        continue   #lewati, lanjut ke angka selanjutnya
    print("ganjil", i)       # hanya mencetak angka ganjil


