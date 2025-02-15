# qsettings_advanced.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QDialog, QTabWidget, QWidget, QVBoxLayout, QFormLayout,
    QLineEdit, QSpinBox, QPushButton, QDialogButtonBox
)
from PyQt6.QtCore import QSettings

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Advanced Settings")
        self.settings = QSettings("MyCompany", "MyApp")
        
        layout = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        layout.addWidget(self.tabs)
        
        # Pestaña General
        general_tab = QWidget()
        general_layout = QFormLayout(general_tab)
        self.app_name_edit = QLineEdit(self)
        general_layout.addRow("Application Name:", self.app_name_edit)
        self.tabs.addTab(general_tab, "General")
        
        # Pestaña User
        user_tab = QWidget()
        user_layout = QFormLayout(user_tab)
        self.username_edit = QLineEdit(self)
        self.user_age_spinbox = QSpinBox(self)
        self.user_age_spinbox.setRange(0, 150)
        user_layout.addRow("Username:", self.username_edit)
        user_layout.addRow("User Age:", self.user_age_spinbox)
        self.tabs.addTab(user_tab, "User")
        
        # Botones OK/Cancel
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        button_box.accepted.connect(self.save_settings)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)
        
        self.load_settings()
        
    def load_settings(self):
        self.app_name_edit.setText(self.settings.value("General/AppName", "My Application"))
        self.username_edit.setText(self.settings.value("User/Username", "DefaultUser"))
        self.user_age_spinbox.setValue(int(self.settings.value("User/UserAge", 25)))
        
    def save_settings(self):
        self.settings.setValue("General/AppName", self.app_name_edit.text())
        self.settings.setValue("User/Username", self.username_edit.text())
        self.settings.setValue("User/UserAge", self.user_age_spinbox.value())
        self.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = SettingsDialog()
    if dialog.exec() == QDialog.DialogCode.Accepted:
        print("Settings saved.")
    sys.exit(app.exec())
