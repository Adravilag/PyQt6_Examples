# styled_delegate_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView, QStyledItemDelegate, QFormLayout, QLineEdit, QSpinBox, QLabel
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt6.QtCore import Qt

class BoldDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        painter.save()
        # Si estamos en la primera columna, usar fuente en negrita
        if index.column() == 0:
            font = option.font
            font.setBold(True)
            painter.setFont(font)
        painter.drawText(option.rect, Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, index.data())
        painter.restore()

class IntermediateDelegateExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QStyledItemDelegate Example")
        self.resize(400, 300)
        layout = QVBoxLayout(self)
        
        self.label = QLabel("Double-click a cell to edit it", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.table_view = QTableView(self)
        layout.addWidget(self.table_view)
        
        # Crear el modelo con 4 filas y 2 columnas
        self.model = QStandardItemModel(4, 2, self)
        self.model.setHorizontalHeaderLabels(["Name", "Value"])
        data = [
            ("Alpha", "100"),
            ("Beta", "200"),
            ("Gamma", "300"),
            ("Delta", "400")
        ]
        for row, (name, value) in enumerate(data):
            item1 = QStandardItem(name)
            item2 = QStandardItem(value)
            item1.setEditable(True)
            item2.setEditable(True)
            self.model.setItem(row, 0, item1)
            self.model.setItem(row, 1, item2)
        self.table_view.setModel(self.model)
        
        delegate = BoldDelegate()
        self.table_view.setItemDelegate(delegate)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateDelegateExample()
    window.show()
    sys.exit(app.exec())
