# graphics_advanced.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor

class DrawingView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self._start = None
        self._current_rect = None
        self.setMouseTracking(True)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._start = self.mapToScene(event.pos())
            self._current_rect = self.scene().addRect(QRectF(self._start, self._start), QPen(QColor("red"), 2), QBrush(QColor(255, 0, 0, 50)))
    
    def mouseMoveEvent(self, event):
        if self._start is not None and self._current_rect is not None:
            current_pos = self.mapToScene(event.pos())
            rect = QRectF(self._start, current_pos).normalized()
            self._current_rect.setRect(rect)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._start = None
            self._current_rect = None

class AdvancedGraphicsExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QGraphicsView/QGraphicsScene Example")
        self.resize(800, 600)
        
        layout = QVBoxLayout(self)
        self.scene = QGraphicsScene(self)
        self.view = DrawingView(self.scene, self)
        layout.addWidget(self.view)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedGraphicsExample()
    window.show()
    sys.exit(app.exec())
