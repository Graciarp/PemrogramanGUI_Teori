# GRACIA RIZKA PASFICA
# 19104064
# SE03A

import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class DialogForm(QDialog): # Class dialogForm untuk tampilan
    def __init__(self):
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(300, 100)
        self.move(320, 280)
        self.setWindowTitle('Dialog') # Mengatur judul window dengan nama 'Dialog'
        self.label = QLabel('Form Kedua (Dialog)') # Judul untuk window kedua
        self.okButton = QPushButton('OK') # Push Button dengan tampilan nama 'OK'
        self.cancelButton = QPushButton('Batal') # Push Button dengan tampilan nama 'Batal'
        hbox = QHBoxLayout() # Layout
        hbox.addStretch()
        hbox.addWidget(self.okButton) 
        hbox.addWidget(self.cancelButton)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(hbox)
        self.setLayout(layout)
        self.okButton.clicked.connect(self.accept) # Jika Button Ok di klik maka akan menuju ke function acccept
        self.cancelButton.clicked.connect(self.reject) # Jika Button cancel di klik maka akan menuju ke function reject
        
class MainForm(QWidget): # Class MainForm digunakan untuk mengatur fungsi kerja layout
    def __init__(self): 
        super().__init__()
        self.setupUi()
    def setupUi(self):
        self.resize(350, 100) # Ukuran layout
        self.move(300, 300) # Tata letak
        self.setWindowTitle('Demo QDialog.accept() dan QDialog.reject()') # Judul Window
        self.label = QLabel('Form Utama') # Judul yang ada di dalam window
        self.showDialogButton = QPushButton('Tampilkan Dialog') # Judul Button
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.showDialogButton)
        self.setLayout(layout)
        self.showDialogButton.clicked.connect(self.showDialogButtonClick)
        # Jika Button "Tampilkan Dialog" di klik maka akan menuju ke function showDialogClick
    def showDialogButtonClick(self):
        form = DialogForm()
        if form.exec_() == QDialog.Accepted:
            QMessageBox.information(self, 'Informasi', 'Anda memilih tombol OK') # Menampilkan pesan tersebut jika Button Ok di klik
        else: # QDialog.Rejected
            QMessageBox.information(self, 'Informasi', 'Anda memilih tombol Batal') # Menampilkan pesan tersebut jika Button Batal di klik

# Function utama untuk di jalankan            
if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
