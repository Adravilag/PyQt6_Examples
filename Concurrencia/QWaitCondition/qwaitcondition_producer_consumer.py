# qwaitcondition_producer_consumer.py
import sys, time
from PyQt6.QtCore import QThread, QMutex, QWaitCondition, pyqtSignal, QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

buffer = []
buffer_size = 5
mutex = QMutex()
condition = QWaitCondition()

class ProducerThread(QThread):
    def run(self):
        global buffer
        for i in range(10):
            mutex.lock()
            while len(buffer) >= buffer_size:
                # Espera a que haya espacio en el buffer
                condition.wait(mutex)
            buffer.append(f"Item {i}")
            print(f"Produced: Item {i}")
            condition.wakeAll()  # Despierta a los consumidores
            mutex.unlock()
            time.sleep(0.5)  # Simula producción

class ConsumerThread(QThread):
    resultReady = pyqtSignal(str)
    def run(self):
        global buffer
        consumed_items = []
        for _ in range(10):
            mutex.lock()
            while not buffer:
                condition.wait(mutex)
            item = buffer.pop(0)
            consumed_items.append(item)
            print(f"Consumed: {item}")
            condition.wakeAll()  # Despierta al productor
            mutex.unlock()
            time.sleep(1)  # Simula consumo
        self.resultReady.emit("Consumed: " + ", ".join(consumed_items))

class QWaitConditionProducerConsumerExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Producer-Consumer with QWaitCondition")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        self.label = QLabel("Buffer: []", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Producer/Consumer", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_threads)
    
    def start_threads(self):
        global buffer
        buffer = []
        self.producer = ProducerThread()
        self.consumer = ConsumerThread()
        self.consumer.resultReady.connect(self.on_result_ready)
        self.producer.start()
        self.consumer.start()
    
    @pyqtSlot(str)
    def on_result_ready(self, result):
        self.label.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWaitConditionProducerConsumerExample()
    window.show()
    sys.exit(app.exec())
