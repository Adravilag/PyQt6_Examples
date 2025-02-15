# groupbox_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QFormLayout, QLineEdit, QSpinBox, QLabel
from PyQt6.QtCore import Qt

class IntermediateGroupBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGroupBox - Intermedio")
        self.resize(400, 200)

        main_layout = QVBoxLayout(self)

        # Crear un QGroupBox para Información Personal
        personal_group = QGroupBox("Personal Information", self)
        form_layout = QFormLayout(personal_group)
        
        self.name_edit = QLineEdit()
        self.age_spinbox = QSpinBox()
        self.age_spinbox.setRange(0, 120)
        self.email_edit = QLineEdit()

        form_layout.addRow("Name:", self.name_edit)
        form_layout.addRow("Age:", self.age_spinbox)
        form_layout.addRow("Email:", self.email_edit)

        main_layout.addWidget(personal_group)

        # Mostrar resumen en una etiqueta (opcional)
        self.summary_label = QLabel("Fill in your information", self)
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.summary_label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateGroupBoxExample()
    window.show()
    sys.exit(app.exec())
