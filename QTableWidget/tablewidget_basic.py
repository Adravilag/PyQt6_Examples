# tablewidget_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class BasicTableWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QTableWidget Example")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        
        # Crear QTableWidget con 4 filas y 3 columnas
        self.table = QTableWidget(4, 3, self)
        self.table.setHorizontalHeaderLabels(["Nombre", "Edad", "País"])
        layout.addWidget(self.table)
        
        # Rellenar la tabla con datos estáticos
        data = [
            ("Alice", "30", "USA"),
            ("Bob", "25", "UK"),
            ("Charlie", "35", "Canada"),
            ("Diana", "28", "Australia")
        ]
        
        for row, (name, age, country) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(age))
            self.table.setItem(row, 2, QTableWidgetItem(country))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicTableWidgetExample()
    window.show()
    sys.exit(app.exec())
