# completer_advanced.py
import sys, random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCompleter, QPushButton
from PyQt6.QtCore import Qt, QStringListModel

class AdvancedCompleterExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QLineEdit with Dynamic QCompleter")
        self.resize(400, 150)
        
        layout = QVBoxLayout(self)
        
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Type to see suggestions...")
        layout.addWidget(self.line_edit)
        
        # Lista de palabras inicial
        self.words = ["apple", "apricot", "banana", "blackberry", "blueberry",
                      "cherry", "citrus", "date", "dragonfruit", "fig", "grape", "kiwi"]
        self.model = QStringListModel(self.words)
        self.completer = QCompleter(self.model, self)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.line_edit.setCompleter(self.completer)
        
        self.update_button = QPushButton("Shuffle Suggestions", self)
        layout.addWidget(self.update_button)
        self.update_button.clicked.connect(self.shuffle_words)
    
    def shuffle_words(self):
        random.shuffle(self.words)
        self.model.setStringList(self.words)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedCompleterExample()
    window.show()
    sys.exit(app.exec())
