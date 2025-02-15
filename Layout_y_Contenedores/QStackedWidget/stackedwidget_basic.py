# stackedwidget_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel, QHBoxLayout

class BasicStackedWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QStackedWidget Example")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        
        # Crear el QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        layout.addWidget(self.stacked_widget)
        
        # Página 1: Un QLabel
        page1 = QWidget()
        page1_layout = QVBoxLayout(page1)
        page1_layout.addWidget(QLabel("Esta es la Página 1", page1))
        self.stacked_widget.addWidget(page1)
        
        # Página 2: Otro QLabel
        page2 = QWidget()
        page2_layout = QVBoxLayout(page2)
        page2_layout.addWidget(QLabel("Esta es la Página 2", page2))
        self.stacked_widget.addWidget(page2)
        
        # Botones de navegación
        nav_layout = QHBoxLayout()
        prev_button = QPushButton("Anterior", self)
        next_button = QPushButton("Siguiente", self)
        prev_button.clicked.connect(self.show_previous)
        next_button.clicked.connect(self.show_next)
        nav_layout.addWidget(prev_button)
        nav_layout.addWidget(next_button)
        layout.addLayout(nav_layout)
        
    def show_previous(self):
        index = self.stacked_widget.currentIndex()
        if index > 0:
            self.stacked_widget.setCurrentIndex(index - 1)
            
    def show_next(self):
        index = self.stacked_widget.currentIndex()
        if index < self.stacked_widget.count() - 1:
            self.stacked_widget.setCurrentIndex(index + 1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicStackedWidget()
    window.show()
    sys.exit(app.exec())
