# tablewidget_advanced.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QMessageBox
)

class AdvancedTableWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QTableWidget Example")
        self.resize(600, 400)
        
        main_layout = QVBoxLayout(self)
        
        # Crear QTableWidget con 3 columnas y sin filas iniciales
        self.table = QTableWidget(0, 3, self)
        self.table.setHorizontalHeaderLabels(["Nombre", "Cantidad", "Precio"])
        main_layout.addWidget(self.table)
        
        # Panel de control para agregar y eliminar filas
        control_layout = QHBoxLayout()
        self.add_button = QPushButton("Agregar Fila", self)
        self.remove_button = QPushButton("Eliminar Fila Seleccionada", self)
        control_layout.addWidget(self.add_button)
        control_layout.addWidget(self.remove_button)
        main_layout.addLayout(control_layout)
        
        self.add_button.clicked.connect(self.add_row)
        self.remove_button.clicked.connect(self.remove_row)
        
    def add_row(self):
        # Insertar una nueva fila al final
        row = self.table.rowCount()
        self.table.insertRow(row)
        # Opcional: establecer datos iniciales en la nueva fila
        self.table.setItem(row, 0, QTableWidgetItem("Nuevo Producto"))
        self.table.setItem(row, 1, QTableWidgetItem("0"))
        self.table.setItem(row, 2, QTableWidgetItem("$0.00"))
        
    def remove_row(self):
        # Eliminar la fila seleccionada
        selected_indexes = self.table.selectedIndexes()
        if selected_indexes:
            row = selected_indexes[0].row()
            self.table.removeRow(row)
        else:
            QMessageBox.information(self, "Información", "No se ha seleccionado ninguna fila.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedTableWidgetExample()
    window.show()
    sys.exit(app.exec())
