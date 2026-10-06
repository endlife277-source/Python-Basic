kata = input("masukkan kata: ")
huruf_dicari = input("masukkan huruf yang dicari: ")

for huruf in kata:
    if huruf == huruf_dicari:
        print("huruf", huruf_dicari, "ditemukan dalam kata!")
        break
else: #else harus sejajar dengar for biar gak jadi if else
     print("Huruf", huruf_dicari, "tidak ditemukan dalam kata!")