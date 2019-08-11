a, b, c = 0,1,0
num = input("Masukan jumlah deret fibonaci : ")
num = int(num)
for i in range(num):
    print(a,'',end='')
    c = a + b
    a = b
    b = c