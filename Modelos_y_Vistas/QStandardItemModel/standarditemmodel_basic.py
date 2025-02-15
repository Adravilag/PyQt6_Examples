# standarditemmodel_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class BasicStandardItemModelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QStandardItemModel Example")
        self.resize(300, 200)
        
        layout = QVBoxLayout(self)
        self.list_view = QListView(self)
        layout.addWidget(self.list_view)
        
        # Crear el modelo y poblarlo con algunos datos
        self.model = QStandardItemModel(self)
        items = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi"]
        for item in items:
            standard_item = QStandardItem(item)
            self.model.appendRow(standard_item)
        
        # Asignar el modelo al QListView
        self.list_view.setModel(self.model)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicStandardItemModelExample()
    window.show()
    sys.exit(app.exec())
