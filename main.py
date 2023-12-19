import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from PyQt5.uic import loadUi
import sqlite3

class CoffeeApp(QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        loadUi('main.ui', self)

        self.initUI()
        self.show()

    def initUI(self):
        self.load_data()

    def load_data(self):
        connection = sqlite3.connect('coffee.db')
        cursor = connection.cursor()

        # Пример SQL-запроса. Замените его на необходимый запрос для вашей базы данных.
        query = "SELECT * FROM coffee"
        cursor.execute(query)
        data = cursor.fetchall()

        connection.close()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(i, j, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeApp()
    sys.exit(app.exec_())
