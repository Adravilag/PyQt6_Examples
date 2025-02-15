# groupbox_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QLabel, QLineEdit
from PyQt6.QtCore import Qt

class BasicGroupBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGroupBox - Básico")
        self.resize(300, 150)

        layout = QVBoxLayout(self)
        
        # Crear un QGroupBox con un título
        group_box = QGroupBox("User Info", self)
        group_layout = QVBoxLayout(group_box)
        
        # Agregar controles al QGroupBox
        label = QLabel("Name:", group_box)
        line_edit = QLineEdit(group_box)
        group_layout.addWidget(label)
        group_layout.addWidget(line_edit)
        
        layout.addWidget(group_box)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicGroupBoxExample()
    window.show()
    sys.exit(app.exec())
