import sys
from praktikum5_ui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

class DemoQtDesainer(QDialog):
     def __init__(self,parent = None):
         QDialog. __init__(self,parent)
         self.ui = Ui_Form()
         self.ui.setupUi(self)
         self.ui.Halo.clicked.connect(self.HaloClicked)

     def HaloClicked(self):
         QMessageBox.information(self, 'Demo Qt Designer','Hallo %s, apa kabar?' % self.ui.namaEdit.text())

     if __name__ == "__main__":
         a = QApplication(sys.argv)
         Form = DemoQtDesainer()
         Form.show()
         a.exec_()
