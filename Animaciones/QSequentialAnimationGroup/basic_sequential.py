# basic_sequential.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QRect, QEasingCurve

class BasicSequentialExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic Sequential Animation")
        self.resize(400, 300)
        layout = QVBoxLayout(self)
        self.button = QPushButton("Animate Sequentially", self)
        layout.addWidget(self.button)
        
        # Animación 1: mover el botón
        self.anim_move = QPropertyAnimation(self.button, b"geometry")
        self.anim_move.setDuration(1500)
        self.anim_move.setEasingCurve(QEasingCurve.Type.InOutQuad)
        start_rect = self.button.geometry()
        end_rect = QRect(start_rect.x() + 100, start_rect.y() + 50,
                         start_rect.width(), start_rect.height())
        self.anim_move.setStartValue(start_rect)
        self.anim_move.setEndValue(end_rect)
        
        # Animación 2: animación dummy para cambiar texto (sin cambio visual)
        self.anim_dummy = QPropertyAnimation(self.button, b"geometry")
        self.anim_dummy.setDuration(500)
        self.anim_dummy.setStartValue(end_rect)
        self.anim_dummy.setEndValue(end_rect)
        self.anim_dummy.finished.connect(lambda: self.button.setText("Animation Done"))
        
        # Grupo secuencial: primero mueve, luego cambia el texto
        self.seq_group = QSequentialAnimationGroup(self)
        self.seq_group.addAnimation(self.anim_move)
        self.seq_group.addAnimation(self.anim_dummy)
        
        self.button.clicked.connect(self.seq_group.start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicSequentialExample()
    window.show()
    sys.exit(app.exec())
