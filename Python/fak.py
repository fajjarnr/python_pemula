def faktorial():
    x=int(raw_input("Masukkan angka: "))
    faktorial=1
    for i in range(1,x+1):
        faktorial=faktorial*i
    print ("Faktorial dari " + x + "adalah ",faktorial)