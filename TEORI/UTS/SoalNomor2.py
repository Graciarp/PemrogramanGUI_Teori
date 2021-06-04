
from PyQt5.QtWidgets import *

app = QApplication([])

button = QPushButton('Click')

def on_button_clicked():

    alert = QMessageBox()

    alert.setText('You clicked the button!')

    alert.exec_()

 

button.clicked.connect(on_button_clicked)

button.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    Frame.show()
    sys.exit(app.exec_());
