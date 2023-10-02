# while is true just incase if you put number in your name
while True:

    nama = input("Masukan nama : ")

    #this is the condition if the name was not alphabet
    if nama.isdigit():
        print("masukan nama yang benar!")
        continue
    #and this is the condition if the name has less letter than 3
    elif len(nama) < 3:
        print("masukan nama yang valid")
        continue
    else:

        break

# while is true just incase if you either put the wrong number or less number or it has alphabet in it
while True:
    nim = (input("Masukan Nim : "))

    # the condition if the NIM was not digit
    if not nim.isdigit():
        print("NIM harus menggunakan angka!")
        continue

    # the condition if the length of the NIM were less than 12 or more than 12
    elif len(nim) != 12:
        print("masukan NIM yang valid!")
        continue


    else:       

        break

#input nama sekolah
sekolah = input("Masukan nama sekolah : ")

#input nilai (float)
nilai = float(input("Masukan Nilai : "))

#kondisi jika nilai antara 100 dan 80
if nilai <= 100.0 and nilai >= 80.0:
    print(f"\nNilai anda {nilai} bernilai A berbobot 4.00")

#kondisi jika nilai antara 79 dan 77.99
elif nilai <= 79.99 and nilai >= 77.00:
    print(f"\nNilai anda {nilai} bernilai A- berbobot 3.75")

#kondisi jika nilai antara 74 dan 76.99
elif nilai <= 76.99 and nilai >= 74.00:
    print(f"\nNilai anda {nilai} bernilai B+ berbobot 3.50")

#kondisi jika nilai antara 68 dan 73.99
elif nilai <= 73.99 and nilai >= 68.00:
    print(f"\nNilai anda {nilai} bernilai B berbobot 3.00")

#kondisi jika nilai antara 65 dan 67.99
elif nilai <= 67.99 and nilai >= 65.00:
    print(f"\nNilai anda {nilai} bernilai B- berbobot 2.75")

#kondisi jika nilai antara 62 dan 64.99
elif nilai <= 64.99 and nilai >= 62.00:
    print(f"\nNilai anda {nilai} bernilai C+ berbobot 2.50")

#kondisi jika nilai antara 56 dan 61.99
elif nilai <= 61.99 and nilai >= 56.00:
    print(f"\nNilai anda {nilai} bernilai C berbobot 2.00")

#kondisi jika nilai antara 45 dan 55.99
elif nilai <= 55.99 and nilai >= 45.00:
    print(f"\nNilai anda {nilai} bernilai D berbobot 1.00")

#kondisi jika nilai antara 0 dan 44.99
elif nilai <= 44.99 and nilai == 0.00:
    print(f"\nNilai anda {nilai} bernilai E berbobot 0.00")

#kondisi jika rentang angka bukan 0 sampai 100
else:
    print("\nNilai tidak valid, nilai harus berada dalam range 0.00 - 100.00")
         
print(f"\nTerimakasih {nama}, {nim}, dari {sekolah} telah menggunakan program saya.")

print("""
Programmer : Dony
NIM : 065002300034
Program Studi : Sistem Informasi
""")
