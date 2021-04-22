#GRACIA RIZKA PASFICA
#19104064

#Fungsi pada python menggunakan def

#Fungsi Global
def kali(a, b) : #nama fungsi : kali, parameter (a, b)
    c = a*b #nilai c didapat dari nilai pada variable a*b
    return c #nilai kembalian dari fungsi kali : c

z = kali (10,5) #memanggil fungsi kali dengan nilai a = 10, b = 5
print(z) #cetak nilai z

#Fungsi Globals
def cetakBonus(daftar=[]) : #nama fungsi : cetakBonus, parameter : daftar (tipe data array)
    #Fungsi Lokal
    def hitungBonus(gaji) : #nama fungsi : hitungBonus, parameter : gaji
        if gaji < 5000000 :
            bonus = 0.05 * gaji
        elif 5000000 <= gaji < 7500000 : #penggunaan else if
            bonus = 0.10 * gaji
        else :
            bonus = 0.10 * gaji
        return bonus #return dari fungsi lokal

    #Diluar fungsi lokal (masih di dalam fungsi Global)
    for nama, gaji in daftar : #melakukan perulangan untuk nama dan gaji sebanyak jumlah daftar
        b = hitungBonus(gaji) #nilai dari variable b adalah
        print(f'{nama}\t: {gaji}, {b}')
        

data = [
    ('ucok', 4000000),
    ('budi', 6000000),
    ('wagi', 8000000),
] #variable data memiliki tipe data array

cetakBonus(data) #Memanggil fungsi cetakBonus dengan nilai parameter dari variable data

#Fungsi Lambda mencari nilai maksimum
maks = lambda a, b : a if a > b else b
print(maks (25, 20)) 

#Fungsi Lambda menentukan nilai sama atau tidak
same = lambda a : True if a == 25 else False
print(same (20))
