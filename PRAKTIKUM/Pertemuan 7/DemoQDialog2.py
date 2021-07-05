import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DialogForm(QDialog): # Class yang digunakan untuk membuat tampilan Dialog
    def __init__(self): 
        super().__init__()
        self.setupUi()
    def setupUi(self): # Function untuk tampilan DialogForm
        self.resize(300,100) # Mengatur ukuran tampilan dengan format x dan y
        self.move(320, 280) # Mengatur tata letak tampilan dengan format x dan y
        self.setWindowTitle('Dialog') # Mengatur judul tampilan dengan nama 'Dialog'
        self.label = QLabel('') # Membuat label baru tanpa isi
        self.closeButton = QPushButton('Tutup') # Membuat button dengan nama 'Tutup'
        hbox = QHBoxLayout() # Membuat layout jenis hBox
        hbox.addStrextch() 
        hbox.addWidget(self.closeButton)
        layout = QVBoxLayout() # Membuat layout
        layout.addWidget(self.label) 
        layout.addLayout(hbox) 
        self.setLayout(layout) 
        self.closeButton.clicked.connect(self.close)
        # Jika Button close di klik maka akan menuju ke close function
        
class MainForm(QWidget): # Class Main Form
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self): # function untuk tampilan MainForm
        self.resize(350, 100) # Mengatur ukuran tampilan MainForm
        self.move(300,300) # Mengatur tata letak tampilan MainForm
        self.setWindowTitle('Demo QDialog.setModal()') # Membuat judul pada tampilan
        self.label = QLabel('Tuliskan teks pada kotak di bawah ketika dialog ditampilkan')
        # Menambahkan label dengan tulisan sesuai teks diatas
        self.lineEdit = QLineEdit() # Membuat Line Edit
        self.showModalDialogButton = QPushButton('Modal') # Membuat Push Button
        self.showModelessDialogButton = QPushButton('Non-Modal') # Membuat Push Button
        hbox = QHBoxLayout()# Membuat layout menggunakan hBox
        hbox.addWidget(self.showModalDialogButton)
        # Menambahkan widget yang dapat menampilkan function showModalDialogButton
        hbox.addWidget(self.showModelessDialogButton)
        # Menambahkan widget yang dapat menampilkan function showModelessDialogButton
        layout = QVBoxLayout()
        # Membuat layout dengan QVBoxLayout
        layout.addWidget(self.label) # Menambahkan widget dari function label
        layout.addWidget(self.lineEdit) # Menambahkan widget dari function lineEdit
        layout.addLayoute(hbox) # Menambahkan layout hbox
        self.setLayout(layout) # Memanggil function layout
        
    self.showModalDialogButton.clicked.connect(self.showModalDialogButtonClick)
    # Jika button showModalDialog di klik maka akan menuju ke function showModalDialogButtonClick
    self.showModelessDialogButton.clicked.connect(self.showModelessDialogButtonClick)
    # Jika button showModelessDialogButton di klik maka akan menuju ke function showModelessDialogButtonClick

    def showModalDialogButtonClick(self): # Function showModalDialogButtonClick
        self.form = DialogForm() # Memanggil class DialogForm
        self.form.label.setText('Dialog Bersifat modal')
        # Label pada DialogForm yang semula kosong akan diisi dengan 'Dialog bersifat modal')
        self.form.setModal(True)
        self.form.show() # Menampilkan form 

    def showModelessDialogButtonClick(Self):
        self.form = DialogForm()
        self.form.label.setText('Dialog bersifat non-modal(modeless)')
        self.form.setModal(False)
        self.form.show()

if __name__ == '__main__': # Function utama untuk menjalankan DemoDialog2.py
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
        
        
