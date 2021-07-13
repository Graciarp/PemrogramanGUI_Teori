# GRACIA RIZKA PASFICA
# 19104064
# SE03A

# Memanggil beberapa fungsi tertentu pada modul QtWidgets
from PyQt5.QtWidgets import (
    QDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
)

class EntryForm(QDialog):
    # function untuk mengaktifkan class EntryForm
    def __init__(self):
        super().__init__()
        self.setupUi()
    # Function untuk membuat tampilan dari class EntryForm
    def setupui(self):
        self.resize(300, 100) # mengatur ukuran tampilan
        self.move(320, 280) # mengatur tata letak tampilan
        self.setWindowTitle('Tambah/Ubah Kontak') # menambahkan judul pada tampilan
        self.mode = -1 # 0 untuk mode tambah, 1 untuk mode ubah
        self.okButton = QPushButton('Ok')
        self.cancelButton = QPushButton('Batal')
        hbox = QHBoxLayout() # menambahkan hbox layout
        hbox.addWidget(self.okButton) # button 'ok' ditambahkan ke dalam hbox layout
        hbox.addWidget(self.cancelButton) # button 'Batal' ditambahkan ke dalam hbox layout
        self.label1 = QLabel("Nama Lengkap: ") # menambahkan label dengan nama "Nama Lengkap: "
        self.nameLineEdit = QLineEdit() # menambahkan line edit
        self.label2 = QLabel("Nomor HP: ") # Menambahkan label dengan nama "Nomor HP: "
        self.phoneLineEdit = QLineEdit() # menambahkan line edit berformat phone
        # jika mode == 0
        if self.mode == 0:
            self.nameLineEdit.clear()
            self.phoneLineEdit.clear()
        layout = QGridLayout() # menambahkan layout grid
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.nameLineEdit, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.phoneLineEdit, 1, 1)
        layout.addLayout(hbox, 2, 1)
        self.setLayout(layout)
        # mengoneksikan button ok dengan function accept
        self.okButton.clicked.connect(self.accept)
        # mengoneksikan button cancel dengan function reject
        self.cancelButton.clicked.connect(self.reject)