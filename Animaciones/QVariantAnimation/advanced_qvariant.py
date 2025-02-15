import sys
from PyQt6.QtCore import pyqtProperty, QVariantAnimation, QParallelAnimationGroup, QRect, QEasingCurve
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton

class ColorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._bgColor = QColor("white")
        self.setGeometry(50, 50, 200, 100)
    
    def getBgColor(self):
        return self._bgColor
    
    def setBgColor(self, color):
        self._bgColor = color
        self.update()  # Forzar repintado
    
    bgColor = pyqtProperty(QColor, fget=getBgColor, fset=setBgColor)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self._bgColor)
        painter.drawRect(self.rect().adjusted(0, 0, -1, -1))

class AdvancedQVariantExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QVariantAnimation Example")
        self.setGeometry(100, 100, 500, 400)
        
        # Crear un widget personalizado con propiedad "bgColor"
        self.color_widget = ColorWidget(self)
        self.color_widget.show()
        
        # Botón para iniciar la animación
        self.button = QPushButton("Start Animation", self)
        self.button.setGeometry(50, 300, 150, 30)
        
        # Animación de color usando QVariantAnimation (interpolando de white a blue)
        self.colorAnim = QVariantAnimation(self)
        self.colorAnim.setDuration(3000)
        self.colorAnim.setStartValue(QColor("white"))
        self.colorAnim.setEndValue(QColor("blue"))
        self.colorAnim.valueChanged.connect(self.update_color)
        
        # Animación de geometría para mover el widget
        self.geomAnim = QVariantAnimation(self)
        self.geomAnim.setDuration(3000)
        self.geomAnim.setStartValue(self.color_widget.geometry())
        self.geomAnim.setEndValue(QRect(250, 50, 300, 150))
        self.geomAnim.valueChanged.connect(self.update_geometry)
        self.geomAnim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
        # Grupo paralelo para ejecutar ambas animaciones al mismo tiempo
        self.group = QParallelAnimationGroup(self)
        self.group.addAnimation(self.colorAnim)
        self.group.addAnimation(self.geomAnim)
        
        self.button.clicked.connect(self.group.start)
    
    def update_color(self, value):
        # value es un QVariant, que en este caso contiene un QColor
        if isinstance(value, QColor):
            self.color_widget.setBgColor(value)
    
    def update_geometry(self, value):
        # value será un QRect
        if isinstance(value, QRect):
            self.color_widget.setGeometry(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedQVariantExample()
    window.show()
    sys.exit(app.exec())
