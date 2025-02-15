# dockwidget_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QDockWidget, QTextEdit
from PyQt6.QtCore import Qt

class BasicDockWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QDockWidget Example")
        self.resize(600, 400)
        
        # Widget central: un editor de texto
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # Crear un QDockWidget
        self.dock = QDockWidget("Navigation", self)
        self.dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        
        # Contenido del dock: una lista
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Item 1", "Item 2", "Item 3", "Item 4"])
        self.dock.setWidget(self.list_widget)
        
        # Anclar el dock a la ventana principal
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dock)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicDockWidget()
    window.show()
    sys.exit(app.exec())
