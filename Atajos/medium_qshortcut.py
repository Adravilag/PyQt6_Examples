# medium_qshortcut.py
import sys
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class MediumQShortcutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medium QShortcut Example")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        self.label = QLabel("Presiona Ctrl+O o Ctrl+S", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        # Atajo Ctrl+O
        shortcut_open = QShortcut(QKeySequence("Ctrl+O"), self)
        shortcut_open.activated.connect(lambda: self.label.setText("Open"))
        
        # Atajo Ctrl+S
        shortcut_save = QShortcut(QKeySequence("Ctrl+S"), self)
        shortcut_save.activated.connect(lambda: self.label.setText("Save"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MediumQShortcutExample()
    window.show()
    sys.exit(app.exec())
