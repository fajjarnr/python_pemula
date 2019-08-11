import os
import sqlite3

con = sqlite3.connect("MyBank.db")
cur = con.cursor()

sql = '''
    create table Bank(
        id char(4) not null primary key,
        nama varchar(50),
        alamat varchar(50)
    )
    '''
cur.execute(sql)

sql = '''
    create table Nasabah(
        id char(4) not null primary key,
        nama varchar(50),
        alamat varchar(50)
    )
    '''
cur.execute(sql)

sql = '''
    create table Karyawan(
        id char(4) not null primary key,
        nama varchar(50),
        alamat varchar(50)
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

repeat = 1
while repeat == 1:
    judul()
    print("\n0. Kembali")
    print("1. Data Bank")
    print("2. Bank Baru")
    print("3. Data Karyawan")
    print("4. Karyawan Baru")
    print("5. Data Nasabah")
    print("6. Nasabah Baru")
    print("7. Edit Data Bank")
    print("8. Edit Data Nasabah")
    print("9. Edit Data Karywan")
    print("10. Delete Data Bank")
    print("11. Delete Data Nasabah")
    print("12. Delete Data Karyawan")
    print("99. Exit")
    pilih = int(input("Masukan Pilihan Anda : "))
    
    if pilih == 1:
        judul()
        print("\n\t### Data Bank ###\t\n")
        print("ID Bank \t Nama Bank \t Alamat Bank")
        for row in cur.execute("SELECT * FROM Bank"):
            print("%s\t %s\t %s\t" % (row[0], row[1], row[2]))
        os.system("pause")
    
    elif pilih == 2:
        print("\n\t### Bank Baru ###\t\n")
        id = input('ID Bank\t: ')
        nama = input('Nama Bank\t\t\t: ')
        alamat = input('Alamat Bank\t\t: ')
        os.system('pause')
        cur.execute('INSERT INTO Bank VALUES(?,?,?)', (id ,nama , alamat))
        con.commit()
    
    elif pilih == 3:
        print("\n\t### Data Karyawan ###\t\n")
        print("ID Karyawan \t Nama Karyawan \t Alamat Karyawan")
        for row in cur.execute("SELECT * FROM Karyawan"):
            print("%s\t %s\t %s\t" % (row[0], row[1], row[2]))
    
    elif pilih == 4:
        print("\n\t### Karyawan Baru ###\t\n")
        id = input('ID Karyawan\t: ')
        nama = input('Nama Karyawan\t\t\t: ')
        alamat = input('Alamat Karyawan\t\t: ')
        os.system('pause')
        cur.execute('INSERT INTO Karyawan VALUES(?,?,?)', (id ,nama , alamat))
        con.commit()

    elif pilih == 5:
        print("### Data Nasabah ###")
        print("ID Nasabah \t Nama Nasabah \t Alamat Nasabah")
        for row in cur.execute("SELECT * FROM Nasabah"):
            print("%s\t %s\t %s\t" % (row[0], row[1], row[2]))
        os.system("pause")
    
    elif pilih == 6:
        print("### Nasabah Baru ###") 
        id = input('ID Nasabah\t: ')
        nama = input('Nama Nasabah\t\t\t: ')
        alamat = input('Alamat Nasabah\t\t: ')
        os.system('pause')
        cur.execute('INSERT INTO Nasabah VALUES(?,?,?)', (id ,nama , alamat))
        con.commit()

    elif pilih == 7:
        print("\n\t### Edit Bank ###\t\n")
        id = input('ID Bank\t: ')
        nama = input('Nama Bank\t\t\t: ')
        alamat = input('Alamat Bank\t\t: ')
        os.system('pause')
        cur.execute("UPDATE Bank SET nama = ? , alamat = ? WHERE id = ?", (nama , alamat, id))
        con.commit()
    
    elif pilih == 8:
        print("\n\t### Edit Nasabah ###\t\n")
        id = input('ID Nasabah\t: ')
        nama = input('Nama Nasabah\t\t\t: ')
        alamat = input('Alamat Nasabah\t\t: ')
        os.system('pause')
        cur.execute("UPDATE Nasabah SET nama = ? , alamat = ? WHERE id = ?", (nama , alamat, id))
        con.commit()

    elif pilih == 9:
        print("\n\t### Edit Karyawan ###\t\n")
        id = input('ID Karyawan\t: ')
        nama = input('Nama Karyawan\t\t\t: ')
        alamat = input('Alamat Karyawan\t\t: ')
        os.system('pause')
        cur.execute("UPDATE Karyawan SET nama = ? , alamat = ? WHERE id = ?", (nama , alamat, id))
        con.commit()

    elif pilih == 10:
        print("\n\t### Delete Bank ###\t\n")
        id = input('ID Bank\t: ')
        nama = input('Nama Bank\t\t\t: ')
        alamat = input('Alamat Bank\t\t: ')
        os.system('pause')
        cur.execute("DELETE FROM Bank WHERE id  = ?", (id,))
        con.commit()
    
    elif pilih == 11:
        print("\n\t### Delete Nasabah ###\t\n")
        id = input('ID Nasabahk\t: ')
        nama = input('Nama Nasabah\t\t\t: ')
        alamat = input('Alamat Nasabah\t\t: ')
        os.system('pause')
        cur.execute("DELETE FROM Nasabah WHERE id  = ?", (id,))
        con.commit()

    elif pilih == 12:
        print("\n\t### Delete Karyawan ###\t\n")
        id = input('ID Karyawan\t: ')
        os.system('pause')
        cur.execute("DELETE FROM Karyawan WHERE id  = ?", (id,))
        con.commit()

    elif pilih == 99:
        break

conn.commit()
cur.close()
conn.close