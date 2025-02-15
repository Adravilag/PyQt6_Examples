import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QRect

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QWidget Example - Drawing")
        self.resize(400, 300)
        self.rect_start = None
        self.rect_end = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.rect_start = event.pos()
            self.rect_end = event.pos()
            self.update()

    def mouseMoveEvent(self, event):
        if self.rect_start:
            self.rect_end = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.rect_end = event.pos()
            self.update()
            self.rect_start = None  # Finalizar el dibujo

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.rect_start and self.rect_end:
            painter = QPainter(self)
            pen = QPen(QColor("blue"), 2, Qt.PenStyle.SolidLine)
            painter.setPen(pen)
            rect = self.make_rect(self.rect_start, self.rect_end)
            painter.drawRect(rect)

    def make_rect(self, start, end):
        x1, y1 = start.x(), start.y()
        x2, y2 = end.x(), end.y()
        return QRect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawingWidget()
    window.show()
    sys.exit(app.exec())
