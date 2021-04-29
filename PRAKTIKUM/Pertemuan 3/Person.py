# DEKLARASI CLASS
class Person :

    # Constructor
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

#------------------------------------------------------------------------#
#   CONSTRUCTOR                                                          #
#                                                                        #
#   Ciri khusus penggunaan constructor :                                 #
#   ==> terdapat " __init__ "                                            #
#   ==> pada parameter terdapat self                                     #
#   ==> terdapat pemberian nilai atribut menggunakan self                #
#------------------------------------------------------------------------#

    # Method untuk cetak data
    def printname(self):
        print(self.firstname, self.lastname)
