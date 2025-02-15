# timeline_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import QTimeLine, Qt

class TimelineBasicExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimeLine Basic Example")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        self.label = QLabel("Progress: 0%", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        # Crear un QTimeLine de 3 segundos (3000 ms)
        self.timeline = QTimeLine(3000, self)
        self.timeline.setFrameRange(0, 100)
        self.timeline.frameChanged.connect(self.update_label)
        self.timeline.finished.connect(lambda: self.label.setText("Finished!"))
        
        # Inicia la animación al hacer clic en el label
        self.label.mousePressEvent = lambda event: self.timeline.start()
    
    def update_label(self, frame):
        self.label.setText(f"Progress: {frame}%")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimelineBasicExample()
    window.show()
    sys.exit(app.exec())
