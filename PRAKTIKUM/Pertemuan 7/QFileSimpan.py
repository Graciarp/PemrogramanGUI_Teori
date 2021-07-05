# GRACIA RIZKA PASFICA
# SE03A
# 19104064

import sys
# Import library
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# Class MainForm
class MainForm(QWidget):
    # Function untuk menjalankan QWidget
    def __init__(self):
        super().__init__()
        self.setupUi()
    # Function untuk mengatur tampilan dari class MainForm   
    def setupUi(self):
        self.resize(500, 450) # Mengatur ukuran tampilan
        self.move(300, 300) # Mengatur tata letak tampilan
        self.setWindowTitle('Demo QFileDialog.getSaveFileName()') # Membuat judul baru
        self.textEdit = QTextEdit() # Menambahka textEdit
        self.saveButton = QPushButton('Simpan') # Menambahkan Button dengan nama simpan
        hbox = QHBoxLayout() # Membuat layout baru menggunakan QHBox
        hbox.addWidget(self.saveButton) # Menambahkan widget dengan menampilkan saveButton
        hbox.addStretch() 
        self.fileLabel = QLabel('Nama file: ') # Menambahkan label dengan nama
        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(hbox)
        layout.addWidget(self.fileLabel)
        self.setLayout(layout)
        # Jika saveButton di klik maka akan terhubung dengan functionButtonClick
        self.saveButton.clicked.connect(self.saveButtonClick)
     # Function savebuttonClick
     def saveButtonClick(self):
        import os
        fileName = QFileDialog.getSaveFileName(self, 'Simpan file', os.curdir,
                                               'Python Code (*.py);; Ruby Code (*.rb) *.py')
        if not fileName[0]: return
        self.fileLabel.setText('Nama file: ' + fileName[0])
        fileHandle = QFile(fileName[0])
        if not fileHandle.open(QIODevice.WriteOnly): return
        stream = QTextStream(fileHandle)
        stream << self.textEdit.document().toPlainText()
        stream.flush()
        fileHandle.close

# Function Utama untuk menajalankan QFileSimpan
if __name__ == '__main__':
     a = QApplication(sys.argv)
     form = MainForm()
     form.show()
     a.exec_()
