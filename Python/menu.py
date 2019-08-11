import os
import sqlite3

conn = sqlite3.connect("MyBank.db")
cur = conn.cursor()

sql = '''
    create table Bank(
        id_Bank char(4) not null primary key,
        Nama_Bank varchar(50),
        Alamat_Bank varchar(50)
    )
    '''
cur.execute(sql)

sql = '''
    create table Nasabah(
        id_Nasabah char(4) not null primary key,
        nama_nasabah varchar(50),
        Alamat_Nasabah varchar(50)
    )
    '''
cur.execute(sql)

sql = '''
    create table Rekening(
        id_Nasabah char(4),
        nama_nasabah varchar(50),
        No_Rekening char(10) not null primary key,
        Mata_Uang char(3),
        Jumlah int
    )
    '''
cur.execute(sql)

sql = '''
    create table Karyawan(
        id_karyawan char(4) not null primary key,
        nama_karyawan varchar(50),
        alamat_karyawan varchar(50),
    )
    '''
cur.execute(sql)

cur.execute("INSERT INTO Bank values('B001', 'BRI', 'jl Perintis')")
cur.execute("INSERT INTO Bank values('B002', 'CIMB', 'jl Mawar')")
cur.execute("INSERT INTO Bank values('B003', 'BNI', 'jl Melati')")
cur.execute("INSERT INTO Bank values('B004', 'BCA', 'jl Kenanga')")
cur.execute("INSERT INTO Bank values('B005', 'BTN', 'jl Buntu')")

cur.execute("INSERT INTO Nasabah values('N001', 'Budi', 'jl Ahmad Yani')")
cur.execute("INSERT INTO Nasabah values('N002', 'Beni', 'jl Patimura')")
cur.execute("INSERT INTO Nasabah values('N003', 'Andi', 'jl Imam Bonjol')")
cur.execute("INSERT INTO Nasabah values('N004', 'Sinta', 'jl Panjaitan')")
cur.execute("INSERT INTO Nasabah values('N005', 'Dewi', 'jl Antasari')")

cur.execute("INSERT INTO Rekening values('N001', 'Budi', '0011223344', 'IDR', '3000000')")
cur.execute("INSERT INTO Rekening values('N002', 'Beni', '0011223355', 'IDR', '5000000')")
cur.execute("INSERT INTO Rekening values('N003', 'Andi', '0011223366', 'IDR', '8000000')")
cur.execute("INSERT INTO Rekening values('N004', 'Rani', '0011223377', 'IDR', '12000000')")
cur.execute("INSERT INTO Rekening values('N005', 'Dewi', '0011223388', 'IDR', '10000000')")

cur.execute("INSERT INTO Karyawan values('K001', 'Adit', 'jl Sudirman')")
cur.execute("INSERT INTO Karyawan values('K002', 'Fajar', 'jl Berkoh')")
cur.execute("INSERT INTO Karyawan values('K003', 'Fathan', 'jl Teluk')")
cur.execute("INSERT INTO Karyawan values('K004', 'Maruf', 'jl Puri Teluk')")
cur.execute("INSERT INTO Karyawan values('K005', 'Agus', 'jl Aja')")


# Judul
def judul():
    print('##########################################')
    print('\n\t         MYBANK    \n')
    print('##########################################')
    print()

def bank():
    print("ID Bank \t Nama Bank \t Alamat Bank")
    for row in cur.execute("SELECT * FROM Bank"):
        print("%s\t %s\t %s\t" % (row[0], row[1], row[2]))

def nasabah():
    print("ID Nasabah \t Nama Nasabah \t Alamat Nasabah")
    for row in cur.execute("SELECT * FROM Nasabah"):
        print("%s\t %s\t %s\t" % (row[0], row[1], row[2]))

def rekening():
    print("ID Nasabah \t Nama Nasabah \t No Rekening \t Mata Uang \t Jumlah")
    for row in cur.execute("SELECT * FROM karyawan"):
        print("%s\t %s\t %s\t %s\t %s\t" % (row[0], row[1], row[2], row[3], row[4]))

