# calendar_intermediate.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel, QPushButton
from PyQt6.QtGui import QTextCharFormat, QBrush, QColor
from PyQt6.QtCore import Qt, QDate

class CalendarIntermediateExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget - Intermedio")
        self.resize(400, 350)
        
        layout = QVBoxLayout(self)
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)
        
        # Resaltar fines de semana
        self.highlight_weekends()
        
        self.date_label = QLabel("", self)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.date_label)
        
        reset_button = QPushButton("Reset to Today", self)
        layout.addWidget(reset_button)
        reset_button.clicked.connect(self.reset_to_today)
        
        self.calendar.selectionChanged.connect(self.update_date_label)
        self.update_date_label()

    def highlight_weekends(self):
        fmt = QTextCharFormat()
        fmt.setBackground(QBrush(QColor("lightblue")))
        # Iterar por el mes actual (por simplicidad, resaltamos fines de semana para el año actual)
        current_year = self.calendar.selectedDate().year()
        for month in range(1, 13):
            for day in range(1, 32):
                date = QDate(current_year, month, day)
                if date.isValid():
                    if date.dayOfWeek() in (6, 7):  # sábado = 6, domingo = 7
                        self.calendar.setDateTextFormat(date, fmt)

    def reset_to_today(self):
        self.calendar.setSelectedDate(QDate.currentDate())
        self.update_date_label()

    def update_date_label(self):
        selected_date = self.calendar.selectedDate()
        self.date_label.setText(f"Fecha seleccionada: {selected_date.toString('dddd, MMMM d, yyyy')}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarIntermediateExample()
    window.show()
    sys.exit(app.exec())
