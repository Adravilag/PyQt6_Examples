# intermediate_qthreadpool.py
import sys
import time
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class WorkerSignals(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal()

class SquareWorker(QRunnable):
    def __init__(self, iterations=100):
        super().__init__()
        self.iterations = iterations
        self.signals = WorkerSignals()
    
    @pyqtSlot()
    def run(self):
        for i in range(1, self.iterations + 1):
            time.sleep(0.05)  # Simula trabajo
            progress = int((i / self.iterations) * 100)
            self.signals.progress.emit(progress)
        self.signals.finished.emit()

class IntermediateThreadPoolExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QThreadPool Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("Progress: 0%", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Task", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_task)
        self.threadpool = QThreadPool()

    def start_task(self):
        worker = SquareWorker(100)
        worker.signals.progress.connect(lambda p: self.label.setText(f"Progress: {p}%"))
        worker.signals.finished.connect(lambda: self.label.setText("Finished"))
        self.threadpool.start(worker)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateThreadPoolExample()
    window.show()
    sys.exit(app.exec())
