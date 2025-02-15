import sys
from PyQt6.QtCore import QAbstractAnimation, QRect, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QColor

def interpolate_value(start, end, progress):
    return start + (end - start) * progress

def interpolate_rect(start_rect, end_rect, progress):
    new_x = interpolate_value(start_rect.x(), end_rect.x(), progress)
    new_y = interpolate_value(start_rect.y(), end_rect.y(), progress)
    new_w = interpolate_value(start_rect.width(), end_rect.width(), progress)
    new_h = interpolate_value(start_rect.height(), end_rect.height(), progress)
    return QRect(int(new_x), int(new_y), int(new_w), int(new_h))

def interpolate_color(start_color, end_color, progress):
    new_r = int(interpolate_value(start_color.red(), end_color.red(), progress))
    new_g = int(interpolate_value(start_color.green(), end_color.green(), progress))
    new_b = int(interpolate_value(start_color.blue(), end_color.blue(), progress))
    return QColor(new_r, new_g, new_b)

class AdvancedAnimation(QAbstractAnimation):
    def __init__(self, widget, start_rect, end_rect, start_color, end_color, duration=4000, parent=None):
        super().__init__(parent)
        self.widget = widget
        self.start_rect = start_rect
        self.end_rect = end_rect
        self.start_color = start_color
        self.end_color = end_color
        self._duration = duration

    def duration(self):
        return self._duration

    def updateCurrentTime(self, currentTime):
        # Aseguramos que progress no supere 1.0
        progress = min(currentTime / self._duration, 1.0)
        # Interpolamos la geometría
        new_rect = interpolate_rect(self.start_rect, self.end_rect, progress)
        self.widget.setGeometry(new_rect)
        # Interpolamos el color
        new_color = interpolate_color(self.start_color, self.end_color, progress)
        self.widget.setStyleSheet(f"background-color: {new_color.name()};")
        # Actualizamos el texto para mostrar el progreso
        self.widget.setText(f"Progreso: {progress*100:.0f}%")

class AdvancedAnimationExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animación Avanzada Mejorada")
        self.resize(500, 400)
        layout = QVBoxLayout(self)
        self.label = QLabel("Progreso: 0%", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # Establece un color inicial visible (blanco)
        self.label.setStyleSheet("background-color: #ffffff;")
        layout.addWidget(self.label)
        # Forzamos una geometría inicial
        self.label.setGeometry(50, 50, 200, 100)
        # Configuramos la animación avanzada
        self.anim = AdvancedAnimation(
            widget=self.label,
            start_rect=self.label.geometry(),
            end_rect=QRect(250, 250, 300, 150),
            start_color=QColor("white"),
            end_color=QColor("blue"),
            duration=4000
        )
        self.anim.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedAnimationExample()
    window.show()
    sys.exit(app.exec())
