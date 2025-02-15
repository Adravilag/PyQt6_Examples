import sys
import time
from PyQt6.QtCore import QThread, QMutex, QMutexLocker, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

counter = 0
mutex = QMutex()

class IncrementThread(QThread):
    def __init__(self, iterations, parent=None):
        super().__init__(parent)
        self.iterations = iterations

    def run(self):
        global counter
        for _ in range(self.iterations):
            with QMutexLocker(mutex):
                counter += 1
            # Simula algo de trabajo
            time.sleep(0.0001)

class MutexBasicExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMutex Basic Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("Counter: 0", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Increment", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_threads)

    @pyqtSlot()
    def start_threads(self):
        global counter
        counter = 0  # Reiniciar contador
        # Crear dos hilos que incrementen el contador 10,000 veces cada uno
        self.thread1 = IncrementThread(10000)
        self.thread2 = IncrementThread(10000)
        # Conectar la señal finished para actualizar la etiqueta cuando cada hilo termine
        self.thread1.finished.connect(self.update_label)
        self.thread2.finished.connect(self.update_label)
        self.thread1.start()
        self.thread2.start()

    @pyqtSlot()
    def update_label(self):
        self.label.setText(f"Counter: {counter}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MutexBasicExample()
    window.show()
    sys.exit(app.exec())
