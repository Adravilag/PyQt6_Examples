# qrunnable_basic.py
import sys, time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot

class WorkerSignals(QObject):
    finished = pyqtSignal(object)

class SquareWorker(QRunnable):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.signals = WorkerSignals()
    
    def run(self):
        time.sleep(2)  # Simula una tarea costosa
        result = self.x * self.x
        self.signals.finished.emit(result)

class QRunnableBasicExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRunnable Basic Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("Press button to compute square", self)
        layout.addWidget(self.label)
        self.button = QPushButton("Compute Square", self)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.start_worker)
        self.threadpool = QThreadPool()
    
    def start_worker(self):
        self.label.setText("Computing...")
        worker = SquareWorker(10)
        worker.signals.finished.connect(self.on_finished)
        self.threadpool.start(worker)
    
    @pyqtSlot(object)
    def on_finished(self, result):
        self.label.setText(f"Result: {result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRunnableBasicExample()
    window.show()
    sys.exit(app.exec())
