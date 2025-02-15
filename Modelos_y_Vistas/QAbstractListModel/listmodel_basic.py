# listmodel_basic.py
import sys
from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView

class FruitListModel(QAbstractListModel):
    def __init__(self, fruits=None):
        super().__init__()
        self._fruits = fruits or []

    def rowCount(self, parent=QModelIndex()):
        return len(self._fruits)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.ItemDataRole.DisplayRole:
            return self._fruits[index.row()]
        return None

class BasicListModelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QAbstractListModel Example")
        self.resize(300, 200)

        layout = QVBoxLayout(self)

        self.list_view = QListView(self)
        layout.addWidget(self.list_view)

        # Datos de ejemplo: lista de frutas
        fruits = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi"]
        self.model = FruitListModel(fruits)
        self.list_view.setModel(self.model)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicListModelExample()
    window.show()
    sys.exit(app.exec())
