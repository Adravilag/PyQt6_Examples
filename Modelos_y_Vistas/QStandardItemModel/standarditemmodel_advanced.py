# standarditemmodel_advanced.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QPushButton, QHBoxLayout
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt

class AdvancedStandardItemModelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QStandardItemModel Example (Drag & Drop)")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        
        # Crear QListView con soporte para drag and drop
        self.list_view = QListView(self)
        self.list_view.setDragDropMode(QListView.DragDropMode.InternalMove)
        layout.addWidget(self.list_view)
        
        # Crear el modelo editable
        self.model = QStandardItemModel(self)
        items = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]
        for item in items:
            standard_item = QStandardItem(item)
            standard_item.setEditable(True)
            self.model.appendRow(standard_item)
        self.list_view.setModel(self.model)
        
        # Botones de control: agregar y eliminar elementos
        control_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Item", self)
        self.remove_button = QPushButton("Remove Selected", self)
        control_layout.addWidget(self.add_button)
        control_layout.addWidget(self.remove_button)
        layout.addLayout(control_layout)
        
        self.add_button.clicked.connect(self.add_item)
        self.remove_button.clicked.connect(self.remove_item)
    
    def add_item(self):
        new_item = QStandardItem("New Task")
        new_item.setEditable(True)
        self.model.appendRow(new_item)
    
    def remove_item(self):
        selected_indexes = self.list_view.selectedIndexes()
        if selected_indexes:
            for index in selected_indexes:
                self.model.removeRow(index.row())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedStandardItemModelExample()
    window.show()
    sys.exit(app.exec())
