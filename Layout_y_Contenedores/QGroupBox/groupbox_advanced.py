# groupbox_advanced.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QGroupBox, QFormLayout, QLineEdit, QSpinBox, QLabel, QPushButton
)
from PyQt6.QtCore import Qt

class AdvancedGroupBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGroupBox - Avanzado (Colapsible)")
        self.resize(400, 300)

        main_layout = QVBoxLayout(self)

        # Crear un QGroupBox checkable que se comporta como colapsable
        self.collapsible_group = QGroupBox("Advanced Settings", self)
        self.collapsible_group.setCheckable(True)
        self.collapsible_group.setChecked(True)
        self.collapsible_group.toggled.connect(self.on_toggled)

        form_layout = QFormLayout()
        self.setting1_edit = QLineEdit()
        self.setting2_spinbox = QSpinBox()
        self.setting2_spinbox.setRange(0, 100)
        form_layout.addRow("Setting 1:", self.setting1_edit)
        form_layout.addRow("Setting 2:", self.setting2_spinbox)
        self.collapsible_group.setLayout(form_layout)

        main_layout.addWidget(self.collapsible_group)

        # Botón para mostrar resumen
        self.summary_button = QPushButton("Show Settings", self)
        self.summary_button.clicked.connect(self.show_settings)
        main_layout.addWidget(self.summary_button)

        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.result_label)

    def on_toggled(self, checked):
        # Si se desmarca el grupo, ocultar su contenido
        # Aquí simplemente se actualiza el título, pero podrías ocultar el widget contenido si deseas
        if checked:
            self.collapsible_group.setTitle("Advanced Settings (Expanded)")
        else:
            self.collapsible_group.setTitle("Advanced Settings (Collapsed)")

    def show_settings(self):
        setting1 = self.setting1_edit.text()
        setting2 = self.setting2_spinbox.value()
        self.result_label.setText(f"Setting 1: {setting1}, Setting 2: {setting2}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedGroupBoxExample()
    window.show()
    sys.exit(app.exec())
