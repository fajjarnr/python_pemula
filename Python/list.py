data_a= [
    ['101', 'Irsyad', 85, 79],
    ['102', 'Rahmat', 90, 82],
    ['103', 'Beni', 75, 60],
    ['104', 'Beno', 60, 50],
    ['105', 'Chandra', 40, 45],
    ['106', 'Deni', 65, 50],
    ['107', 'Diki', 70, 75],
    ['108', 'Ega', 35, 40],
    ['109', 'Farah', 90, 85]
]

def cetaknilai(data):
    def hitungnilai(uts, uas):
        def ambilindeks(nilai):
            idx = ''
            if nilai >= 80:
                idx = 'A'
            elif nilai >= 70:
                idx = 'B'
            elif nilai >= 60:
                idx = 'C'
            elif nilai >= 40:
                idx = 'D'
            else:
                idx = 'E'
            return idx
        for baris in data_a:
            nim = baris[0]
            nama = baris[1]
            uts = baris[2]
            uas = baris[3]
            nilai = hitungnilai(uts, uas)
            indeks = ambilindeks(nilai)

print('%s\t%s\t%0.2f\t%s' % (nim, nama, nilai, indeks))

cetaknilai(data_a)