#                   CONTOH CLASS, OBJECT, ATTRIBUTE STATIS                  #

#Deklarasi class
class PersegiPanjang :

  # Variable biasa
  counter = 0

  # Constructor
  def __init__(self, p, l) :
    # Instance/object variable
    self.panjang = p
    self.lebar = l

    # Encapsulation
      # Setter
    def ubahPanjang (self, p) :
        self.panjang = p
  
    def ubahLebar (self, l) :
        self.lebar = l
    #-- End Encapsulation

  #Method untuk perhitungan luas dan keliling
  def hitungLuas(self) :
    return self.panjang * self.lebar
  
  def hitungKeliling(self) :
    return 2 * (self.panjang + self.lebar)

  #Method untuk mencetak data
  def cetakLuas(self):
    print(f'Luas persegi Panjang\t\t: {self.hitungLuas()} ')
  
  def cetakKeliling(self):
    print(f'Keliling persegi Panjang\t: {self.hitungKeliling()} ')


#DEKLARASI OBJECT
objekPP1 = PersegiPanjang(10, 8)

objekPP2 = PersegiPanjang(9, 8)

objekPP3 = PersegiPanjang(8, 8)

#Memanggil method menggunakan object
objekPP1.cetakLuas()

objekPP1.cetakKeliling()

#Memberi nilai pada atribut menggunakan object
objekPP1.counter = 10

#---------------------------------------------------------------------------#    
#                               HASIL RUNNING                               #
#   Luas Persegi panjang : (memanggil method hitungLuas)                    #
#   Keliling Persegi panjang : (memanggil method hitungKeliling)            #
#   Pada method hitungLuas dan hitungKeliling terdapat parameter self       #
#       yang artinya memanggil constructor.                                 #
#   Ketika method memanggil self.panjang dan self.lebar pada return maka    #
#       nilainya didapat dari constructor, dan constructor mendapat nilai   #
#       dari Object yang memanggil.                                         #
#   ==> method hitungLuas menggunakan objekPP1                              #
#   ==> method hitungKeliling menggunakan objekPP1                          #
#   ObjectPP1 memiliki parameter panjang 10, lebar 8                        #
#---------------------------------------------------------------------------#
