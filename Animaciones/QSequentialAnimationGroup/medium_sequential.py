# medium_sequential.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout
from PyQt6.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QRect, QEasingCurve, Qt

class MediumSequentialExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medium Sequential Animation Example")
        self.resize(400, 150)
        layout = QVBoxLayout(self)
        
        self.slider = QSlider(Qt.Orientation.Horizontal, self)
        self.slider.setRange(0, 100)
        layout.addWidget(self.slider)
        
        self.label = QLabel("Value: 0", self)
        layout.addWidget(self.label)
        
        # Establece un tamaño fijo para que el layout no modifique su geometría
        self.slider.setFixedSize(self.slider.sizeHint())
        
        # Animación 1: Animar el valor del slider de 0 a 100
        self.anim_value = QPropertyAnimation(self.slider, b"value")
        self.anim_value.setDuration(1500)
        self.anim_value.setStartValue(0)
        self.anim_value.setEndValue(100)
        self.anim_value.setEasingCurve(QEasingCurve.Type.Linear)
        self.anim_value.valueChanged.connect(lambda val: self.label.setText(f"Value: {val}"))
        
        # Animación 2: Mover el slider horizontalmente
        self.anim_geom = QPropertyAnimation(self.slider, b"geometry")
        self.anim_geom.setDuration(1500)
        start_rect = self.slider.geometry()
        end_rect = QRect(start_rect.x() + 50, start_rect.y(),
                         start_rect.width(), start_rect.height())
        self.anim_geom.setStartValue(start_rect)
        self.anim_geom.setEndValue(end_rect)
        self.anim_geom.setEasingCurve(QEasingCurve.Type.InOutQuad)
        
        # Grupo secuencial: primero anima el valor, luego la posición
        self.seq_group = QSequentialAnimationGroup(self)
        self.seq_group.addAnimation(self.anim_value)
        self.seq_group.addAnimation(self.anim_geom)
        
        # Iniciar animación al presionar el slider
        self.slider.sliderPressed.connect(self.seq_group.start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MediumSequentialExample()
    window.show()
    sys.exit(app.exec())
