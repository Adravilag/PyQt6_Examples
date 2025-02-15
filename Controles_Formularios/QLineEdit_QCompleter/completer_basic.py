import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCompleter
from PyQt6.QtCore import Qt

class BasicCompleterExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QLineEdit with QCompleter")
        self.resize(300, 100)
        
        layout = QVBoxLayout(self)
        
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Type a fruit...")
        layout.addWidget(self.line_edit)
        
        # Lista estática de palabras sugeridas
        words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
        completer = QCompleter(words, self)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.line_edit.setCompleter(completer)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicCompleterExample()
    window.show()
    sys.exit(app.exec())
