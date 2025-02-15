# qsettings_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QSpinBox, QPushButton
from PyQt6.QtCore import QSettings

class IntermediateSettingsExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QSettings Example")
        self.resize(400, 250)

        self.settings = QSettings("MyCompany", "MyApp")
        
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        self.username_edit = QLineEdit(self)
        self.age_spinbox = QSpinBox(self)
        self.age_spinbox.setRange(0, 150)
        
        form_layout.addRow("Username:", self.username_edit)
        form_layout.addRow("Age:", self.age_spinbox)
        layout.addLayout(form_layout)
        
        self.save_button = QPushButton("Save Settings", self)
        layout.addWidget(self.save_button)
        self.save_button.clicked.connect(self.save_settings)
        
        self.load_settings()

    def load_settings(self):
        self.username_edit.setText(self.settings.value("username", "DefaultUser"))
        self.age_spinbox.setValue(int(self.settings.value("age", 25)))

    def save_settings(self):
        self.settings.setValue("username", self.username_edit.text())
        self.settings.setValue("age", self.age_spinbox.value())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateSettingsExample()
    window.show()
    sys.exit(app.exec())
