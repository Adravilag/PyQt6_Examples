# future_alternative_sum.py
import sys
import time
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
        time.sleep(2)  # Simula una tarea costosa
        total = sum(i * i for i in range(1, self.n + 1))
        self.signals.finished.emit(total)

class FutureAlternativeSumExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Future Alternative Sum of Squares Example")
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
    window = FutureAlternativeSumExample()
    window.show()
    sys.exit(app.exec())
