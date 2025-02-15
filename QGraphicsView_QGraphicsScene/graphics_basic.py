# graphics_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import QRectF, Qt

class BasicGraphicsExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QGraphicsView/QGraphicsScene Example")
        self.resize(600, 400)
        
        layout = QVBoxLayout(self)
        self.view = QGraphicsView(self)
        layout.addWidget(self.view)
        
        # Crear la escena y asignarla a la vista
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        
        # Añadir un rectángulo
        rect = self.scene.addRect(QRectF(50, 50, 150, 100), brush=QBrush(QColor("red")))
        
        # Añadir una elipse
        ellipse = self.scene.addEllipse(QRectF(250, 150, 120, 90), brush=QBrush(QColor("blue")))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicGraphicsExample()
    window.show()
    sys.exit(app.exec())
