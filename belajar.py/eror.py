# print("hello"
# print(nama)
# print("5" + 5)
# angka = int("abc")
# list data = [1, 2, 5]
#print(list data[0])
# data = {"nama": "alice"}
#print(umur("angka"))
#print(20 / 0)

#try-except

print("=== kalkulator===")

try:
    angka1 = int(input("angka pertama:"))
    angka2 = int(input("angka kedua:"))
    hasil = angka1 / angka2
    print("hasil: ", hasil)
except:
    print("terjadi eror")