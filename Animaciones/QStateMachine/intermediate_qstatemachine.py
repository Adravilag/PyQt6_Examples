# intermediate_qstatemachine.py
import sys
from PyQt6.QtStateMachine import QState, QStateMachine
from PyQt6.QtCore import QTimer, Qt, pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class IntermediateStateMachineExample(QWidget):
    # Señal personalizada para alternar estados
    toggleState = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QStateMachine Example")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        
        self.label = QLabel("State 1", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.button = QPushButton("Start Auto Toggle", self)
        layout.addWidget(self.button)
        
        # Configurar un QTimer para emitir la señal toggleState cada 2 segundos
        self.timer = QTimer(self)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.toggleState.emit)
        
        self.button.clicked.connect(self.timer.start)
        
        # Definir dos estados con diferentes propiedades
        self.state1 = QState()
        self.state1.assignProperty(self.label, "text", "State 1")
        self.state1.assignProperty(self, "styleSheet", "background-color: peachpuff;")
        
        self.state2 = QState()
        self.state2.assignProperty(self.label, "text", "State 2")
        self.state2.assignProperty(self, "styleSheet", "background-color: lightsteelblue;")
        
        self.machine = QStateMachine(self)
        self.machine.addState(self.state1)
        self.machine.addState(self.state2)
        self.machine.setInitialState(self.state1)
        
        # Transiciones basadas en la señal toggleState
        self.state1.addTransition(self.toggleState, self.state2)
        self.state2.addTransition(self.toggleState, self.state1)
        
        self.machine.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateStateMachineExample()
    window.show()
    sys.exit(app.exec())
