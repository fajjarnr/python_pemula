
data_a = [
    ['101', 'Andi', 85, 79],
    ['102', 'Ahmad', 90, 82],
    ['103', 'Beti', 75, 60],
    ['104', 'Beno', 60, 50],
    ['105', 'Chandra', 40, 45]
]

def cetaknilai(data):
    def hitungnilai(uts, uas):
        return (0.4 * uts) + (0.6 * uas)
    def ambilindeks(nilai):
        idx = ''
        if nilai >= 80:
            idx = 'A'
        elif nilai >= 70:
            idx = 'B'
        elif nilai >= 60:
            idx = 'c'
        elif nilai >= 40:
            idx = 'D'
        else:
            idx = 'E'
        return idx
    
    for baris in data:
        nim = baris[0]
        nama = baris [1] 
        uts = baris[2]
        uas = baris[3]
        nilai = hitungnilai(uts, uas)
        indeks = ambilindeks(nilai)
        print('%s\t%s\t%0.2f\t%s' % (nim, nama, nilai, indeks))

cetaknilai(data_a)