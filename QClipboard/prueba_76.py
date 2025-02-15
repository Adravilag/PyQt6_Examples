import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel

class ClipboardExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo de QClipboard")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.input = QLineEdit(self)
        self.copy_button = QPushButton("Copiar al portapapeles", self)
        self.paste_button = QPushButton("Pegar del portapapeles", self)
        self.result_label = QLabel("", self)
        layout.addWidget(self.input)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.paste_button)
        layout.addWidget(self.result_label)
        self.copy_button.clicked.connect(self.copy_text)
        self.paste_button.clicked.connect(self.paste_text)

    def copy_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.input.text())

    def paste_text(self):
        clipboard = QApplication.clipboard()
        self.result_label.setText("Texto pegado: " + clipboard.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClipboardExample()
    window.show()
    sys.exit(app.exec())
