# advanced_qthreadpool.py
import sys
import time
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class WorkerSignals(QObject):
    result = pyqtSignal(object)

class SumSquaresWorker(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.signals = WorkerSignals()
    
    @pyqtSlot()
    def run(self):
        total = 0
        for i in range(1, self.n + 1):
            time.sleep(0.05)  # Simula trabajo
            total += i * i
        self.signals.result.emit(total)

class AdvancedThreadPoolExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QThreadPool Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("Press button to compute sum of squares", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Compute", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_worker)
        self.threadpool = QThreadPool()

    def start_worker(self):
        self.label.setText("Computing...")
        worker = SumSquaresWorker(100)
        worker.signals.result.connect(self.on_result)
        self.threadpool.start(worker)

    @pyqtSlot(object)
    def on_result(self, result):
        self.label.setText(f"Result: {result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedThreadPoolExample()
    window.show()
    sys.exit(app.exec())
