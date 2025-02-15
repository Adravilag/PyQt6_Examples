# qsettings_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QSettings

class BasicSettingsExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QSettings Example")
        self.resize(400, 200)

        layout = QVBoxLayout(self)
        self.label = QLabel("Esta ventana recuerda su tamaño y posición.", self)
        layout.addWidget(self.label)

        self.button = QPushButton("Reset Settings", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.reset_settings)

        self.settings = QSettings("MyCompany", "MyApp")
        self.load_settings()

    def load_settings(self):
        geometry = self.settings.value("geometry")
        if geometry:
            self.restoreGeometry(geometry)

    def closeEvent(self, event):
        self.settings.setValue("geometry", self.saveGeometry())
        super().closeEvent(event)

    def reset_settings(self):
        self.settings.clear()
        self.setGeometry(100, 100, 400, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicSettingsExample()
    window.show()
    sys.exit(app.exec())
