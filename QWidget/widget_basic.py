# widget_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class BasicWidgetExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QWidget Example")
        self.resize(300, 150)

        layout = QVBoxLayout(self)

        self.label = QLabel("¡Hola, soy un QWidget básico!", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Haz clic", self)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        self.label.setText("¡Botón pulsado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasicWidgetExample()
    window.show()
    sys.exit(app.exec())
