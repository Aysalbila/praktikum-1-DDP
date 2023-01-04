while True:
    number = int(input("Masukan angka :"))
    if number == 0:
        break
    if number % 2 == 0:
        print("Bilangan genap")
    else:
        print("Bilangan ganjil")