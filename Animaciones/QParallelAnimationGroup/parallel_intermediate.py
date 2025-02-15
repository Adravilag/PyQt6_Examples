# parallel_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import QPropertyAnimation, QParallelAnimationGroup, QRect, QEasingCurve

class IntermediateParallelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QParallelAnimationGroup - Intermedio")
        self.resize(400, 200)
        
        main_layout = QVBoxLayout(self)
        
        # Crear dos botones
        self.button1 = QPushButton("Mover Horizontal", self)
        self.button2 = QPushButton("Mover Vertical", self)
        
        # Colocarlos en un layout horizontal
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button1)
        h_layout.addWidget(self.button2)
        main_layout.addLayout(h_layout)
        
        self.anim_group = QParallelAnimationGroup(self)
        
        anim1 = QPropertyAnimation(self.button1, b"geometry")
        anim1.setDuration(2000)
        anim1.setEasingCurve(QEasingCurve.Type.InOutQuad)
        start_rect1 = self.button1.geometry()
        end_rect1 = QRect(start_rect1.x() + 100, start_rect1.y(),
                          start_rect1.width(), start_rect1.height())
        anim1.setStartValue(start_rect1)
        anim1.setEndValue(end_rect1)
        
        anim2 = QPropertyAnimation(self.button2, b"geometry")
        anim2.setDuration(2000)
        anim2.setEasingCurve(QEasingCurve.Type.InOutQuad)
        start_rect2 = self.button2.geometry()
        end_rect2 = QRect(start_rect2.x(), start_rect2.y() + 100,
                          start_rect2.width(), start_rect2.height())
        anim2.setStartValue(start_rect2)
        anim2.setEndValue(end_rect2)
        
        self.anim_group.addAnimation(anim1)
        self.anim_group.addAnimation(anim2)
        
        # Iniciar la animación al presionar cualquiera de los botones
        self.button1.clicked.connect(self.anim_group.start)
        self.button2.clicked.connect(self.anim_group.start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateParallelExample()
    window.show()
    sys.exit(app.exec())
