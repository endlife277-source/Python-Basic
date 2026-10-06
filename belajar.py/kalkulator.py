#program simple calculator
def app_pertambahan():
    print("== PROGRAM PERTAMBAHAN ==")
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 + angka2
    print("hasil pertambahan =", hasil)
    print("=== program selesai ===")
    input("enter untuk lanjut")

def app_pengurangan():
    print("== PROGRAM PENGURANGAN ==")
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 - angka2
    print("hasil pengurangan =", hasil)
    print("=== program selesai ===")
    input("enter untuk lanjut")

def app_perkalian():
    print("== PROGRAM PERKALIAN ==")
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 * angka2
    print("hasil perkalian =", hasil)
    print("=== program selesai ===")
    input("enter untuk lanjut")

def app_pembagian():
    print("== PROGRAM PEMBAGIAN ==")
    angka1 = int(input("angka1: "))
    angka2 = int(input("angka2: "))
    hasil = angka1 / angka2
    print("hasil pembagian =", hasil)
    print("=== program selesai ===")
    input("enter untuk lanjut")

def app_menu():
   try: 
    while True:
     print("== PROGRAM KALKULATOR ==")
     print("1. pertambahan")
     print("2. pengurangan")
     print("3. perkalian")
     print("4. pembagian")
     print("5. Tutup")
     print("== PROGRAM KALKULATOR ==")

    
     pilihan = int(input("Pilihan: "))
 
     if pilihan == 1:
         app_pertambahan()
     elif pilihan == 2:
         app_pengurangan()
     elif pilihan == 3:
         app_perkalian()
     elif pilihan == 4:
         app_pembagian()
     elif pilihan == 5:
         print(" Anda telah Keluar")
    
         break
   except:
      print("terjadi eror")    

  
app_menu()
