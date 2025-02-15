# scrollarea_intermediate.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QScrollArea, QVBoxLayout, QPushButton, QLabel
)
from PyQt6.QtCore import Qt

class IntermediateScrollAreaExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QScrollArea Example")
        self.resize(400, 300)
        
        main_layout = QVBoxLayout(self)
        
        # Crear un contenedor para agregar múltiples widgets
        container = QWidget()
        container_layout = QVBoxLayout(container)
        
        # Agregar varios botones y etiquetas
        for i in range(1, 21):
            btn = QPushButton(f"Botón {i}", container)
            lbl = QLabel(f"Etiqueta {i}: Contenido de ejemplo", container)
            container_layout.addWidget(btn)
            container_layout.addWidget(lbl)
        
        # Crear QScrollArea y asignar el contenedor
        scroll_area = QScrollArea(self)
        scroll_area.setWidget(container)
        scroll_area.setWidgetResizable(True)
        
        main_layout.addWidget(scroll_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateScrollAreaExample()
    window.show()
    sys.exit(app.exec())
