#                            CONTOH PENGGUNAAN METHOD STATIS                           #

#Deklarasi class aritmatika
class Aritmatika :
        
    @staticmethod
    def tambah(a,b) :
        return a + b
#---------------------------------------------------------------------------------------#
#                                   PENJELASAN METHOD TAMBAH                            #
#   Penggunaan @static method : menandakan bahwa method memiliki access modifier static #
#   Nama method : tambah                                                                #
#   Parameter : a dan b                                                                 #
#   Return : hasil dari a + b                                                           #
#---------------------------------------------------------------------------------------#

    @staticmethod
    def kurang(a,b) :
        return a - b

    @staticmethod
    def bagi(a,b) :
        return a / b
  
    @staticmethod
    def bagi_int(a,b) :
        return a // b
  
    @staticmethod
    def pangkat(a,b) :
        return a ** b

    print(Aritmatika.tambah(5,5))
#---------------------------------------------------------------------------------------#
#                                   MENCETAK DATA                                       #
#   print : mencetak data                                                               #
#   Aritmatika.tambah : memanggil method tambah                                         #
#   Langkah memanggil method : nama_class nama_method(parameter)                        #
#   Peritah di atas artinya, mencetak data pada method tambah dengan niai a = 5, b = 5  #
#---------------------------------------------------------------------------------------#
#   Terjadi ERROR ketika mencetak data karena kesalahan dalam pemanggilan class dan     #
#   method sehingga tidak terdefinisi sebagai class                                     #
#---------------------------------------------------------------------------------------#

    objekA = Aritmatika(5, 5)
    print(objekA.pangkat(2,3))
#---------------------------------------------------------------------------------------#
#                                   MENCETAK DENGAN OBJECT                              #
#   objekA = Aritmatika() : sebuah objek dari class Aritmatika                          #
#   Langkah penggunaan object : nama_object = nama_class()                              #
#   objekA.pangkat(2,3) : objekA memanggil method pangkat dg nilai a = 2, b = 3         #
#---------------------------------------------------------------------------------------#
#   Terjadi ERROR ketika mencetak data karena kesalahan dalam pemanggilan deklarasi     #
#   object ketika memanggil class Aritmatika                                            #
#---------------------------------------------------------------------------------------#
