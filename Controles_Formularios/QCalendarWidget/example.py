import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QCalendarWidget, QFormLayout,
    QLineEdit, QPushButton, QLabel, QListWidget, QListWidgetItem, QHBoxLayout, QDialog, QDialogButtonBox
)
from PyQt6.QtCore import Qt, QDate

class AppointmentDialog(QDialog):
    def __init__(self, date, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add Appointment")
        self.appointment = None
        layout = QFormLayout(self)
        self.date_label = QLabel(date.toString("dddd, MMMM d, yyyy"), self)
        layout.addRow("Date:", self.date_label)
        self.details_edit = QLineEdit(self)
        layout.addRow("Details:", self.details_edit)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def accept(self):
        self.appointment = self.details_edit.text()
        super().accept()

class AppointmentScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Appointment Scheduler")
        self.resize(600, 500)
        layout = QVBoxLayout(self)
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)
        
        self.add_button = QPushButton("Add Appointment", self)
        layout.addWidget(self.add_button)
        self.add_button.clicked.connect(self.add_appointment)
        
        self.appointments_list = QListWidget(self)
        layout.addWidget(self.appointments_list)
        
        self.info_label = QLabel("Select a date and add appointments.", self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)

        # Almacenar citas en un diccionario {QDate: [appointment, ...]}
        self.appointments = {}
    
    def add_appointment(self):
        selected_date = self.calendar.selectedDate()
        dialog = AppointmentDialog(selected_date, self)
        if dialog.exec() == QDialog.DialogCode.Accepted and dialog.appointment:
            # Guardar la cita en el diccionario
            if selected_date in self.appointments:
                self.appointments[selected_date].append(dialog.appointment)
            else:
                self.appointments[selected_date] = [dialog.appointment]
            self.update_appointments_list(selected_date)
    
    def update_appointments_list(self, date):
        self.appointments_list.clear()
        if date in self.appointments:
            for appointment in self.appointments[date]:
                item = QListWidgetItem(f"{date.toString('dd/MM/yyyy')}: {appointment}")
                self.appointments_list.addItem(item)
        else:
            self.appointments_list.addItem("No appointments for this date.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppointmentScheduler()
    window.show()
    sys.exit(app.exec())
