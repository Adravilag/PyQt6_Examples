# basic_qvariant.py
import sys
from PyQt6.QtCore import QVariantAnimation, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class BasicQVariantExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QVariantAnimation")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        self.label = QLabel("Value: 0", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        # Crear una QVariantAnimation que interpole de 0 a 255 en 3 segundos
        self.animation = QVariantAnimation(self)
        self.animation.setDuration(3000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(255)
        self.animation.valueChanged.connect(self.on_value_changed)
        
        # Inicia la animación al hacer clic en la ventana
        self.mousePressEvent = lambda event: self.animation.start()
        
    def on_value_changed(self, value):
        self.label.setText(f"Value: {int(value)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicQVariantExample()
    window.show()
    sys.exit(app.exec())
