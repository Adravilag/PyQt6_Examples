# qsemaphore_basic.py
import sys
import time
from PyQt6.QtCore import QThread, QSemaphore, QMutexLocker, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

# Crear un semáforo con capacidad para 3 recursos simultáneos
semaphore = QSemaphore(3)

class WorkerThread(QThread):
    def __init__(self, worker_id, iterations=5, parent=None):
        super().__init__(parent)
        self.worker_id = worker_id
        self.iterations = iterations

    def run(self):
        for i in range(self.iterations):
            # Intentar adquirir el semáforo (si no hay recursos disponibles, se bloquea)
            semaphore.acquire()
            print(f"Worker {self.worker_id} acquired semaphore (iteration {i}).")
            time.sleep(0.5)  # Simula tarea
            print(f"Worker {self.worker_id} releasing semaphore (iteration {i}).")
            semaphore.release()
            time.sleep(0.1)

class SemaphoreBasicExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSemaphore Basic Example")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        self.label = QLabel("Revisa la consola para ver el uso del semáforo.", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Workers", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_workers)

    @pyqtSlot()
    def start_workers(self):
        # Lanzar 5 hilos, pero solo 3 podrán adquirir el semáforo a la vez.
        self.threads = [WorkerThread(i) for i in range(5)]
        for thread in self.threads:
            thread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SemaphoreBasicExample()
    window.show()
    sys.exit(app.exec())
