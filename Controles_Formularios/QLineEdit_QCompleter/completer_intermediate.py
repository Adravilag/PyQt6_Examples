import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCompleter
from PyQt6.QtCore import Qt

class TabCompleterLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._completer = None

    def setCompleter(self, completer):
        self._completer = completer
        super().setCompleter(completer)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Tab and self._completer:
            prefix = self.text()
            self._completer.setCompletionPrefix(prefix)
            if self._completer.completionCount() > 0:
                index = self._completer.completionModel().index(0, 0)
                completion = self._completer.completionModel().data(index)
                self.setText(completion)
                return
        super().keyPressEvent(event)

class BasicCompleterExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QLineEdit with QCompleter")
        self.resize(300, 100)
        
        layout = QVBoxLayout(self)
        
        self.line_edit = TabCompleterLineEdit(self)
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
