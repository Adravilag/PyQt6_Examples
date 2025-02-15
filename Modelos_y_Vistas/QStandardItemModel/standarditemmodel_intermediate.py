# standarditemmodel_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QLabel
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt

class IntermediateStandardItemModelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QStandardItemModel Example")
        self.resize(300, 250)
        
        layout = QVBoxLayout(self)
        self.info_label = QLabel("Double-click an item to edit it", self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)
        
        self.list_view = QListView(self)
        layout.addWidget(self.list_view)
        
        # Crear el modelo editable
        self.model = QStandardItemModel(self)
        items = ["Red", "Green", "Blue", "Yellow", "Purple"]
        for item in items:
            standard_item = QStandardItem(item)
            standard_item.setEditable(True)
            self.model.appendRow(standard_item)
        
        self.list_view.setModel(self.model)
        self.list_view.setEditTriggers(QListView.EditTrigger.DoubleClicked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateStandardItemModelExample()
    window.show()
    sys.exit(app.exec())
