# font_dialog_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFontDialog
from PyQt6.QtCore import Qt

class FontDialogBasicExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog - Básico")
        self.resize(400, 200)

        layout = QVBoxLayout(self)

        self.label = QLabel("Hola, elige una fuente.", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        self.button = QPushButton("Elegir Fuente", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.choose_font)

    def choose_font(self):
        font, ok = QFontDialog.getFont(self.label.font(), self, "Elige una fuente")
        if ok:
            self.label.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontDialogBasicExample()
    window.show()
    sys.exit(app.exec())
