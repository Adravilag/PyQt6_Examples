# styled_delegate_basic.py
import sys
from PyQt6.QtCore import QAbstractListModel, Qt, QModelIndex
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QListView, QStyledItemDelegate, QWidget, QVBoxLayout, QStyle

class SimpleListModel(QAbstractListModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        _ = parent
        return len(self._data)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if index.isValid() and role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()]
        return None

class ColorDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        painter.save()
        # Si el item está seleccionado, usar fondo azul y texto blanco
        if option.state & QStyle.StateFlag.State_Selected:
            painter.fillRect(option.rect, QColor("blue"))
            painter.setPen(QColor("white"))
        else:
            painter.setPen(QColor("black"))
        text = index.data(Qt.ItemDataRole.DisplayRole)
        painter.drawText(option.rect, Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft, text)
        painter.restore()

class BasicDelegateExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QStyledItemDelegate Example")
        self.resize(300, 200)
        
        layout = QVBoxLayout(self)
        self.list_view = QListView(self)
        layout.addWidget(self.list_view)
        
        data = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Kiwi"]
        self.model = SimpleListModel(data)
        self.list_view.setModel(self.model)
        
        # Asignar el delegado personalizado
        delegate = ColorDelegate()
        self.list_view.setItemDelegate(delegate)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicDelegateExample()
    window.show()
    sys.exit(app.exec())
