Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> conn = sqlite3.connect("AA")
>>> cur = conn.cursor()
>>> sql = '''
	create table Bank(
        id_Bank char(4) not null primary key,
        Nama_Bank varchar(50),
        Alamat_Bank varchar(50)
    )
    '''
>>> cur.execute(sql)
<sqlite3.Cursor object at 0x034BA8A0>
>>> sql = '''
	create table Nasabah(
        id_Nasabah char(4) not null primary key,
        nama_nasabah varchar(50),
        Alamat_Nasabah varchar(50)
    )
    '''
>>> cur.execute(sql)
<sqlite3.Cursor object at 0x034BA8A0>
>>> sql = '''
	create table Rekening(
        No_Rekening char(10) not null primary key,
        Mata_Uang char(3),
        Jumlah int
    )
    '''
>>> cur.execute(sql)
<sqlite3.Cursor object at 0x034BA8A0>
>>> sql = '''
	create table Karyawan(
        id_karyawan char(4) not null primary key,
        username varchar(10),
        nama_karyawan varchar(50)
    )
    '''
>>> cur.execute(sql)
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Bank values('B001', 'BRI', 'jl Perintis')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Bank values('B002', 'Mandiri', 'jl Mawar')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Bank values('B003', 'BNI', 'jl Melati')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Bank values('B004', 'BCA', 'jl Kenanga')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Bank values('B005', 'BTN', 'jl Buntu')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> for row in cur.execute("SELECT * FROM Bank"):
    print('%s, %s, %s' % (row[0], row[1], row[2]))

    
B001, BRI, jl Perintis
B002, Mandiri, jl Mawar
B003, BNI, jl Melati
B004, BCA, jl Kenanga
B005, BTN, jl Buntu
>>> cur.execute("INSERT INTO Nasabah values('N001', 'Budi', 'jl Ahmad Yani')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Nasabah values('N002', 'Bambang', 'jl Patimura')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Nasabah values('N003', 'Andi', 'jl Imam Bonjol')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Nasabah values('N004', 'Sinta', 'jl Panjaitan')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Nasabah values('N005', 'Dewi', 'jl Antasari')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> for row in cur.execute("SELECT * FROM Nasabah"):
    print('%s, %s, %s' % (row[0], row[1], row[2]))

    
N001, Budi, jl Ahmad Yani
N002, Bambang, jl Patimura
N003, Andi, jl Imam Bonjol
N004, Sinta, jl Panjaitan
N005, Dewi, jl Antasari
>>> cur.execute("INSERT INTO Rekening values('0011223344', 'IDR', '3000000')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Rekening values('0011223355', 'IDR', '5000000')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Rekening values('0011223366', 'IDR', '8000000')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Rekening values('0011223377', 'IDR', '12000000')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Rekening values('0011223388', 'IDR', '10000000')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> for row in cur.execute("SELECT * FROM Rekening"):
    print('%s, %s, %s' % (row[0], row[1], row[2]))

    
0011223344, IDR, 3000000
0011223355, IDR, 5000000
0011223366, IDR, 8000000
0011223377, IDR, 12000000
0011223388, IDR, 10000000
>>> cur.execute("INSERT INTO Karyawan values('K001', 'Adit', 'jl Sudirman')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Karyawan values('K002', 'Fajar', 'jl Berkoh')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Karyawan values('K003', 'Fathan', 'jl Teluk')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Karyawan values('K004', 'Maruf', 'jl Puri Teluk')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> cur.execute("INSERT INTO Karyawan values('K005', 'Ferguso', 'jl Aja')")
<sqlite3.Cursor object at 0x034BA8A0>
>>> for row in cur.execute("SELECT * FROM Karyawan"):
    print('%s, %s, %s' % (row[0], row[1], row[2]))

    
K001, Adit, jl Sudirman
K002, Fajar, jl Berkoh
K003, Fathan, jl Teluk
K004, Maruf, jl Puri Teluk
K005, Ferguso, jl Aja
>>> 
