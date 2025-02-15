import sys
from PyQt6.QtCore import pyqtProperty, QPropertyAnimation, QParallelAnimationGroup, QRect, QEasingCurve
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class CustomWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._bgColor = QColor("white")
        self.setGeometry(50, 50, 150, 100)

    def getBgColor(self):
        return self._bgColor

    def setBgColor(self, color):
        self._bgColor = color
        self.update()  # Forzar repintado

    bgColor = pyqtProperty(QColor, fget=getBgColor, fset=setBgColor)

    def paintEvent(self, event):
        painter = QPainter(self)
        # Dibuja un rectángulo lleno con el color de fondo
        painter.fillRect(self.rect(), self._bgColor)
        # Opcional: dibujar un borde
        painter.setPen(QColor("black"))
        painter.drawRect(self.rect().adjusted(0, 0, -1, -1))

class AdvancedParallelExample2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QParallelAnimationGroup - Avanzado (v2)")
        self.resize(600, 500)
        # Posicionamiento absoluto para evitar interferencias
        self.custom_widget = CustomWidget(self)
        self.custom_widget.show()
        
        self.button = QPushButton("Iniciar Animación", self)
        self.button.setGeometry(50, 400, 150, 30)
        self.button.clicked.connect(self.startAnimation)
        
        # Animación de geometría: mueve y cambia tamaño del custom_widget
        self.geomAnim = QPropertyAnimation(self.custom_widget, b"geometry")
        self.geomAnim.setDuration(3000)
        self.geomAnim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        start_rect = self.custom_widget.geometry()
        end_rect = QRect(start_rect.x() + 150, start_rect.y() + 100,
                         start_rect.width() + 50, start_rect.height() + 30)
        self.geomAnim.setStartValue(start_rect)
        self.geomAnim.setEndValue(end_rect)
        
        # Animación de color: cambia la propiedad 'bgColor' de blanco a magenta
        self.colorAnim = QPropertyAnimation(self.custom_widget, b"bgColor")
        self.colorAnim.setDuration(3000)
        self.colorAnim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.colorAnim.setStartValue(QColor("white"))
        self.colorAnim.setEndValue(QColor("magenta"))
        
        # Grupo paralelo que ejecuta ambas animaciones simultáneamente
        self.parallelGroup = QParallelAnimationGroup(self)
        self.parallelGroup.addAnimation(self.geomAnim)
        self.parallelGroup.addAnimation(self.colorAnim)

    def startAnimation(self):
        self.parallelGroup.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedParallelExample2()
    window.show()
    sys.exit(app.exec())
