# calendar_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel
from PyQt6.QtCore import Qt

class CalendarBasicExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget - Básico")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)
        
        self.date_label = QLabel("", self)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.date_label)
        
        self.calendar.selectionChanged.connect(self.update_date_label)
        self.update_date_label()  # Inicializa con la fecha actual seleccionada

    def update_date_label(self):
        selected_date = self.calendar.selectedDate()
        self.date_label.setText(f"Fecha seleccionada: {selected_date.toString('dddd, MMMM d, yyyy')}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarBasicExample()
    window.show()
    sys.exit(app.exec())
