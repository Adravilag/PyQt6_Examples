# basic_qpropertyanimation.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QPropertyAnimation, QRect, QEasingCurve

class BasicQPropertyAnimationExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QPropertyAnimation Example")
        self.resize(400, 300)
        layout = QVBoxLayout(self)
        self.button = QPushButton("Animate Me", self)
        layout.addWidget(self.button)
        
        # Configuración de la animación para la propiedad "geometry"
        self.anim = QPropertyAnimation(self.button, b"geometry")
        self.anim.setDuration(2000)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        startRect = self.button.geometry()
        endRect = QRect(startRect.x() + 100, startRect.y() + 50,
                        startRect.width(), startRect.height())
        self.anim.setStartValue(startRect)
        self.anim.setEndValue(endRect)
        
        self.button.clicked.connect(self.anim.start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicQPropertyAnimationExample()
    window.show()
    sys.exit(app.exec())
