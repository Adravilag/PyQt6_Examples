# dockwidget_advanced.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class AdvancedDockWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QDockWidget Example")
        self.resize(900, 600)
        
        # Widget central
        self.text_edit = QTextEdit("Main Content Area")
        self.setCentralWidget(self.text_edit)
        
        # Crear menú para gestionar dock widgets
        self.menu = self.menuBar().addMenu("Docks")
        
        # Acción para agregar un dock de navegación
        self.add_nav_action = QAction("Add Navigation Dock", self)
        self.add_nav_action.triggered.connect(self.add_navigation_dock)
        self.menu.addAction(self.add_nav_action)
        
        # Acción para agregar un dock de información
        self.add_info_action = QAction("Add Info Dock", self)
        self.add_info_action.triggered.connect(self.add_info_dock)
        self.menu.addAction(self.add_info_action)
        
        # Almacenar los docks creados
        self.docks = []

    def add_navigation_dock(self):
        dock = QDockWidget("Navigation", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        nav_list = QListWidget()
        nav_list.addItems(["Dashboard", "Users", "Reports", "Settings"])
        dock.setWidget(nav_list)
        dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetMovable |
            QDockWidget.DockWidgetFeature.DockWidgetFloatable |
            QDockWidget.DockWidgetFeature.DockWidgetClosable
        )
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)
        self.docks.append(dock)

    def add_info_dock(self):
        dock = QDockWidget("Information", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.TopDockWidgetArea | Qt.DockWidgetArea.BottomDockWidgetArea)
        info_list = QListWidget()
        info_list.addItems(["Info A", "Info B", "Info C"])
        dock.setWidget(info_list)
        dock.setFeatures(
            QDockWidget.DockWidgetFeature.DockWidgetMovable |
            QDockWidget.DockWidgetFeature.DockWidgetFloatable |
            QDockWidget.DockWidgetFeature.DockWidgetClosable
        )
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, dock)
        self.docks.append(dock)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedDockWidget()
    window.show()
    sys.exit(app.exec())
