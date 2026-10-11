import csv
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import uic
from data_reader import get_data


class TableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("table_window.ui", self)

        self.read_button.clicked.connect(self.read_data)
        self.save_button.clicked.connect(self.save_data)

        self.load_csv()

    def read_data(self):
        temperature, humidity, light = get_data()

        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, self.make_item(str(temperature)))
        self.table.setItem(row, 1, self.make_item(str(humidity)))
        self.table.setItem(row, 2, self.make_item(str(light)))

    def make_item(self, text):
        from PyQt5.QtWidgets import QTableWidgetItem
        return QTableWidgetItem(text)

    def save_data(self):
        with open("data.csv", "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["Температура", "Влажность", "Освещение"])

            for row in range(self.table.rowCount()):
                values = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    values.append(item.text() if item else "")
                writer.writerow(values)

        QMessageBox.information(self, "Сохранение", "Данные сохранены в data.csv")

    def load_csv(self):
        try:
            with open("data.csv", "r", newline="", encoding="utf-8-sig") as file:
                reader = csv.reader(file)
                rows = list(reader)

            if len(rows) <= 1:
                return

            for values in rows[1:]:
                if len(values) != 3:
                    continue

                row = self.table.rowCount()
                self.table.insertRow(row)

                for column, value in enumerate(values):
                    self.table.setItem(row, column, self.make_item(value))

        except FileNotFoundError:
            pass