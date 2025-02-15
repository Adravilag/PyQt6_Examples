# basic_qshortcut.py
import sys
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class BasicQShortcutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QShortcut Example")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        self.label = QLabel("Presiona Ctrl+P", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        # Crear un atajo: Ctrl+P
        shortcut = QShortcut(QKeySequence("Ctrl+P"), self)
        shortcut.activated.connect(self.shortcut_triggered)
        
    def shortcut_triggered(self):
        self.label.setText("¡Ctrl+P presionado!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicQShortcutExample()
    window.show()
    sys.exit(app.exec())
