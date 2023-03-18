from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt

n = int(input('Enter modulo value: '))
if n > 1:
    for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
            print(n, "is not a prime number")
            break
        else:
            elements = {x for x in range(n)}


            def generate_addition_table_Zn(z):
                table = [[(i * j) % z for j in elements] for i in elements]
                return table


            class AdditionTableGUI(QWidget):
                def __init__(self, z):
                    super().__init__()
                    self.n = z
                    self.table = generate_addition_table_Zn(z)
                    self.setWindowTitle(f"Multiplication Table for \u2124_{z}")
                    self.setGeometry(100, 100, 800, 800)
                    # Create a table widget and set its properties
                    self.tableWidget = QTableWidget(self)
                    self.tableWidget.setRowCount(z)
                    self.tableWidget.setColumnCount(z)
                    self.tableWidget.setHorizontalHeaderLabels([str(i) for i in range(z)])
                    self.tableWidget.setVerticalHeaderLabels([str(i) for i in range(z)])
                    self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                    self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
                    self.tableWidget.setMinimumSize(800, 800)
                    # Populate the table widget with the addition table
                    for i in range(z):
                        for j in range(z):
                            item = QTableWidgetItem(str(self.table[i][j]))
                            item.setTextAlignment(Qt.AlignCenter)
                            self.tableWidget.setItem(i, j, item)
                    self.show()
            app = QApplication([])
            gui = AdditionTableGUI(n)
            app.exec_()
