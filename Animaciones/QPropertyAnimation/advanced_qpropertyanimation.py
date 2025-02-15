import sys
from PyQt6.QtCore import pyqtProperty, QPropertyAnimation, QParallelAnimationGroup, QRect, QEasingCurve, Qt
from PyQt6.QtGui import QPainter, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class RotatingLabel(QWidget):
    def __init__(self, text="", parent=None):
        super().__init__(parent)
        self._angle = 0.0
        self._text = text
        self._font = QFont("Arial", 24)
        self.setMinimumSize(300, 100)

    def getAngle(self):
        return self._angle

    def setAngle(self, angle):
        self._angle = angle
        self.update()  # Forzar repintado para reflejar la nueva rotación

    angle = pyqtProperty(float, fget=getAngle, fset=setAngle)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setFont(self._font)
        # Guardar el estado actual del pintor
        painter.save()
        # Mover el origen al centro del widget
        center = self.rect().center()
        painter.translate(center)
        painter.rotate(self._angle)
        painter.translate(-center)
        # Dibujar el texto centrado en el widget
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self._text)
        # Restaurar el estado
        painter.restore()

class AdvancedQPropertyAnimationExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QPropertyAnimation Example - Rotating Text")
        self.resize(500, 400)
        layout = QVBoxLayout(self)
        
        # Crear la instancia de RotatingLabel
        self.rotatingLabel = RotatingLabel("Rotating Text", self)
        self.rotatingLabel.setMinimumSize(300, 100)
        layout.addWidget(self.rotatingLabel)
        
        # Botón para iniciar la animación
        self.button = QPushButton("Start Animation", self)
        layout.addWidget(self.button)
        
        # Animación para la propiedad 'angle' (rotación)
        self.anim_rotation = QPropertyAnimation(self.rotatingLabel, b"angle")
        self.anim_rotation.setDuration(3000)
        self.anim_rotation.setStartValue(0)
        self.anim_rotation.setEndValue(360)
        self.anim_rotation.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
        # Animación para la propiedad 'geometry' (movimiento)
        self.anim_geometry = QPropertyAnimation(self.rotatingLabel, b"geometry")
        self.anim_geometry.setDuration(3000)
        start_rect = self.rotatingLabel.geometry()
        end_rect = QRect(start_rect.x() + 50, start_rect.y() + 50,
                         start_rect.width(), start_rect.height())
        self.anim_geometry.setStartValue(start_rect)
        self.anim_geometry.setEndValue(end_rect)
        self.anim_geometry.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
        # Grupo paralelo para ejecutar ambas animaciones simultáneamente
        self.parallel_group = QParallelAnimationGroup(self)
        self.parallel_group.addAnimation(self.anim_rotation)
        self.parallel_group.addAnimation(self.anim_geometry)
        
        self.button.clicked.connect(self.parallel_group.start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedQPropertyAnimationExample()
    window.show()
    sys.exit(app.exec())
