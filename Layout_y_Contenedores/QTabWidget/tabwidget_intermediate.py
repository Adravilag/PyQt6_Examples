# tabwidget_intermediate.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget, QFormLayout,
    QLineEdit, QSpinBox, QVBoxLayout, QLabel
)
from PyQt6.QtCore import QDate, Qt

class IntermediateTabWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QTabWidget Example")
        self.resize(600, 400)
        
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        # Pestaña 1: Información Personal
        personal_tab = QWidget()
        personal_layout = QFormLayout(personal_tab)
        self.name_edit = QLineEdit()
        self.age_spinbox = QSpinBox()
        self.age_spinbox.setRange(0, 120)
        self.birth_date_edit = QLineEdit()  # Aquí podrías usar QDateEdit en un ejemplo real
        self.birth_date_edit.setText(QDate.currentDate().toString("yyyy-MM-dd"))
        personal_layout.addRow("Name:", self.name_edit)
        personal_layout.addRow("Age:", self.age_spinbox)
        personal_layout.addRow("Birth Date:", self.birth_date_edit)
        self.tab_widget.addTab(personal_tab, "Personal Info")
        
        # Pestaña 2: Información de Contacto
        contact_tab = QWidget()
        contact_layout = QFormLayout(contact_tab)
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        contact_layout.addRow("Email:", self.email_edit)
        contact_layout.addRow("Phone:", self.phone_edit)
        self.tab_widget.addTab(contact_tab, "Contact Info")
        
        # Etiqueta de resumen (opcional)
        self.summary_label = QLabel("Complete the form in each tab", self)
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        main_layout.addWidget(self.summary_label)
        
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateTabWidget()
    window.show()
    sys.exit(app.exec())
