def app_tebak_angka():
    import random
    angka_acak = random.randint(1, 10)
    maksimal = 3
    tebakan = 0
    while tebakan < maksimal:
        tebakan += 1
        angka_user = int(input("Masukkan angka: "))
        if angka_user > angka_acak:
            print("angka terlalu besar")
        elif angka_user < angka_acak:
            print("angka terlalu kecil")
        else:
            print("selamat angka benar")
            break
    else:
        print("kamu telah melewati batas maksimal")
        print("angka acak adalah: ", angka_acak)

    input("Enter untuk melanjutkan")
     

def app_menu():
   try:
    while True:
        print("== TEBAK ANGKA ==")
        print("1. Tebak angka")
        print("2. keluar")
        print("== PROGRAM SELESAI ==")
        
        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            app_tebak_angka()
        elif pilihan == 2:
            print("== PROGRAM SELESAI ==")
            break    
        else:
            print("Error: Pilihan tidak valid")
   except:
       print("terjadi eror")
app_menu()