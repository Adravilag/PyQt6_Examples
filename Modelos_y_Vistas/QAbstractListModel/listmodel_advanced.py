# listmodel_advanced.py
import sys
from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QPushButton, QHBoxLayout, QLineEdit

class EditableListModel(QAbstractListModel):
    def __init__(self, items=None):
        super().__init__()
        self._items = items or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._items)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return QVariant()
        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            return self._items[index.row()]
        return QVariant()

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if index.isValid() and role == Qt.ItemDataRole.EditRole:
            self._items[index.row()] = value
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.EditRole])
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable

    def addItem(self, item):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(item)
        self.endInsertRows()

    def removeItem(self, index):
        if 0 <= index < self.rowCount():
            self.beginRemoveRows(QModelIndex(), index, index)
            self._items.pop(index)
            self.endRemoveRows()
            return True
        return False

class AdvancedListModelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Editable QAbstractListModel Example")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        self.list_view = QListView(self)
        layout.addWidget(self.list_view)
        
        # Modelo editable con algunos elementos iniciales
        self.model = EditableListModel(["Item 1", "Item 2", "Item 3"])
        self.list_view.setModel(self.model)
        
        # Panel de control para agregar y eliminar elementos
        control_layout = QHBoxLayout()
        self.new_item_edit = QLineEdit(self)
        self.new_item_edit.setPlaceholderText("Nuevo ítem")
        self.add_button = QPushButton("Agregar", self)
        self.remove_button = QPushButton("Eliminar Seleccionado", self)
        control_layout.addWidget(self.new_item_edit)
        control_layout.addWidget(self.add_button)
        control_layout.addWidget(self.remove_button)
        layout.addLayout(control_layout)
        
        self.add_button.clicked.connect(self.add_item)
        self.remove_button.clicked.connect(self.remove_item)

    def add_item(self):
        text = self.new_item_edit.text().strip()
        if text:
            self.model.addItem(text)
            self.new_item_edit.clear()

    def remove_item(self):
        index = self.list_view.currentIndex()
        if index.isValid():
            self.model.removeItem(index.row())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedListModelExample()
    window.show()
    sys.exit(app.exec())
