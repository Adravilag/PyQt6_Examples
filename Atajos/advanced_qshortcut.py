import sys
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class AdvancedQShortcutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QShortcut Example")
        self.resize(400, 200)
        
        layout = QVBoxLayout(self)
        self.label = QLabel("Texto Original (Ctrl+T para alternar)", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        # Atajo Ctrl+T: alterna el texto del label
        self.shortcut_toggle = QShortcut(QKeySequence("Ctrl+T"), self)
        self.shortcut_toggle.activated.connect(self.toggle_text)
        
        # Atajo Ctrl+M: mueve el label 50 píxeles a la derecha
        self.shortcut_move = QShortcut(QKeySequence("Ctrl+M"), self)
        self.shortcut_move.activated.connect(self.move_label)
        
        # Atajo Ctrl+Q: cierra la aplicación
        self.shortcut_quit = QShortcut(QKeySequence("Ctrl+Q"), self)
        self.shortcut_quit.activated.connect(self.close)
        
    def toggle_text(self):
        current_text = self.label.text()
        # Cambiar el texto indicando que se activó Ctrl+T
        if "Original" in current_text:
            new_text = "Texto Alternativo (Ctrl+T activado)"
        else:
            new_text = "Texto Original (Ctrl+T activado)"
        self.label.setText(new_text)
        print("Ctrl+T activado: se ha alternado el texto.")
    
    def move_label(self):
        # Mover el label 50 píxeles a la derecha
        geom = self.label.geometry()
        new_geom = geom.adjusted(50, 0, 50, 0)
        self.label.setGeometry(new_geom)
        print("Ctrl+M activado: el label se ha movido 50 píxeles a la derecha.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedQShortcutExample()
    window.show()
    sys.exit(app.exec())
