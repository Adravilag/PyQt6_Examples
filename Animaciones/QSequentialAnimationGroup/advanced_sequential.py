# advanced_sequential.py
import sys
from PyQt6.QtCore import pyqtProperty, QPropertyAnimation, QSequentialAnimationGroup, QRect, QEasingCurve, Qt
from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class RotatingFadingLabel(QWidget):
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self._angle = 0.0
        self._opacity = 1.0
        self._text = text
        self._font = QFont("Arial", 24)
        self.setMinimumSize(300, 100)

    def getAngle(self):
        return self._angle

    def setAngle(self, angle):
        self._angle = angle
        self.update()

    angle = pyqtProperty(float, fget=getAngle, fset=setAngle)

    def getOpacity(self):
        return self._opacity

    def setOpacity(self, opacity):
        self._opacity = opacity
        self.update()

    opacity = pyqtProperty(float, fget=getOpacity, fset=setOpacity)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setFont(self._font)
        # Aplicar opacidad
        painter.setOpacity(self._opacity)
        # Guardar el estado actual y trasladar el origen al centro
        painter.save()
        center = self.rect().center()
        painter.translate(center)
        painter.rotate(self._angle)
        painter.translate(-center)
        # Dibujar el texto centrado
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self._text)
        painter.restore()

class AdvancedSequentialExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Sequential Animation")
        self.resize(500, 400)
        layout = QVBoxLayout(self)
        
        self.rotatingLabel = RotatingFadingLabel("Rotating & Fading", self)
        self.rotatingLabel.setFixedSize(300, 100)
        layout.addWidget(self.rotatingLabel)
        
        self.button = QPushButton("Start Animation", self)
        layout.addWidget(self.button)
        
        # Animación 1: Rotación de 0 a 360 grados
        self.anim_rotate = QPropertyAnimation(self.rotatingLabel, b"angle")
        self.anim_rotate.setDuration(2000)
        self.anim_rotate.setStartValue(0)
        self.anim_rotate.setEndValue(360)
        self.anim_rotate.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
        # Animación 2: Fade out (opacidad de 1 a 0)
        self.anim_fade = QPropertyAnimation(self.rotatingLabel, b"opacity")
        self.anim_fade.setDuration(2000)
        self.anim_fade.setStartValue(1.0)
        self.anim_fade.setEndValue(0.0)
        self.anim_fade.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
        # Grupo secuencial: primero rotar, luego fade out
        self.seq_group = QSequentialAnimationGroup(self)
        self.seq_group.addAnimation(self.anim_rotate)
        self.seq_group.addAnimation(self.anim_fade)
        
        self.button.clicked.connect(self.seq_group.start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedSequentialExample()
    window.show()
    sys.exit(app.exec())
