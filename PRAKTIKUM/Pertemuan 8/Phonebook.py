# GRACIA RIZKA PASFICA
# SE03A
# 19104064

import sys # modul yang berisi fungsi yang berkaitan dengan interpreter python dan lingkungannya
from PyQt5.QtWidgets import * # modul yang berisi kelas dasar untuk semua elemen GUI
from PyQt5.QtSql import * # modul yang berisi serangkaian fungsi database
from EntryForm import * # menghubungkan Phonebook.py dengan EntryForm.py
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# class untuk membuat tampilan
class MainForm(QWidget):
    # Function untuk menjalankan class main form
    def __init__(self):
        super().__init__() # function ini dijadikan sebagai function utama pada class MainForm
        self.setupUi() # function yang akan dijalankan
        self.loadData()

    # Function untuk membuat tampilan GUI
    def setupui(self):
        self.resize(350, 300) # mengatur ukuran tampilan
        self.move(300, 300) # mengatur tata letak tampilan
        self.setWindowTitle('Phonebook Manager') # membuat judul tampilan
        self.table = QTableView() # menambahkan tabel pada tampilan
        self.addButton = QPushButton('Tambah') # Menambahkan button 'Tambah'
        self.editButton = QPushButton('Ubah') # Menambahkan button 'Edit'
        self.deleteButton = QPushButton('Delete') # Menambahkan button 'Hapus'
        hbox = QHBoxLayout() # Menambahkan HBox Layout
        hbox.addWidget(self.addButton) # menambahkan button 'Tambah' ke dalam Box Layout
        hbox.addWidget(self.editButton) # menambahkan button 'Edit' ke dalam Box Layout
        hbox.addWidget(self.deleteButton) # menambahkan button 'Hapus' ke dalam Box Layout
        hbox.addStretch()
        layout = QVBoxLayout() # Menambahkan VBox Layout
        layout.addWidget(self.table) # menambahkan table ke dalam VBox Layout
        layout.addLayout(hbox) # Menambahkan hbox layout ke dalam vbox layout
        self.setLayout(layout)

        # mengkoneksikan button 'Tambah' dengan function addButtonClick
        self.addButton.clicked.connect(self.addButtonClick)
        # mengkoneksikan button 'Edit' dengan function editButtonClick
        self.editButton.clicked.connect(self.editButtonClick)
        # mengkoneksikan button 'Hapus' dengan function deleteButtonClick
        self.deleteButton.clicked.connect(self.deleteButton)

    # Function untuk loadData ke database
    def loadData(self):
        self.table.clear()
        self.table.setRowCount(self.getRowCount()) # Menambahkan baris berdasarkan isi pada tabel
        self.table.setColumnCount(3) # Menambahkan 3 kolom ke dalam tabel
        # Memberi nilai di kolom paling atas pada tabel
        columnHeaders = {'ID',
                         'Nama',
                         'No. HP'}
        # nilai pada columnHeaders diisikan secara horizontal
        self.table.setHorizontalHeaderLabels(columnHeaders)
        query = QSqlQuery() # menghubungkan Phonebook.py dengan SQL
        ID, NAMA, NOHP = range(3)
        row = 0 # inisiasi awal baris
        query.exec_('SELECT * FROM phonebook') # menampilkan data dari tabel phonebook
        # jika query sebelumnya berhasil maka terjadi looping
        while query.next():
            for i in range(3): # perulangan sebanyak 3 kolom
                item = QTableWidgetItem()
                item.setText(str(query.value(i))) # menambahkan nilai per kolom sesuai pada database
                self.table.setItem(row, i, item)
            row += 1 # perulangan dilakukan secara increment
        item = QTableWidgetItem()
        item.setText(str(self.getRowCount()))
        self.table.setItem(6, 0, item)

    # Function untuk menambahkan baris sesuai database
    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM phonebook') # Menampilkan seluruh data di tabel phonebook
        query.next()
        rowCount = query.value(0) # digunakan untuk menentukan jml baris pada tabel
        return rowCount

    # Function untuk button 'Tambah'
    def addButtonClick(self):
        self.entryForm = EntryForm()
        self.mode = 0
        # Jika class entryForm dapat dijalankan
        if self.entryForm.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1 # kolom id menambahkan 1 baris
            query = QSqlQuery()
            # Menambahkan 2 baris baru yang datanya sesuai dengan data id
            query.exec_("INSERT INTO phonebook VALUES (%d, '%s', '%s')" %
                        (id,self.entryForm.nameLineEdit.text(),
                           self.entryForm.phoneLineEdit.text()))
            self.loadData() # memanggil function loadData

    # Function untuk button 'Edit'
    def editButtonClick(self):
        self.entryForm = EntryForm()
        self.mode = 1
        # Pilih data pada tabel yang akan di edit
        self.entryForm.nameLineEdit.setText(
            self.table.item(self.tabel.currentRow(),1).text()
        )
        # Tentukan data baru pada tabel yang akan di edit
        self.entryForm.phoneLineEdit.setText(
            self.table.item(self.table.currentRow(),2).text()
        )
        # Jika data lama dan data baru berhasil di tambahkan
        if self.entryForm.exec_() == QDialog.Accepted:
            id = int(self.table.item(self.table.currentRow(),0).text())
            query = QSqlQuery()
            # Update data lama ke data baru
            query.exec_('''UPDATE phonebook SET nama = '%s', nohp = '%s' WHERE id = %d'''
                        % (self.entryForm.nameLineEdit.text(),
                           self.entryForm.phoneLineEdit.text(), id))
            self.loadData() # memanggil function loadData

    # Function untuk button 'Hapus'
    def deleteButtonClick(self):
        id = int(self.table.item(self.table.currentRow(),0).text())
        query = QSqlQuery()
        query.exec_('DELETE FROM phonebook WHERE id = %d' % id) # menghapus data sesuai id yang dipilih
        self.loadData() # memanggil function loadData

# function utama untuk menjalankan Phonebook.py
if __name__ == '__main__':
    a = QApplication(sys.argv)
    # koneksi database
    db = QSqlDatabase.addDatabase('QSQLITE') # jenis db yang dipakai berupa SQL LITE
    db.setDatabaseName('testdb') # nama database
    # jika koneksi gagal
    if not db.open():
        print('ERROR: '+db.lastError().text())
        sys.exit(1)
    form = MainForm() # class yang akan dijalankan
    form.show() # Menampilkan class yang akan di jalankan
    a.exec_()