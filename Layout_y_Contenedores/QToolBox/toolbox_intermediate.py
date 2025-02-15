# toolbox_intermediate.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QToolBox, QVBoxLayout, QFormLayout, QLineEdit, QSpinBox, QDateEdit, QLabel
)
from PyQt6.QtCore import QDate

class IntermediateToolBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QToolBox Example")
        self.resize(400, 350)
        
        main_layout = QVBoxLayout(self)
        toolbox = QToolBox(self)
        
        # Página 1: Información Personal
        personal_widget = QWidget()
        personal_layout = QFormLayout(personal_widget)
        self.name_edit = QLineEdit()
        self.age_spinbox = QSpinBox()
        self.age_spinbox.setRange(0, 120)
        self.birth_date_edit = QDateEdit()
        self.birth_date_edit.setCalendarPopup(True)
        self.birth_date_edit.setDate(QDate.currentDate())
        personal_layout.addRow("Name:", self.name_edit)
        personal_layout.addRow("Age:", self.age_spinbox)
        personal_layout.addRow("Birth Date:", self.birth_date_edit)
        toolbox.addItem(personal_widget, "Personal Info")
        
        # Página 2: Información de Contacto
        contact_widget = QWidget()
        contact_layout = QFormLayout(contact_widget)
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        contact_layout.addRow("Email:", self.email_edit)
        contact_layout.addRow("Phone:", self.phone_edit)
        toolbox.addItem(contact_widget, "Contact Info")
        
        main_layout.addWidget(toolbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateToolBoxExample()
    window.show()
    sys.exit(app.exec())