def karyawan():
    print("ID Karyawan \t Nama Karyawan \t Alamat Karyawan")
    for row in cur.execute("SELECT * FROM Karyawan"):
        print("%s\t %s\t %s\t" % (row[0], row[1], row[2]))

repeat = 1
while repeat == 1:
    judul()
    print("\n0. Kembali")
    print("1. Bank")
    print("2. Nasabah")
    print("99. Exit")
    pilih = int(input("Masukan Pilihan Anda : "))

    if pilih == 1:
        judul()
        print("\n1. Data Bank")
        print("2. Karyawan\n")
        x = int(input("Masukan Pilihan Anda : "))
        if x == 1:
            judul()
            print("\n1. Data Bank")
            print("2. Bank Baru")
            a = int(input("Masukan Pilihan Anda : "))
            if a == 1:
                judul()
                print("\n\t### Data Bank ###\t\n")
                bank()
                os.system("pause")

            else:
                judul()
                print("\n\t### Bank Baru ###\t\n")
                id_Bank = input("id_Nasabah : ")
                Nama_Bank = input("Nama_Nasabah : ")
                Alamat_Bank = input("Alamat Nasabah : ")
                cur.execute('INSERT INTO buku VALUES(?,?,?,?,?,?)', (id_Bank, Nama_Bank, Alamat_Bank)

        else:                    
            print("1. Data Karyawan")
            print("2. Karyawan Baru")
            y = int(input("Masukan Pilihan Anda : "))
            if y == 1:
                print("### Data Karyawan ###")
                os.system("pause")

            else:
                print("### Karyawan Baru ###")
                id_Karyawan = input("ID Karyawan : ")
                Nama_Karyawan = input("Nama Karyawan : ")
                Alamat_Karyawan = input("Alamat Karyawan : ")
                cur.execute('INSERT INTO buku VALUES(?,?,?,?,?,?)', (id_Karyawan, Nama_Karyawan, Alamat_Karyawan)
            break
                

    elif pilih == 2:
        print("1. Data Nasabah")
        print("2. Rekening")
        z = int(input("Masukan Pilihan Anda : "))
        if z == 1:
            print("1. Data Nasabah")
            print("2. Nasabah Baru")
            b = int(input("Masukan Pilihan Anda : "))
            if b == 1:
                print("### Data Nasabah ###")
                nasabah()
                os.system("pause")

            else:
                print("### Nasabah Baru ###")
                id_Nasabah = input("id_Nasabah : ")
                Nama_Nasabah = input("Nama_Nasabah : ")
                Alamat_Nasabah = input("Alamat Nasabah : ")
                cur.execute('INSERT INTO buku VALUES(?,?,?,?,?,?)', (id_Nasabah, Nama_Nasabah, Alamat_Nasabah)
                
        
        else:
            print("1. Data Rekening")
            print("2. Rekening Baru")
            print("3. Edit Data Rekening")
            c = int(input("Masukan Pilihan Anda : "))
            if c == 1:
                print("### Data Rekening ###")
                rekening()
                os.system("pause")

            elif c == 2:
                print("### Rekening Baru ###")
                id_Nasabah = input("ID Nasabah : ")
                Nama_Nasabah = input("Nama Nasabah : ")
                No_Rekening = input("No Rekening : ")
                Mata_Uang = input("Mata Uang : ")
                Jumlah = input("Jumlah Uang : ")
                cur.execute('INSERT INTO buku VALUES(?,?,?,?,?,?)', (id_Nasabah, Nama_Nasabah, No_Rekening, Mata_Uang, Jumlah)
                

            else:
                print("### Edit Data Rekening ###")
                id_Nasabah = input("ID Nasabah : ")
                Nama_Nasabah = input("Nama Nasabah : ")
                No_Rekening = input("No Rekening : ")
                Mata_Uang = input("Mata Uang : ")
                Jumlah = input("Jumlah Uang : ")
                cur.execute('INSERT INTO buku VALUES(?,?,?,?,?,?)', (id_Nasabah, Nama_Nasabah, No_Rekening, Mata_Uang, Jumlah)
                
    elif pilih == 99:
        break

cur.close()
conn.close()
