# styled_delegate_advanced.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableView, QComboBox, QStyledItemDelegate
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt, pyqtSlot

class ComboBoxDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        combo = QComboBox(parent)
        combo.addItems(["Option 1", "Option 2", "Option 3"])
        return combo

    def setEditorData(self, editor, index):
        current_text = index.data(Qt.ItemDataRole.EditRole) or ""
        idx = editor.findText(current_text)
        if idx >= 0:
            editor.setCurrentIndex(idx)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.ItemDataRole.EditRole)

class AdvancedDelegateExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QStyledItemDelegate Example (Custom Editor)")
        self.resize(500, 300)
        
        layout = QVBoxLayout(self)
        self.table_view = QTableView(self)
        layout.addWidget(self.table_view)
        
        # Crear un modelo con dos columnas
        self.model = QStandardItemModel(4, 2, self)
        self.model.setHorizontalHeaderLabels(["Name", "Option"])
        data = [
            ("Item A", "Option 1"),
            ("Item B", "Option 2"),
            ("Item C", "Option 1"),
            ("Item D", "Option 3")
        ]
        for row, (name, option) in enumerate(data):
            item1 = QStandardItem(name)
            item2 = QStandardItem(option)
            item1.setEditable(True)
            item2.setEditable(True)
            self.model.setItem(row, 0, item1)
            self.model.setItem(row, 1, item2)
        self.table_view.setModel(self.model)
        
        # Asignar el delegado personalizado para la segunda columna
        delegate = ComboBoxDelegate()
        self.table_view.setItemDelegateForColumn(1, delegate)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedDelegateExample()
    window.show()
    sys.exit(app.exec())
