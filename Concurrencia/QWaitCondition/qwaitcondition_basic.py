# qwaitcondition_basic.py
import sys
import time
from PyQt6.QtCore import QThread, QMutex, QWaitCondition, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

class WaitThread(QThread):
    def __init__(self, mutex, condition, parent=None):
        super().__init__(parent)
        self.mutex = mutex
        self.condition = condition

    def run(self):
        self.mutex.lock()
        print("WaitThread: Esperando la condición...")
        self.condition.wait(self.mutex)  # Espera hasta que se active la condición
        print("WaitThread: Condición activada, continuando...")
        self.mutex.unlock()

class QWaitConditionBasicExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWaitCondition Basic Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        
        self.label = QLabel("Presiona el botón para activar la condición", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.button = QPushButton("Activar Condición", self)
        layout.addWidget(self.button)
        
        # Crear un QMutex y QWaitCondition
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        
        # Crear e iniciar el hilo que espera la condición
        self.wait_thread = WaitThread(self.mutex, self.condition)
        self.wait_thread.start()
        
        self.button.clicked.connect(self.activate_condition)

    @pyqtSlot()
    def activate_condition(self):
        # Simula un retardo antes de activar la condición
        time.sleep(1)
        print("Main thread: Activando la condición.")
        self.condition.wakeAll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWaitConditionBasicExample()
    window.show()
    sys.exit(app.exec())
