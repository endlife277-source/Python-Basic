#for loop 

for i in range(5):
    print(i)

for i in range(3):
    print("hello") #mencetak hello 3x

print("menghitung mundur")
for i in range(5, 0, -1):
    print(i)

#for loop with str

nama = "python"
for huruf in nama:
    print(huruf)

kata = input("masukan nama: ")
print("huruf-huruf dalam kata: ")
for karakter in kata:
    print("-", karakter)

#while loop

angka = 1
while angka <= 5:
    print(angka)
    angka += 1 #angka = angka +1


#menerima input menggunakan while

paswword = ""
while paswword != "343":
    paswword = input("masukkan password: ")
    if paswword != "343":
        print("password salah coba lagi")
    
print("password benar!")