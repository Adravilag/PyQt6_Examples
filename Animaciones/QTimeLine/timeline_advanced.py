# timeline_advanced.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimeLine, Qt
from PyQt6.QtGui import QColor

def interpolate_color(start_color, end_color, progress):
    # Interpolar cada componente de color
    r = int(start_color.red() + (end_color.red() - start_color.red()) * progress)
    g = int(start_color.green() + (end_color.green() - start_color.green()) * progress)
    b = int(start_color.blue() + (end_color.blue() - start_color.blue()) * progress)
    return QColor(r, g, b)

class TimelineAdvancedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimeLine Advanced Example")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        
        self.label = QLabel("Color Animation", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Color inicial: blanco
        self.label.setStyleSheet("background-color: white; font-size: 24px;")
        layout.addWidget(self.label)
        
        self.timeline = QTimeLine(5000, self)  # Duración de 5 segundos
        self.timeline.setFrameRange(0, 100)
        self.timeline.frameChanged.connect(self.update_color)
        self.timeline.finished.connect(lambda: self.label.setText("Finished"))
        
        self.label.mousePressEvent = lambda event: self.timeline.start()
        self.start_color = QColor("white")
        self.end_color = QColor("red")
    
    def update_color(self, frame):
        progress = frame / 100.0
        color = interpolate_color(self.start_color, self.end_color, progress)
        self.label.setStyleSheet(f"background-color: {color.name()}; font-size: 24px;")
        self.label.setText(f"Progress: {frame}%")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimelineAdvancedExample()
    window.show()
    sys.exit(app.exec())
