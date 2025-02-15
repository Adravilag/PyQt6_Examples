# tablewidget_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLabel, QHBoxLayout

class IntermediateTableWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QTableWidget Example")
        self.resize(500, 350)
        
        main_layout = QVBoxLayout(self)
        
        # Crear QTableWidget con 3 filas y 3 columnas
        self.table = QTableWidget(3, 3, self)
        self.table.setHorizontalHeaderLabels(["Producto", "Cantidad", "Precio"])
        main_layout.addWidget(self.table)
        
        # Rellenar la tabla con datos editables
        data = [
            ("Manzanas", "10", "$1.50"),
            ("Naranjas", "20", "$2.00"),
            ("Plátanos", "15", "$1.20")
        ]
        for row, (product, quantity, price) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(product))
            self.table.setItem(row, 1, QTableWidgetItem(quantity))
            self.table.setItem(row, 2, QTableWidgetItem(price))
        
        # Botón para mostrar el contenido de la tabla
        self.show_button = QPushButton("Mostrar Contenido", self)
        self.show_button.clicked.connect(self.show_table_content)
        
        # Etiqueta para mostrar resultados
        self.result_label = QLabel("", self)
        main_layout.addWidget(self.show_button)
        main_layout.addWidget(self.result_label)
        
    def show_table_content(self):
        content = ""
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            content += " | ".join(row_data) + "\n"
        self.result_label.setText(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateTableWidgetExample()
    window.show()
    sys.exit(app.exec())
