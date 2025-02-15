# calendar_advanced.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel, QPushButton
from PyQt6.QtGui import QTextCharFormat, QBrush, QColor
from PyQt6.QtCore import Qt, QDate

class CalendarAdvancedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget - Avanzado (Selección Múltiple)")
        self.resize(450, 400)
        
        self.selected_dates = set()
        
        layout = QVBoxLayout(self)
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        layout.addWidget(self.calendar)
        
        self.calendar.clicked.connect(self.toggle_date_selection)
        
        self.dates_label = QLabel("Fechas seleccionadas: Ninguna", self)
        self.dates_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.dates_label)
        
        reset_button = QPushButton("Reset Selections", self)
        layout.addWidget(reset_button)
        reset_button.clicked.connect(self.reset_selections)

    def toggle_date_selection(self, date):
        # Si la fecha ya está seleccionada, se deselecciona, de lo contrario se añade
        if date in self.selected_dates:
            self.selected_dates.remove(date)
        else:
            self.selected_dates.add(date)
        self.update_date_formats()
        self.update_dates_label()

    def update_date_formats(self):
        # Restablece el formato para todas las fechas del mes
        default_format = self.calendar.dateTextFormat(self.calendar.minimumDate())
        for d in self.selected_dates:
            fmt = QTextCharFormat()
            fmt.setBackground(QBrush(QColor("lightgreen")))
            self.calendar.setDateTextFormat(d, fmt)
        # Para las fechas no seleccionadas, podemos restablecer el formato
        # (Una implementación completa implicaría recorrer todas las fechas visibles)
        # En este ejemplo, asumiremos que las fechas seleccionadas se mantienen resaltadas

    def update_dates_label(self):
        if self.selected_dates:
            dates_str = ", ".join([d.toString("dd/MM/yyyy") for d in sorted(self.selected_dates)])
            self.dates_label.setText(f"Fechas seleccionadas: {dates_str}")
        else:
            self.dates_label.setText("Fechas seleccionadas: Ninguna")
    
    def reset_selections(self):
        self.selected_dates.clear()
        # Limpiar el formato para todas las fechas (podrías recorrer las fechas visibles)
        self.calendar.setDateTextFormat(QDate(), QTextCharFormat())
        self.update_dates_label()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarAdvancedExample()
    window.show()
    sys.exit(app.exec())
