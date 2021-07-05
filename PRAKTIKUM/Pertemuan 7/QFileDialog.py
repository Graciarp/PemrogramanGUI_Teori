# GRACIA RIZKA PASFICA
# SE03A
# 19104064

import sys

#Import library
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

# Class untuk membuat tampilan UI
class MainForm(QWidget):
    # Function untuk menjalankan class MainForm
    def __init__(self):
        super().__init__()
        self.setupUi()
    # Function untuk mengatur tampilan
    def setupUi(self):
        self.resize(500, 450) # Mengatur ukuran tampilan
        self.move(300, 300) # Mengatur tata letak tampilan
        hbox = QHBoxLayout # Membuat layout menggunakan QHBoxLayout
        hbox.addWidget(self.openButton)
        hbox.addStretch()
        self.fileLabel = QLabel('Nama file :')
        layout.addWidget(Self.textEdit) # Menampilkan widget dengan menampilkan textEdit
        layout.addLayout(hbox) # Membuat layout menggunakan hbox
        layout.addWidget(self.fileLabel) # Menampilkan widget dengan menampilkan fileLabel
        self.setLayout(layout)

    self.openButton.clicked.connect(self.openButtonClick)
    # Apabila openButtondi klik maka akan terhubung dengan function openButtonClick

    # Function openButtonClick
    def openButtonClick(self):
        import os
        fileName = QFileDialog.getOpenFileName(self,
                                               'Pilih File', os.curdir,
                                               'Python code (*.py);; Ruby code(*.eb)',
                                               '*.py')
        if not fileName[0]: return
        self.fileLabel.setText('Nama file: '+ fileName[0])
        # Mengatur nama file sesuai dengan file yang dipanggil
        fileHandle = QFile(fileName[0])
        if not fileHandle.open(QIDevice.ReadOnly): return
        stream = QTextStream(fileHandle)
        self.textEdit.setPlainText(stream.readAll())
        fileHandle.close()

if __name__ == '__main__':
    a = QApplication(sys.argv)
    form = MainForm()
    form.show()
    a.exec_()
        
        
