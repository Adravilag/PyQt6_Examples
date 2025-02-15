# font_dialog_advanced.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFontDialog, QHBoxLayout, QLineEdit
)
from PyQt6.QtCore import Qt

class FontDialogAdvancedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog - Avanzado")
        self.resize(500, 300)

        self.selected_font = None  # Almacena la fuente seleccionada

        main_layout = QVBoxLayout(self)

        # Panel superior: botón para elegir fuente y mostrar la fuente actual
        top_layout = QHBoxLayout()
        self.choose_font_button = QPushButton("Elegir Fuente", self)
        self.choose_font_button.clicked.connect(self.choose_font)
        top_layout.addWidget(self.choose_font_button)

        self.font_display = QLineEdit("Fuente actual", self)
        self.font_display.setReadOnly(True)
        top_layout.addWidget(self.font_display)
        main_layout.addLayout(top_layout)

        # Área de vista previa
        self.preview_label = QLabel("Vista Previa: Texto de Ejemplo", self)
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.preview_label)

        # Botón para aplicar la fuente almacenada a la vista previa
        self.apply_button = QPushButton("Aplicar Fuente Guardada", self)
        self.apply_button.clicked.connect(self.apply_saved_font)
        main_layout.addWidget(self.apply_button)

    def choose_font(self):
        # Usamos la fuente actual del preview como base
        initial_font = self.preview_label.font() if self.selected_font is None else self.selected_font
        font, ok = QFontDialog.getFont(initial_font, self, "Selecciona una fuente")
        if ok:
            self.selected_font = font
            # Mostrar la descripción de la fuente en el QLineEdit
            self.font_display.setText(f"{font.family()}, {font.pointSize()} pt")
            # Aplicar la fuente a la vista previa automáticamente
            self.preview_label.setFont(font)

    def apply_saved_font(self):
        if self.selected_font:
            self.preview_label.setFont(self.selected_font)
        else:
            self.font_display.setText("No hay fuente guardada.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontDialogAdvancedExample()
    window.show()
    sys.exit(app.exec())
