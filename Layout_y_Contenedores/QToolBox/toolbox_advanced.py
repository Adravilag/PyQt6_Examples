# toolbox_advanced.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QToolBox, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QMessageBox
)
from PyQt6.QtCore import Qt

class AdvancedToolBoxExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QToolBox Example")
        self.resize(500, 400)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Crear QToolBox
        self.toolbox = QToolBox(self)
        main_layout.addWidget(self.toolbox)
        
        # Panel de control para agregar/eliminar páginas
        control_layout = QHBoxLayout()
        add_button = QPushButton("Add Page", self)
        remove_button = QPushButton("Remove Current Page", self)
        control_layout.addWidget(add_button)
        control_layout.addWidget(remove_button)
        main_layout.addLayout(control_layout)
        
        add_button.clicked.connect(self.add_page)
        remove_button.clicked.connect(self.remove_current_page)
        
        # Agregar una página inicial
        self.page_counter = 1
        self.add_page()

    def add_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        label = QLabel(f"This is page {self.page_counter}", page)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.toolbox.addItem(page, f"Page {self.page_counter}")
        self.page_counter += 1

    def remove_current_page(self):
        index = self.toolbox.currentIndex()
        if index != -1:
            self.toolbox.removeItem(index)
        else:
            QMessageBox.information(self, "Information", "No page to remove.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedToolBoxExample()
    window.show()
    sys.exit(app.exec())
