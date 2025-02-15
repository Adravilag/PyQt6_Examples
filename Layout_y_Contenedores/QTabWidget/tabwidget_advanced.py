import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QTabWidget, QVBoxLayout,
    QPushButton, QHBoxLayout, QLineEdit, QLabel
)
from PyQt6.QtCore import Qt

class AdvancedTabWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QTabWidget Example")
        self.resize(800, 600)
        
        # Crear widget central y layout principal
        central = QWidget(self)
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        
        # Crear QTabWidget y habilitar pestañas cerrables y movibles
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.setMovable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        main_layout.addWidget(self.tab_widget)
        
        # Panel de control para agregar y renombrar pestañas
        control_layout = QHBoxLayout()
        
        self.add_tab_button = QPushButton("Add Tab", self)
        self.add_tab_button.clicked.connect(self.add_tab)
        control_layout.addWidget(self.add_tab_button)
        
        self.rename_line_edit = QLineEdit(self)
        self.rename_line_edit.setPlaceholderText("New tab title")
        control_layout.addWidget(self.rename_line_edit)
        
        self.rename_button = QPushButton("Rename Current Tab", self)
        self.rename_button.clicked.connect(self.rename_tab)
        control_layout.addWidget(self.rename_button)
        
        main_layout.addLayout(control_layout)
        
        # Inicializar contador para nombres de pestañas
        self.tab_counter = 0
        
        # Agregar una pestaña inicial
        self.add_tab()

    def add_tab(self):
        self.tab_counter += 1
        new_tab = QWidget()
        layout = QVBoxLayout(new_tab)
        label = QLabel(f"This is dynamically added Tab {self.tab_counter}", new_tab)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        self.tab_widget.addTab(new_tab, f"Tab {self.tab_counter}")
        self.tab_widget.setCurrentWidget(new_tab)

    def rename_tab(self):
        new_title = self.rename_line_edit.text().strip()
        if new_title:
            index = self.tab_widget.currentIndex()
            if index != -1:
                self.tab_widget.setTabText(index, new_title)
                self.rename_line_edit.clear()

    def close_tab(self, index):
        # Evitar cerrar la última pestaña
        if self.tab_widget.count() > 1:
            self.tab_widget.removeTab(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedTabWidget()
    window.show()
    sys.exit(app.exec())
