# scrollarea_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QScrollArea, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class BasicScrollAreaExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QScrollArea Example")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        
        # Crear un QLabel con texto extenso
        long_text = "Este es un ejemplo de QScrollArea.\n" * 50
        label = QLabel(long_text, self)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        label.setWordWrap(True)
        
        # Crear el QScrollArea y asignar el QLabel como widget contenido
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(label)
        scroll_area.setWidgetResizable(True)
        
        layout.addWidget(scroll_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicScrollAreaExample()
    window.show()
    sys.exit(app.exec())
