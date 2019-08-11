class segiempat:
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    def luas(self):
        return self.panjang * self.lebar
    def keliling(self):
        return 2 * (self.panjang + self.lebar)

obj.luas()
obj.keliling()

# obj tidak didefinisi tapi dipanggil dg printah obj.luas() dan obj.keliling()