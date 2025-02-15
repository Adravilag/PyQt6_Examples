import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog,
    QMessageBox, QStatusBar, QToolBar
)
from PyQt6.QtGui import QKeySequence, QAction, QIcon, QShortcut
from PyQt6.QtCore import Qt

class AdvancedTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Text Editor with Shortcuts")
        self.resize(900, 600)

        # Crear el editor de texto central
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # Barra de estado
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Crear la barra de herramientas
        self.create_toolbar()

        # Atajo adicional para cerrar la aplicación
        QShortcut(QKeySequence("Ctrl+Q"), self, activated=self.close)

    def create_toolbar(self):
        toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(toolbar)

        # Nuevo documento
        new_action = QAction(QIcon(), "New", self)
        new_action.setShortcut(QKeySequence("Ctrl+N"))
        new_action.triggered.connect(self.new_file)
        toolbar.addAction(new_action)

        # Abrir archivo
        open_action = QAction(QIcon(), "Open", self)
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        open_action.triggered.connect(self.open_file)
        toolbar.addAction(open_action)

        # Guardar archivo
        save_action = QAction(QIcon(), "Save", self)
        save_action.setShortcut(QKeySequence("Ctrl+S"))
        save_action.triggered.connect(self.save_file)
        toolbar.addAction(save_action)

        # Cortar, Copiar, Pegar
        cut_action = QAction(QIcon(), "Cut", self)
        cut_action.setShortcut(QKeySequence("Ctrl+X"))
        cut_action.triggered.connect(self.text_edit.cut)
        toolbar.addAction(cut_action)

        copy_action = QAction(QIcon(), "Copy", self)
        copy_action.setShortcut(QKeySequence("Ctrl+C"))
        copy_action.triggered.connect(self.text_edit.copy)
        toolbar.addAction(copy_action)

        paste_action = QAction(QIcon(), "Paste", self)
        paste_action.setShortcut(QKeySequence("Ctrl+V"))
        paste_action.triggered.connect(self.text_edit.paste)
        toolbar.addAction(paste_action)

        # Deshacer y Rehacer
        undo_action = QAction(QIcon(), "Undo", self)
        undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        undo_action.triggered.connect(self.text_edit.undo)
        toolbar.addAction(undo_action)

        redo_action = QAction(QIcon(), "Redo", self)
        redo_action.setShortcut(QKeySequence("Ctrl+Y"))
        redo_action.triggered.connect(self.text_edit.redo)
        toolbar.addAction(redo_action)

    def new_file(self):
        if self.maybe_save():
            self.text_edit.clear()
            self.status_bar.showMessage("New file created", 2000)

    def open_file(self):
        if self.maybe_save():
            filename, _ = QFileDialog.getOpenFileName(
                self, "Open File", "", "Text Files (*.txt);;All Files (*)"
            )
            if filename:
                try:
                    with open(filename, 'r', encoding='utf-8') as file:
                        self.text_edit.setText(file.read())
                    self.status_bar.showMessage("File opened successfully", 2000)
                except Exception as e:
                    QMessageBox.warning(self, "Error", f"Cannot open file: {e}")

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text Files (*.txt);;All Files (*)"
        )
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(self.text_edit.toPlainText())
                self.status_bar.showMessage("File saved successfully", 2000)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Cannot save file: {e}")

    def maybe_save(self):
        if not self.text_edit.document().isModified():
            return True
        ret = QMessageBox.warning(
            self,
            "Text Editor",
            "The document has been modified.\nDo you want to save your changes?",
            QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel
        )
        if ret == QMessageBox.StandardButton.Save:
            self.save_file()
            return True
        elif ret == QMessageBox.StandardButton.Cancel:
            return False
        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = AdvancedTextEditor()
    editor.show()
    sys.exit(app.exec())
