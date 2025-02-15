# qsemaphore_producer_consumer.py
import sys
import time
from PyQt6.QtCore import QThread, QSemaphore, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

buffer_size = 5
availableItems = QSemaphore(0)
emptySlots = QSemaphore(buffer_size)
buffer = []

class ProducerThread(QThread):
    def run(self):
        global buffer
        for i in range(10):
            emptySlots.acquire()  # Espera a que haya un espacio disponible
            # Simula la producción
            item = f"Item {i}"
            buffer.append(item)
            print(f"Producer produced: {item}")
            availableItems.release()  # Indica que hay un nuevo ítem
            time.sleep(0.5)

class ConsumerThread(QThread):
    update = pyqtSignal(str)
    def run(self):
        global buffer
        for i in range(10):
            availableItems.acquire()  # Espera a que haya un ítem disponible
            item = buffer.pop(0)
            print(f"Consumer consumed: {item}")
            emptySlots.release()  # Libera un espacio
            self.update.emit(item)
            time.sleep(1)

class ProducerConsumerExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Producer-Consumer with QSemaphore")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        self.label = QLabel("Buffer: []", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_threads)
    
    @pyqtSlot()
    def start_threads(self):
        self.producer = ProducerThread()
        self.consumer = ConsumerThread()
        self.consumer.update.connect(self.update_label)
        self.producer.start()
        self.consumer.start()
    
    @pyqtSlot(str)
    def update_label(self, consumed_item):
        # Actualiza la etiqueta con el contenido actual del buffer
        self.label.setText("Buffer: " + str(buffer))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProducerConsumerExample()
    window.show()
    sys.exit(app.exec())
