class persegipanjang:
    def __init__(self, p=0, l=0):
        self.__panjang = p
        self.__lebar = l
    def setvalue(self, p, l):
        self.__panjang = p
        self.__lebar = l
    def getp(self):
        return self.__panjang
    def get1(self):
        return self.__lebar
    def luas(self):
        return self.__panjang * self.__lebar

obj = segiempat(8, 6)
obj.luas()
obj.keliling()

# obj didefinisi tapi bukan persegipanjang melainkan segiempat
# obj.keliling() dipanggil tp dalam syntax tidak ada fungsi dari keliling() 