# GRACIA RIZKA PASFICA
# SE03A
# 19104064

import sys

# Import Library
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

# Class MainForm untuk membuat UI
class MainForm(QWidget):
    # Function untuk menjalankan class MainForm
    def __init__(self): 
        super().__init__()
        self.setupUi()
    # Function untuk mengatur tampilan MainForm   
    def setupUi(self): 
        self.resize(450,100)
        self.move(300, 300)
        self.setWindowTitle('Demo QMessageBox') # Membuat judul 'Demo QMessageBox')
        self.aboutButton = QPushButton('About') # Membuat button dengan nama 'About')
        self.criticalButton = QPushButton('critical') # Membuat button dengan nama 'critical')
        self.informationButton = QPushButton('Information') # Membuat button dengan nama 'Information')
        self.questionButton = QPushButton('Question') # Membuat button dengan nama 'Question'
        self.warningButton = QPushButton('Warning') # Membuat Button dengan nama 'Warning')
        layout = QHBoxLayout() # Membuat layout menggunakan QHBoxLayout
        layout.addWidget(self.aboutButton) # Menambahkan widget dengan menampilkan aboutButton
        layout.addWidget(self.criticalButton) # Menambahkan widget dengan menampilkan criticalButton
        layout.addWidget(self.informationButton) # Menambahkan widget dengan menampilkan informationButton
        layout.addWidget(self.questionButton) # Menambahkan widget dengan menampilkan questionButton
        layout.addWidget(self.warningButton) # Menambahkan widget dengan menampilkan warningButton
    self.aboutButton.clicked.connect(self.aboutButtonClick)
    # Jika aboutButton di klik maka akan dihubungkan dengan function aboutButtonClick
    self.criticalButton.clicked.connect(self.criticalButtonClick)
    # Jika criticalButton di klik maka akan dihubungkan dengan function criticalButtonClick
    self.informationButton.clicked.connect(self.informationButtonClick)
    # Jika informationButton di klik maka akan dihubungkan dengan function informationButtonClick
    self.questionButton.clicked.connect(self.questionButtonClick)
    # Jika questionButton di klik maka akan dihubungkan dengan function questionButtonClick
    self.warningButton.clicked.connect(self.warningButtonClick)
    # Jika warningButton di klik maka akan dihubungkan dengan function warningButtonClick

    # Function abouButtonClick
    def aboutButtonClick(self):
        # Menampilkan pesan 
        QMessageBox.about(self, 'Tentang Program Video Recorder\n Versi 1.0.0\n' +
                          'Hak Cipta (c) 2016 PyQt Lover Team')

    # Function criticalButtonClick
    def criticalButtonClick(self):
        # Menampilkan pesan
        QMessageBox.critical(self, 'Kesalahan file settings.conf tidak ditemukan')

    # Function informationButtonClick
    def informationButtonClick(self):
        QMessageBox.information(self, 'Informasi Proses upload file ke server telah berhasil dilakukan')

    # Function questionBox
    def questionButtonClick(self):
        fileName = 'settings.conf'
        response = QMessageBox.question(self, 'Konfirmasi anda yakin akan menghapus file %s?' %fileName)
        # kondisi untuk menampilkan pesan
        if response == QMessaBox.Yes: # Jika kondisi terpenuhi
            QMessageBox.about(self, 'Respon anda memilih tombol yes') # Menampilkan pesan
        else : # Jika kondisi awal tidak terpenuhi
            QMessageBox.about(self, 'Respon anda memilih tombo no') # Menampilkan pesan

    # Function warningButtonClick
    def warningButtonClick(self):
        # Menampilkan pesan
        QMessageBox.warnign(self, 'Peringatan Operasi ini akan menghapus semua data di dalam disk anda!')


# Function utama untuk menjalankan DemoQMessage.py
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec


