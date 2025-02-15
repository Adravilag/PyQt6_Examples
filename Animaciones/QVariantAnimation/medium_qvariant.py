# medium_qvariant.py
import sys
from PyQt6.QtCore import QVariantAnimation, Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

def interpolate_color(start_color: QColor, end_color: QColor, progress: float) -> QColor:
    r = int(start_color.red() + (end_color.red() - start_color.red()) * progress)
    g = int(start_color.green() + (end_color.green() - start_color.green()) * progress)
    b = int(start_color.blue() + (end_color.blue() - start_color.blue()) * progress)
    return QColor(r, g, b)

class MediumQVariantExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medium QVariantAnimation")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        self.label = QLabel("Color Animation", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; background-color: white;")
        layout.addWidget(self.label)
        
        # Crear una QVariantAnimation para interpolar de 0 a 1 (representa el progreso)
        self.animation = QVariantAnimation(self)
        self.animation.setDuration(3000)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.valueChanged.connect(self.on_value_changed)
        
        # Inicia la animación al hacer clic en el label
        self.label.mousePressEvent = lambda event: self.animation.start()
        
        self.start_color = QColor("white")
        self.end_color = QColor("black")
    
    def on_value_changed(self, value):
        progress = float(value)
        color = interpolate_color(self.start_color, self.end_color, progress)
        self.label.setStyleSheet(f"font-size: 24px; background-color: {color.name()};")
        self.label.setText(f"Progress: {int(progress*100)}%")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MediumQVariantExample()
    window.show()
    sys.exit(app.exec())
