# font_dialog_intermediate.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QFontDialog
)
from PyQt6.QtCore import Qt

class FontDialogIntermediateExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog - Intermedio")
        self.resize(400, 250)

        layout = QVBoxLayout(self)

        self.info_label = QLabel("Texto de ejemplo en QLabel", self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)

        self.edit = QLineEdit("Texto en QLineEdit", self)
        layout.addWidget(self.edit)

        self.button = QPushButton("Cambiar Fuente", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.change_font)

    def change_font(self):
        # Usa la fuente del QLabel como fuente actual predeterminada
        font, ok = QFontDialog.getFont(self.info_label.font(), self, "Elige una fuente para todos")
        if ok:
            # Actualiza la fuente en ambos widgets
            self.info_label.setFont(font)
            self.edit.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontDialogIntermediateExample()
    window.show()
    sys.exit(app.exec())
