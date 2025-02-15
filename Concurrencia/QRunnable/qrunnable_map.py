# qrunnable_map.py
import sys, time
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot

class WorkerSignals(QObject):
    finished = pyqtSignal(object)

class MapWorker(QRunnable):
    def __init__(self, numbers):
        super().__init__()
        self.numbers = numbers
        self.signals = WorkerSignals()
    
    def run(self):
        time.sleep(2)  # Simula una tarea costosa
        result = [x * x for x in self.numbers]
        self.signals.finished.emit(result)

class QRunnableMapExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRunnable Map Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("Press button to map squares", self)
        layout.addWidget(self.label)
        self.button = QPushButton("Map Squares", self)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.start_worker)
        self.threadpool = QThreadPool()
        self.numbers = [1, 2, 3, 4, 5]
    
    def start_worker(self):
        self.label.setText("Mapping...")
        worker = MapWorker(self.numbers)
        worker.signals.finished.connect(self.on_finished)
        self.threadpool.start(worker)
    
    @pyqtSlot(object)
    def on_finished(self, result):
        self.label.setText("Result: " + str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QRunnableMapExample()
    window.show()
    sys.exit(app.exec())
