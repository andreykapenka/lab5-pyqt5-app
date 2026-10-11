from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from table_window import TableWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)
        self.table_window = None
        self.open_table_button.clicked.connect(self.open_table)

    def open_table(self):
        self.table_window = TableWindow()
        self.table_window.show()