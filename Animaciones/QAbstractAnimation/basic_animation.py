import sys
from PyQt6.QtCore import QAbstractAnimation, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class BasicTextAnimation(QAbstractAnimation):
    def __init__(self, label, duration=3000, parent=None):
        super().__init__(parent)
        self.label = label
        self._duration = duration

    def duration(self):
        return self._duration

    def updateCurrentTime(self, currentTime):
        progress = currentTime / self._duration
        self.label.setText(f"Progreso: {progress*100:.0f}%")

class BasicAnimationExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animación Básica")
        self.resize(300, 100)
        layout = QVBoxLayout(self)
        self.label = QLabel("Progreso: 0%", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.anim = BasicTextAnimation(self.label, 5000)
        self.anim.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicAnimationExample()
    window.show()
    sys.exit(app.exec())
