# angka = 1

# while angka > 0 and angka < 11:
#     angka = int(input("Masukan bilangan bulat: "))
#     if angka >= 1:
#         print("Bilangan positif")
#     elif angka < 0:
#         print("Bilangan Negatif")
#     else:
#         print("Bilangan Nol")

while True:
    nama = input("Masukkan nama anda: ")
    if nama == "x":
        break
    elif nama == "surya":
        continue
    print("Selamat Datang", nama)
