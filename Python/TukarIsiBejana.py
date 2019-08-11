print("Tukar Isi Bejanan\n")

bejA = str(input("Masukan Bejana A : "))
bejB = str(input("Masukan Bejana B : "))
temp = str()

temp = bejA
bejA = bejB
bejB = temp

print("Isi bejana A adalah " + bejA)
print("Isi bejana B adalah " + bejB)