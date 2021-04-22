#GRACIA RIZKA PASFICA
#19104064

# Try..except..
try :
  a = int(input('masukkan nilai a: ')) #Perintah input digunakan untuk menginput nilai
  b = int(input('masukkan nilai b: '))
  c = a / b
  print(f"{a} / {b} = {c}")

except ZeroDivisionError as e :
  print('Error : Tidak boleh bagi 0')

# Try..except..finally
f = ''

try : 
  f = open('contoh.txt', 'r') #Mencoba untuk membuka file contoh.txt
  lines = f.readlines()
  for line in lines : 
    print(line, end='\n')

except IOError as e : #Dijalankan jika file yang dibuka pada bagian try tidak ditemukan
  print('Error : File Hilang')

finally :
  if f :
    f.close()
