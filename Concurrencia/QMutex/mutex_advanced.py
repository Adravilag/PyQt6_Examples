# mutex_advanced.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import QThread, QMutex, QWaitCondition, pyqtSignal, pyqtSlot
from PyQt6.QtCore import Qt

class ProducerThread(QThread):
    def __init__(self, queue, mutex, condition, iterations=20, parent=None):
        super().__init__(parent)
        self.queue = queue
        self.mutex = mutex
        self.condition = condition
        self.iterations = iterations

    def run(self):
        for i in range(self.iterations):
            self.mutex.lock()
            self.queue.append(f"Item {i}")
            print("Produced:", f"Item {i}")
            self.condition.wakeAll()
            self.mutex.unlock()
            self.msleep(200)  # 200 ms de espera

class ConsumerThread(QThread):
    resultReady = pyqtSignal(str)
    def __init__(self, queue, mutex, condition, iterations=20, parent=None):
        super().__init__(parent)
        self.queue = queue
        self.mutex = mutex
        self.condition = condition
        self.iterations = iterations
        self.consumed = []

    def run(self):
        for _ in range(self.iterations):
            self.mutex.lock()
            while not self.queue:
                self.condition.wait(self.mutex)
            item = self.queue.pop(0)
            self.consumed.append(item)
            print("Consumed:", item)
            self.mutex.unlock()
            self.sleep(1)
        self.resultReady.emit("Consumed: " + ", ".join(self.consumed))

class MutexAdvancedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMutex Advanced (Producer-Consumer)")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        self.label = QLabel("Waiting...", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Producer/Consumer", self)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.start_threads)
        
        self.queue = []
        self.mutex = QMutex()
        self.condition = QWaitCondition()
    
    def start_threads(self):
        self.producer = ProducerThread(self.queue, self.mutex, self.condition, iterations=20)
        self.consumer = ConsumerThread(self.queue, self.mutex, self.condition, iterations=20)
        self.consumer.resultReady.connect(self.on_result_ready)
        self.producer.start()
        self.consumer.start()
    
    @pyqtSlot(str)
    def on_result_ready(self, result):
        self.label.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MutexAdvancedExample()
    window.show()
    sys.exit(app.exec())
