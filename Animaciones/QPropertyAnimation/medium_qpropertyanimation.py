# medium_qpropertyanimation.py
import sys
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QGraphicsOpacityEffect

class MediumQPropertyAnimationExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medium QPropertyAnimation Example")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        
        self.label = QLabel("Fade Me", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.label)
        
        # Asignamos un efecto de opacidad al label
        self.opacityEffect = QGraphicsOpacityEffect(self.label)
        self.label.setGraphicsEffect(self.opacityEffect)
        
        # Configuración de la animación para la propiedad "opacity"
        self.anim = QPropertyAnimation(self.opacityEffect, b"opacity")
        self.anim.setDuration(2000)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        
        # Inicia la animación al hacer clic en el label
        self.label.mousePressEvent = lambda event: self.anim.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MediumQPropertyAnimationExample()
    window.show()
    sys.exit(app.exec())
