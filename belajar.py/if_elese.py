nilai = int(input("masukan nilai: "))

if nilai > 60:
    print("anda lulus")
else:
    print("tidak lulus") #if else digunakan untuk memberi dua kondisi true dan false 

#else if

nilai = int(input("masukan nilai: "))

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
elif nilai >= 70:
    print("Grade C")
else:
    print("Grade F")

#digunakan untuk memeriksa kondisi tambahan secara berurutan apabila kondisi if utama tidak terpenuhi.
#elif kalo misalnya dan harus di akhiri else
#kalo misalnya pake if dia bakal muncul semua 

#kondisi operator logika

umur = int(input("masukan umur anda: "))
punya_sim = input("Punya sim? (ya/tidak): ")

if umur >= 17 and punya_sim == "ya":
    print("Boleh mengendarai")
else:
    print("tidak boleh mengendarai")

#nested if atau if berserang 
#kita bisa menempatkan if dalam if

usarename = input("Usarename: ")
password = input("Password: ")

if usarename == "admin":
    if password == "434":
        print("Login berhasil")
        print("selamat datang admin")
    else:
        print("Password salah")
else:
    print("Usarename tidak ditemukan")

#pernytaan match case

hari = input("masukan nama hari: ").lower()

match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
       print("hari kerja")
    case "sabtu" | "minggu":
       print("hari libur")
    case _:
      print("tidak valid")




