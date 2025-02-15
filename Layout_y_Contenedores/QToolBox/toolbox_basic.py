# toolbox_basic.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QToolBox, QLabel, QVBoxLayout

class BasicToolBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QToolBox Example")
        self.resize(400, 300)
        
        layout = QVBoxLayout(self)
        
        # Crear QToolBox
        toolbox = QToolBox(self)
        
        # Primera página: Información general
        page1 = QWidget()
        page1_layout = QVBoxLayout(page1)
        page1_layout.addWidget(QLabel("Esta es la página de información general.", page1))
        toolbox.addItem(page1, "General Info")
        
        # Segunda página: Detalles adicionales
        page2 = QWidget()
        page2_layout = QVBoxLayout(page2)
        page2_layout.addWidget(QLabel("Esta es la página de detalles adicionales.", page2))
        toolbox.addItem(page2, "Details")
        
        layout.addWidget(toolbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicToolBoxExample()
    window.show()
    sys.exit(app.exec())
