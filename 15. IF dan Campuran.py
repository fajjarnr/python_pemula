
def nilai(angka1, angka2, angka3):
    if angka1 >= angka2 and angka1 >= angka3:
        return angka1
    elif angka2 >= angka1 and angka2 >= angka3:
        return angka2
    else:
        return angka3

print(nilai(200, 60, 3))