from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton
from PyQt6.QtCore import QSize,Qt
import sys
class MainWindow(QMainWindow):
    k = 0
    def __init__(self):
        super().__init__()
        self.button_is_checked = True
        self.setWindowTitle("Счётчик нажатий")
        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.status = 'Press me!'
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setFixedSize(QSize(400,100))
        self.button.setChecked(self.button_is_checked)
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        if self.status == 'Press me!':
            MainWindow.k += 1
            print(f"Cliked {MainWindow.k} times!")
            self.button.setText(f"{MainWindow.k}")
            self.status = 'Other'
        else:
            MainWindow.k += 1
            print(f"Cliked {MainWindow.k} times!")
            self.button.setText(f"{MainWindow.k}")
            self.status = 'Other'

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()