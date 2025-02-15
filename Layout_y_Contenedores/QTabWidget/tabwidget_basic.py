# tabwidget_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout, QLabel

class BasicTabWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QTabWidget Example")
        self.resize(600, 400)
        
        # Crear el QTabWidget
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        # Pestaña 1: Contenido estático
        tab1 = QWidget()
        layout1 = QVBoxLayout(tab1)
        layout1.addWidget(QLabel("Contenido de la Pestaña 1"))
        self.tab_widget.addTab(tab1, "Pestaña 1")
        
        # Pestaña 2: Contenido estático
        tab2 = QWidget()
        layout2 = QVBoxLayout(tab2)
        layout2.addWidget(QLabel("Contenido de la Pestaña 2"))
        self.tab_widget.addTab(tab2, "Pestaña 2")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicTabWidget()
    window.show()
    sys.exit(app.exec())
