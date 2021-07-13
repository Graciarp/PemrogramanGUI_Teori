# GRACIA RIZKA PASFICA
# 19104064
# SE03A

# Import library SQL pada python
from PyQt5.QtSql import *

# function untuk mengkoneksikan database
def connectdb():
    # jenis database yang ditamabahkan (SQL LITE)
    db = QSqlDatabase.addDatabase('QSQLITE')
    # nama database yang ditamabahkan
    db.setDatabaseName('tesdb')
    if db.open():
        # jika database berhasil dibuka
        print('koneksi telah dibuat')
    else:
        # jika database tidak bisa dibuka
        # lastError().text untuk menampilkan pesan error pada database
        print('EROR: '+db.lastError().text())

# Function utama untuk menguji hasil program
if __name__ == '__main__':
    # memanggil function connectdb()
    connectdb()