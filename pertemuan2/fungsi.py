def greeting(jam):
    if jam < 12:
        return "Selamat Pagi!"
    elif jam < 18:
        return "Selamat Siang!"
    else:
        return "Selamat Malam!"

print(greeting(12))
