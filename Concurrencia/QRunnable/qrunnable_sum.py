# qrunnable_sum.py
import sys, time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot

class WorkerSignals(QObject):
    finished = pyqtSignal(object)

class SumSquaresWorker(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.signals = WorkerSignals()
    
    def run(self):
        total = 0
        # Simula una tarea costosa con progresión (aunque no se reporta en tiempo real)
        for i in range(1, self.n + 1):
            time.sleep(0.05)  # Pequeño retardo para simular trabajo
            total += i * i
        self.signals.finished.emit(total)

class QRunnableSumExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRunnable Sum of Squares Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("Press button to compute sum of squares", self)
        layout.addWidget(self.label)
        self.button = QPushButton("Compute Sum", self)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.start_worker)
        self.threadpool = QThreadPool()
    
    def start_worker(self):
        self.label.setText("Computing...")
        worker = SumSquaresWorker(100)
        worker.signals.finished.connect(self.on_finished)
        self.threadpool.start(worker)
    
    @pyqtSlot(object)
    def on_finished(self, result):
        self.label.setText(f"Result: {result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRunnableSumExample()
    window.show()
    sys.exit(app.exec())
