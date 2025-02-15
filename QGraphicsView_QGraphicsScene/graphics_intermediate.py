# graphics_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsItem
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import QRectF, QPointF, Qt

class TriangleItem(QGraphicsItem):
    def __init__(self):
        super().__init__()
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
                      QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        
    def boundingRect(self):
        return QRectF(0, 0, 100, 100)
    
    def paint(self, painter, option, widget):
        painter.save()
        pen = QPen(Qt.GlobalColor.black, 2)
        painter.setPen(pen)
        brush = QBrush(QColor("green"))
        if self.isSelected():
            brush.setColor(QColor("yellow"))
        painter.setBrush(brush)
        points = [QPointF(50, 0), QPointF(0, 100), QPointF(100, 100)]
        painter.drawPolygon(points)
        painter.restore()

class IntermediateGraphicsExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QGraphicsView/QGraphicsScene Example")
        self.resize(600, 400)
        
        layout = QVBoxLayout(self)
        self.view = QGraphicsView(self)
        layout.addWidget(self.view)
        
        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)
        
        # Añadir un triángulo personalizado a la escena
        triangle = TriangleItem()
        triangle.setPos(150, 100)
        self.scene.addItem(triangle)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateGraphicsExample()
    window.show()
    sys.exit(app.exec())
