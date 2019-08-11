print("CV. XYZ")


nama = str(input("Masukan Nama : "))
jjk = int(input("Jumlah Jam Kerja : "))

if jjk <= 40:
    total= jjk * 20000
    print('Total Gaji Anda adalah : ',total)
else:
    lembur = jjk - 40
    total = 40 * 20000 + lembur * 50000
    print('Total Gaji Anda adalah : ',total)
