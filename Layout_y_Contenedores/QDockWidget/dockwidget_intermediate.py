# dockwidget_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QDockWidget, QTextEdit, QLabel
from PyQt6.QtCore import Qt

class IntermediateDockWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QDockWidget Example")
        self.resize(800, 600)
        
        # Widget central
        self.text_edit = QTextEdit("Central Widget: Main Content")
        self.setCentralWidget(self.text_edit)
        
        # Primer dock: Lista de navegación
        self.nav_dock = QDockWidget("Navigation", self)
        self.nav_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        self.nav_list = QListWidget()
        self.nav_list.addItems(["Home", "Profile", "Settings", "About"])
        self.nav_dock.setWidget(self.nav_list)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.nav_dock)
        
        # Segundo dock: Información adicional
        self.info_dock = QDockWidget("Information", self)
        self.info_dock.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea | Qt.DockWidgetArea.TopDockWidgetArea)
        self.info_label = QLabel("Additional Information Displayed Here")
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.info_dock.setWidget(self.info_label)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.info_dock)
        
        # Permitir que los docks sean flotables y cerrables
        self.nav_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable |
                                  QDockWidget.DockWidgetFeature.DockWidgetFloatable |
                                  QDockWidget.DockWidgetFeature.DockWidgetClosable)
        self.info_dock.setFeatures(QDockWidget.DockWidgetFeature.DockWidgetMovable |
                                   QDockWidget.DockWidgetFeature.DockWidgetFloatable |
                                   QDockWidget.DockWidgetFeature.DockWidgetClosable)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateDockWidget()
    window.show()
    sys.exit(app.exec())
