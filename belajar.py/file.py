print("=== SIMPAN DATA NILAI ===")

file = open("nilai-siswa.txt", "w")

while True:
    nama = input("Nama siswa (enter untuk selesai): ")
    if nama == "":
        break

    nilai = input("Nilai: ")

    #tulis ke file
    file.write(nama + "," + nilai + "\n")
    print("data", nama, "berhasil disimpan")

file.close()
print("Semua data berhasil disimpan ke nilai-siswa.txt")

#membaca file
print("=== MENAMPILKAN DATA NILAI ===")

file = open("nilai-siswa.txt", "r")

for line in file:
    data = line.strip().split(",")
    print(data[0], ":", data[1])

file.close

print("=== SELESAI ===")

#menampilkan data tanpa file.close menggunakan with
print("=== menampilkan data siswa ===")


with open("nilai-siswa.txt", "r") as file:
     for line in file:
        data = line.strip().split(",")
        print(data[0], ":", data[1])

 
print("selesai")