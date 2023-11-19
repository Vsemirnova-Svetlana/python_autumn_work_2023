import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,QDialog, QPushButton, QTextEdit,QMdiArea, QMdiSubWindow, QTextEdit,
    QLabel, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout,QSlider, QSpinBox, QComboBox, QGridLayout,QDoubleSpinBox
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    list_of_tasks = []
    str = ''
    k = 0
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Список дел')

        exitAction = QAction('Exit',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Выйти из приложения')
        exitAction.triggered.connect(self.close)


        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)

        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.setCentralWidget(self.label)

        button_action = QAction("Help", self)
        button_action.setStatusTip("Вызов помощника")
        button_action.triggered.connect(self.for_help)
        toolbar.addAction(button_action)

        button_action = QAction("Instruction", self)
        button_action.setStatusTip("Инструкция к программе")
        button_action.triggered.connect(self.for_instruction)
        toolbar.addAction(button_action)

        button_action = QAction("Description", self)
        button_action.setStatusTip("Описание программы")
        button_action.triggered.connect(self.for_description)
        toolbar.addAction(button_action)

        self.line = QLineEdit()
        self.line.setMaxLength(100)
        self.line.setPlaceholderText('Введите задачу')

        self.button = QPushButton("Add task")
        self.setFixedSize(QSize(400, 200))
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        self.button1 = QPushButton("View all tasks")
        self.setFixedSize(QSize(400, 200))
        self.button1.setCheckable(True)
        self.button1.clicked.connect(self.the_button1_was_clicked)

        # layout = QVBoxLayout()
        layout = QGridLayout()
        layout.addWidget(self.label, 1, 0)
        layout.addWidget(self.line, 0, 0)
        layout.addWidget(self.button, 0, 1)
        layout.addWidget(self.button1, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def for_help(self, s):
        print("Для выхода из программы нажмите Exit", s)
        self.label.setText('Для выхода из программы нажмите Exit либо Ctrl+Q')
    def for_instruction(self):
        self.label.setText(''' 
        Чтобы добавить новую задачу, нажмите кнопку
        "Add task". Для просмотра созданных задач 
        нажмите кнопку "View all tasks".
                           ''')

    def for_description(self):
        self.label.setText('''
        Данная программа помогает создавать
        список текущих дел и (когда-нибудь) будет 
        отправлять напоминания на почту''')

    def the_button_was_clicked(self):
        MainWindow.list_of_tasks.append(self.line.text())
        print(MainWindow.list_of_tasks)

        self.line.setPlaceholderText('Введите новую задачу.')

    def the_button1_was_clicked(self):
        for j,i in enumerate(MainWindow.list_of_tasks):
            MainWindow.str = MainWindow.str + str(j+1) + ') ' + i +'\n'
            self.label.setText(MainWindow.str)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()