import sys
from PyQt6.QtWidgets import (
QMainWindow, QApplication,QPushButton,
QLabel, QLineEdit, QWidget,QVBoxLayout
)
from PyQt6.QtCore import Qt,QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.setWindowTitle('Простой калькулятор')
        self.line = QLineEdit()
        self.line.setMaxLength(100)
        self.line.setPlaceholderText('Введите данные и нажмите "result"')

        self.setCentralWidget(self.line)


        self.button = QPushButton("result")
        self.setFixedSize(QSize(400, 100))
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.label = QLabel('Здесь будет результат')
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)

        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        layout = QVBoxLayout()
        widgets = [self.line, self.button,self.label]
        for w in widgets:
            layout.addWidget(w)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        res = 0
    #
    def the_button_was_clicked(self):
        print(self.line.text(), '= ',end='')

        try:
            if '+' in self.line.text():
                lst = self.line.text().split('+')
                res = float(lst[0]) + float(lst[1])
                self.label.setText(f"{round(res, 2)}")

            elif '-' in self.line.text():
                lst = self.line.text().split('-')
                res = float(lst[0]) - float(lst[1])
                self.label.setText(f"{round(res, 2)}")

            elif '/' in self.line.text():
                lst = self.line.text().split('/')
                res = float(lst[0]) / float(lst[1])
                self.label.setText(f"{round(res, 2)}")
            elif '*' in self.line.text():
                lst = self.line.text().split('*')
                res = float(lst[0]) * float(lst[1])
                self.label.setText(f"{round(res,2)}")
        except:
            res = 'Ошибка ввода'
            self.label.setText(f"{res}")
        print(res)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()