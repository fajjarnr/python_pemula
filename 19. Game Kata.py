
kunci = "bakso"
kata =""
jumlah = 0
batas = 5
lewat = False

while kata != kunci and not(lewat):
    if jumlah < batas:
        kata = input("Masukan Kata : ")
        jumlah += 1
    else:
        lewat = True

if lewat:
    print("Gagal !!!")
else:
    print("Benar !!!")