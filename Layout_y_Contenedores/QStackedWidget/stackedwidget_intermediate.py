import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget, QLabel, QComboBox
from PyQt6.QtCore import Qt, QDate

class IntermediateStackedWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QStackedWidget Example")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        
        # Crear el QStackedWidget y agregarlo al layout
        self.stacked_widget = QStackedWidget(self)
        layout.addWidget(self.stacked_widget)
        
        # Crear un QComboBox para seleccionar la página
        self.combo = QComboBox(self)
        self.combo.addItems(["Página 1", "Página 2", "Página 3"])
        layout.addWidget(self.combo)
        
        # Agregar 3 páginas al QStackedWidget
        for i in range(1, 4):
            page = QWidget()
            page_layout = QVBoxLayout(page)
            label = QLabel(f"Esta es la Página {i}", page)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            page_layout.addWidget(label)
            self.stacked_widget.addWidget(page)
        
        # Conectar la señal del combo para cambiar de página
        self.combo.currentIndexChanged.connect(self.stacked_widget.setCurrentIndex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateStackedWidget()
    window.show()
    sys.exit(app.exec())
