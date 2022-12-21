# def balik_angka(num):
#     return int(str(num)[::-1])

# bilangan = 1234567
# print (balik_angka(bilangan))

def reverse(*input):
    i = len(input)
    result = []

    while i >= 1:
        result.append(input[i-1])
        i = i - 1

    print(result.append)

reverse(1, 2, 3, 4, 5)