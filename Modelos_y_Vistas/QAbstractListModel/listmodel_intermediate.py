# listmodel_intermediate.py
import sys
from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QLabel

# Definir un rol personalizado para el color
ColorRole = Qt.ItemDataRole.UserRole + 1

class FruitListModel(QAbstractListModel):
    def __init__(self, fruits=None):
        super().__init__()
        # Cada fruta es un diccionario con 'name' y 'color'
        self._fruits = fruits or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._fruits)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return QVariant()
        fruit = self._fruits[index.row()]
        if role == Qt.ItemDataRole.DisplayRole:
            return fruit["name"]
        elif role == ColorRole:
            return fruit["color"]
        return QVariant()

    def roleNames(self):
        roles = super().roleNames()
        roles[ColorRole] = b"color"
        return roles

class IntermediateListModelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QAbstractListModel Example")
        self.resize(300, 250)

        layout = QVBoxLayout(self)
        self.list_view = QListView(self)
        layout.addWidget(self.list_view)
        
        self.info_label = QLabel("Select an item to see its color", self)
        layout.addWidget(self.info_label)

        fruits = [
            {"name": "Apple", "color": "Red"},
            {"name": "Banana", "color": "Yellow"},
            {"name": "Cherry", "color": "Dark Red"},
            {"name": "Date", "color": "Brown"},
            {"name": "Fig", "color": "Purple"},
            {"name": "Grape", "color": "Green"},
            {"name": "Kiwi", "color": "Brown"}
        ]
        self.model = FruitListModel(fruits)
        self.list_view.setModel(self.model)

        # Conectar la señal de selección para mostrar el color del elemento seleccionado
        self.list_view.clicked.connect(self.show_color)

    def show_color(self, index):
        # Obtener el color usando el rol personalizado
        color = self.model.data(index, ColorRole)
        self.info_label.setText(f"Color: {color}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateListModelExample()
    window.show()
    sys.exit(app.exec())
