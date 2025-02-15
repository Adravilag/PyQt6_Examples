# stackedwidget_advanced.py
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget, QVBoxLayout,
    QPushButton, QHBoxLayout, QLabel, QLineEdit, QMessageBox
)
from PyQt6.QtCore import Qt

class AdvancedStackedWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QStackedWidget Example")
        self.resize(600, 400)
        
        # Widget central y layout principal
        central = QWidget(self)
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        
        # QStackedWidget para las páginas
        self.stacked_widget = QStackedWidget(self)
        main_layout.addWidget(self.stacked_widget)
        
        # Panel de control
        control_layout = QHBoxLayout()
        self.add_button = QPushButton("Agregar Pestaña", self)
        self.remove_button = QPushButton("Eliminar Pestaña Actual", self)
        control_layout.addWidget(self.add_button)
        control_layout.addWidget(self.remove_button)
        main_layout.addLayout(control_layout)
        
        self.add_button.clicked.connect(self.add_new_tab)
        self.remove_button.clicked.connect(self.remove_current_tab)
        
        self.tab_counter = 0
        # Agregar una pestaña inicial
        self.add_new_tab()

    def add_new_tab(self):
        self.tab_counter += 1
        new_tab = QWidget()
        layout = QVBoxLayout(new_tab)
        label = QLabel(f"Contenido de la Pestaña {self.tab_counter}", new_tab)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.stacked_widget.addWidget(new_tab)
        self.stacked_widget.setCurrentWidget(new_tab)

    def remove_current_tab(self):
        current_index = self.stacked_widget.currentIndex()
        if self.stacked_widget.count() > 1:
            self.stacked_widget.removeWidget(self.stacked_widget.widget(current_index))
        else:
            QMessageBox.information(self, "Información", "No se puede cerrar la última pestaña.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedStackedWidget()
    window.show()
    sys.exit(app.exec())
