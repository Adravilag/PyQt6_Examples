# scrollarea_advanced.py
import sys, random, time
from PyQt6.QtWidgets import (
    QApplication, QWidget, QScrollArea, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
)
from PyQt6.QtCore import Qt, QTimer

class AdvancedScrollAreaExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QScrollArea Example")
        self.resize(500, 400)
        
        main_layout = QVBoxLayout(self)
        
        # Botón para agregar elementos dinámicamente
        control_layout = QHBoxLayout()
        self.add_button = QPushButton("Agregar Elemento", self)
        self.add_button.clicked.connect(self.add_item)
        control_layout.addWidget(self.add_button)
        main_layout.addLayout(control_layout)
        
        # Crear un contenedor interno para los elementos
        self.container = QWidget(self)
        self.container_layout = QVBoxLayout(self.container)
        self.container.setLayout(self.container_layout)
        
        # Crear el QScrollArea y asignar el contenedor
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidget(self.container)
        self.scroll_area.setWidgetResizable(True)
        main_layout.addWidget(self.scroll_area)
        
        self.item_counter = 0

    def add_item(self):
        self.item_counter += 1
        label = QLabel(f"Elemento {self.item_counter}: Dato {random.randint(100, 999)}", self.container)
        label.setStyleSheet("background-color: lightyellow; border: 1px solid black; padding: 4px;")
        self.container_layout.addWidget(label)
        # Opcional: Desplazar automáticamente hacia abajo para ver el nuevo elemento
        QTimer.singleShot(100, lambda: self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedScrollAreaExample()
    window.show()
    sys.exit(app.exec())
