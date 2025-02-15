import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt6.QtStateMachine import QState, QStateMachine
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QRect, Qt

class AdvancedStateCycleAbsExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QStateMachine Cycle (Absolute)")
        self.setGeometry(100, 100, 500, 300)
        
        # Crear un QLabel para mostrar el estado; posicionamiento absoluto
        self.label = QLabel("Red", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-size: 24px; background-color: red;")
        self.label.setGeometry(50, 50, 400, 100)
        
        # Botón para cambiar de estado
        self.button = QPushButton("Next State", self)
        self.button.setGeometry(200, 200, 100, 30)
        
        # Definir estados sin pasar parent
        state_red = QState()
        state_red.assignProperty(self.label, "text", "Red")
        state_red.assignProperty(self.label, "geometry", QRect(50, 50, 400, 100))
        state_red.assignProperty(self.label, "styleSheet", "font-size: 24px; background-color: red;")
        
        state_green = QState()
        state_green.assignProperty(self.label, "text", "Green")
        state_green.assignProperty(self.label, "geometry", QRect(70, 70, 380, 90))
        state_green.assignProperty(self.label, "styleSheet", "font-size: 24px; background-color: green;")
        
        state_blue = QState()
        state_blue.assignProperty(self.label, "text", "Blue")
        state_blue.assignProperty(self.label, "geometry", QRect(90, 90, 360, 80))
        state_blue.assignProperty(self.label, "styleSheet", "font-size: 24px; background-color: blue;")
        
        # Crear la máquina de estados y agregar los estados
        self.machine = QStateMachine(self)
        self.machine.addState(state_red)
        self.machine.addState(state_green)
        self.machine.addState(state_blue)
        self.machine.setInitialState(state_red)
        
        # Transición: Red -> Green
        trans_rg = state_red.addTransition(self.button.clicked, state_green)
        anim_rg = QPropertyAnimation(self.label, b"geometry", self)
        anim_rg.setDuration(1000)
        anim_rg.setEasingCurve(QEasingCurve.Type.InOutQuad)
        trans_rg.addAnimation(anim_rg)
        
        # Transición: Green -> Blue
        trans_gb = state_green.addTransition(self.button.clicked, state_blue)
        anim_gb = QPropertyAnimation(self.label, b"geometry", self)
        anim_gb.setDuration(1000)
        anim_gb.setEasingCurve(QEasingCurve.Type.InOutQuad)
        trans_gb.addAnimation(anim_gb)
        
        # Transición: Blue -> Red
        trans_br = state_blue.addTransition(self.button.clicked, state_red)
        anim_br = QPropertyAnimation(self.label, b"geometry", self)
        anim_br.setDuration(1000)
        anim_br.setEasingCurve(QEasingCurve.Type.InOutQuad)
        trans_br.addAnimation(anim_br)
        
        self.machine.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedStateCycleAbsExample()
    window.show()
    sys.exit(app.exec())
