# qwaitcondition_advanced.py
import sys, time
from PyQt6.QtCore import QThread, QMutex, QWaitCondition, pyqtSignal, QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

buffer = []
buffer_size = 5
mutex = QMutex()
condition = QWaitCondition()

class Producer(QThread):
    idProduced = pyqtSignal(str)
    
    def __init__(self, producer_id, iterations=10, parent=None):
        super().__init__(parent)
        self.producer_id = producer_id
        self.iterations = iterations

    def run(self):
        global buffer
        for i in range(self.iterations):
            mutex.lock()
            while len(buffer) >= buffer_size:
                condition.wait(mutex)
            item = f"P{self.producer_id}-Item{i}"
            buffer.append(item)
            print(f"Producer {self.producer_id} produced: {item}")
            condition.wakeAll()  # Despertar a consumidores
            mutex.unlock()
            self.idProduced.emit(item)
            time.sleep(0.3)

class Consumer(QThread):
    idConsumed = pyqtSignal(str)
    
    def __init__(self, consumer_id, iterations=10, parent=None):
        super().__init__(parent)
        self.consumer_id = consumer_id
        self.iterations = iterations

    def run(self):
        global buffer
        for _ in range(self.iterations):
            mutex.lock()
            while not buffer:
                condition.wait(mutex)
            item = buffer.pop(0)
            print(f"Consumer {self.consumer_id} consumed: {item}")
            condition.wakeAll()  # Despertar a productores
            mutex.unlock()
            self.idConsumed.emit(item)
            time.sleep(0.6)

class QWaitConditionAdvancedExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QWaitCondition Example")
        self.resize(500, 250)
        layout = QVBoxLayout(self)
        self.label = QLabel("Check console for producer/consumer logs.", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Advanced", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_threads)
    
    def start_threads(self):
        self.producers = [Producer(i, iterations=10) for i in range(2)]
        self.consumers = [Consumer(i, iterations=10) for i in range(2)]
        for producer in self.producers:
            producer.start()
        for consumer in self.consumers:
            consumer.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWaitConditionAdvancedExample()
    window.show()
    sys.exit(app.exec())
