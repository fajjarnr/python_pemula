import sqlite3
conn = sqlite3.connect("MYBANK.db")
cur = conn.cursor()

def header():
    print('##########################################')
    print('\n\t     MYBANK')
    print('##########################################')
    print()

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
        No_Rekening char(10) not null primary key,
        Mata_Uang char(3),
        Jumlah int
    )
    '''
cur.execute(sql)

sql = '''
    create table Karyawan(
        id_karyawan char(4) not null primary key,
        username varchar(10),
        nama_karyawan varchar(50)
    )
    '''
cur.execute(sql)

repeat = 1
while repeat == 1:
    header()
    print('1. Daftar Bank')
    print('2. Daftar Nasabah')
    print('3. Daftar Karyawan')
    print('4. Nasabah Baru')
    print('5. Karyawan Baru')
    x = int(input('Masukkan Pilihan Anda : '))

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

cur.execute("INSERT INTO Rekening values('0011223344', 'IDR', '3000000')")
cur.execute("INSERT INTO Rekening values('0011223355', 'IDR', '5000000')")
cur.execute("INSERT INTO Rekening values('0011223366', 'IDR', '8000000')")
cur.execute("INSERT INTO Rekening values('0011223377', 'IDR', '12000000')")
cur.execute("INSERT INTO Rekening values('0011223388', 'IDR', '10000000')")

cur.execute("INSERT INTO Karyawan values('K001', 'Adit', 'jl Sudirman')")
cur.execute("INSERT INTO Karyawan values('K002', 'Fajar', 'jl Berkoh')")
cur.execute("INSERT INTO Karyawan values('K003', 'Fathan', 'jl Teluk')")
cur.execute("INSERT INTO Karyawan values('K004', 'Maruf', 'jl Puri Teluk')")
cur.execute("INSERT INTO Karyawan values('K005', 'Agus', 'jl Aja')")

print("================== Data Bank ===================\n")
for row in cur.execute("SELECT * FROM Bank"):
    print('%s\t %s\t %s\t' % (row[0], row[1], row[2]))

print("\n================ Data Nasabah ===================\n")
for row in cur.execute("SELECT * FROM Nasabah"):
    print('%s\t %s\t %s\t' % (row[0], row[1], row[2]))

print("\n================= Data Rekening =================\n")
for row in cur.execute("SELECT * FROM Rekening"):
    print('%s\t %s\t %s\t' % (row[0], row[1], row[2]))

print("\n============== Data Karyawan =====================\n")
for row in cur.execute("SELECT * FROM Karyawan"):
    print('%s\t %s\t %s\t' % (row[0], row[1], row[2]))



print("\n========== Nasabah Baru ==============\n")

nama = input("Masukan Nama Nasabah Baru : ")
alamat = input("Alamat Nasabah : ")
print("Nama Nasabah : ",nama)
print("Alamat Nasabah : ",alamat)



cur.execute('''update nasabah set nama_nasabah='Nizar' where id_nasabah ='N001' ''')
print("\n================ Data Nasabah ===================\n")
for row in cur.execute("SELECT * FROM Nasabah"):
    print('%s\t %s\t %s\t' % (row[0], row[1], row[2]))

