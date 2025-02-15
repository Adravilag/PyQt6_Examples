# timeline_intermediate_fixed.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import QTimeLine, Qt, QRect

class TimelineIntermediateExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimeLine Intermediate Example (Fixed)")
        self.resize(400, 300)
        
        # Posicionamiento absoluto para el label
        self.label = QLabel("Progress: 0%", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px;")
        # Posicionar el label manualmente
        self.label.setGeometry(50, 50, 300, 50)
        
        # Crear QTimeLine de 4 segundos
        self.timeline = QTimeLine(4000, self)
        self.timeline.setFrameRange(0, 100)
        self.timeline.frameChanged.connect(self.animate_label)
        self.timeline.finished.connect(lambda: self.label.setText("Done"))
        
        # Inicia la animación al hacer clic sobre el label
        self.label.mousePressEvent = lambda event: self.timeline.start()
    
    def animate_label(self, frame):
        self.label.setText(f"Progress: {frame}%")
        # Mueve el label horizontalmente: de x=50 a x=150
        new_x = 50 + (frame / 100.0) * 100  # movimiento de 100 píxeles
        self.label.setGeometry(int(new_x), 50, 300, 50)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TimelineIntermediateExample()
    window.show()
    sys.exit(app.exec())
