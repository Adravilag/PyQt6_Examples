# mutex_intermediate.py
import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import QRunnable, QThreadPool, QMutex, QMutexLocker, pyqtSignal, QObject, pyqtSlot
from PyQt6.QtCore import Qt

shared_list = []
mutex = QMutex()

class WorkerSignals(QObject):
    finished = pyqtSignal(object)

class AppendWorker(QRunnable):
    def __init__(self, value, iterations):
        super().__init__()
        self.value = value
        self.iterations = iterations
        self.signals = WorkerSignals()
    
    def run(self):
        global shared_list
        for _ in range(self.iterations):
            with QMutexLocker(mutex):
                shared_list.append(self.value)
            time.sleep(0.0005)  # Simula trabajo
        self.signals.finished.emit(shared_list)

class MutexIntermediateExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMutex Intermediate Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("List length: 0", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Append", self)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.start_workers)
        self.threadpool = QThreadPool()
    
    def start_workers(self):
        global shared_list
        shared_list = []
        worker1 = AppendWorker("A", 5000)
        worker2 = AppendWorker("B", 5000)
        worker1.signals.finished.connect(self.update_label)
        worker2.signals.finished.connect(self.update_label)
        self.threadpool.start(worker1)
        self.threadpool.start(worker2)
    
    @pyqtSlot(object)
    def update_label(self, result):
        self.label.setText(f"List length: {len(result)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MutexIntermediateExample()
    window.show()
    sys.exit(app.exec())
