# basic_qstatemachine.py
import sys
from PyQt6.QtStateMachine import QState, QStateMachine
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class BasicStateMachineExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QStateMachine Example")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        
        self.label = QLabel("State 1", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.button = QPushButton("Toggle State", self)
        layout.addWidget(self.button)
        
        # Definición de estados
        self.state1 = QState()
        self.state1.assignProperty(self.label, "text", "State 1")
        self.state1.assignProperty(self, "styleSheet", "background-color: lightblue;")
        
        self.state2 = QState()
        self.state2.assignProperty(self.label, "text", "State 2")
        self.state2.assignProperty(self, "styleSheet", "background-color: lightgreen;")
        
        # Configuración de la máquina de estados
        self.machine = QStateMachine(self)
        self.machine.addState(self.state1)
        self.machine.addState(self.state2)
        self.machine.setInitialState(self.state1)
        
        # Transiciones: cambiar de estado al hacer clic en el botón
        self.state1.addTransition(self.button.clicked, self.state2)
        self.state2.addTransition(self.button.clicked, self.state1)
        
        self.machine.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicStateMachineExample()
    window.show()
    sys.exit(app.exec())
