# parallel_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QParallelAnimationGroup, QRect, QEasingCurve

class BasicParallelExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QParallelAnimationGroup - Básico")
        self.resize(400, 300)
        layout = QVBoxLayout(self)
        
        self.button = QPushButton("Animar", self)
        layout.addWidget(self.button)
        
        # Asignar efecto de opacidad al botón
        self.opacity_effect = QGraphicsOpacityEffect(self.button)
        self.button.setGraphicsEffect(self.opacity_effect)
        
        # Animación de geometría: mover el botón
        self.anim_geom = QPropertyAnimation(self.button, b"geometry")
        self.anim_geom.setDuration(2000)
        self.anim_geom.setEasingCurve(QEasingCurve.Type.InOutQuad)
        start_rect = self.button.geometry()
        end_rect = QRect(start_rect.x() + 100, start_rect.y() + 50,
                         start_rect.width(), start_rect.height())
        self.anim_geom.setStartValue(start_rect)
        self.anim_geom.setEndValue(end_rect)
        
        # Animación de opacidad: de 1.0 a 0.3
        self.anim_opacity = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.anim_opacity.setDuration(2000)
        self.anim_opacity.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.anim_opacity.setStartValue(1.0)
        self.anim_opacity.setEndValue(0.3)
        
        # Grupo paralelo que ejecuta ambas animaciones al mismo tiempo
        self.parallel_group = QParallelAnimationGroup(self)
        self.parallel_group.addAnimation(self.anim_geom)
        self.parallel_group.addAnimation(self.anim_opacity)
        
        # Inicia la animación al hacer clic en el botón
        self.button.clicked.connect(self.parallel_group.start)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicParallelExample()
    window.show()
    sys.exit(app.exec())
