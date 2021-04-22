#GRACIA RIZKA PASFICA
#19104064

#Parameter untuk inheritance
class Titik (object) :
    #Constructor
    def __init__(self, x = 0, y = 0) : #penamaan constructor ditandai dengan underscore __
        #Self pada constructor sama dengan this
        self.x = x
        self.y = y

    def pindah(self, x, y) :
        self.x = x
        self.y = y

    def cetak(self) :
        print(f'{self.x}, {self.y}')

#Membuat Object
titik = Titik() #Object titik didapat dari class Titik
titik.cetak() #memanggil fungsi cetak menggunakan object titik
titik.pindah(5, 10) #memanggil fungsi pindah menggunakan object titik (5 : x, 10 : y)
titik.cetak() #memanggil fungsi cetak yang sudah di update
