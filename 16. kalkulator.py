
angka1 = float(input("Masukan Angka : "))
op = input("Operasi : ")
angka2 = float(input("Masukan angka : "))

if op == "+":
    print(angka1 + angka2)
elif op == "-":
    print(angka1 - angka2)
elif op == "*":
    print(angka1 * angka2)
elif op == "/":
    print(angka1 /  angka2)
else:
    print("invalid proses")