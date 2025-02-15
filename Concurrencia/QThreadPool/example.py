import sys, time, random
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget, QListWidgetItem

class WorkerSignals(QObject):
    finished = pyqtSignal(str)

class OrderWorker(QRunnable):
    """
    Simula el procesamiento de un pedido. 
    En un escenario real, aquí se podría procesar información del pedido,
    comunicarse con una base de datos o un sistema de pago, etc.
    """
    def __init__(self, order_id):
        super().__init__()
        self.order_id = order_id
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        # Simula el tiempo de procesamiento (entre 1 y 3 segundos)
        processing_time = random.uniform(1, 3)
        time.sleep(processing_time)
        result = f"Order {self.order_id} processed in {processing_time:.2f} sec."
        self.signals.finished.emit(result)

class OrderProcessingSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Order Processing Simulator with QThreadPool")
        self.resize(500, 400)
        layout = QVBoxLayout(self)

        self.instructions = QLabel("Click 'Process Orders' to start processing orders concurrently.", self)
        self.instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.instructions)

        self.processButton = QPushButton("Process Orders", self)
        layout.addWidget(self.processButton)
        self.processButton.clicked.connect(self.process_orders)

        self.resultList = QListWidget(self)
        layout.addWidget(self.resultList)

        # QThreadPool para ejecutar múltiples workers en paralelo
        self.threadpool = QThreadPool()
        self.total_orders = 10

    @pyqtSlot()
    def process_orders(self):
        self.resultList.clear()
        # Encolar la tarea de procesar cada pedido
        for order_id in range(1, self.total_orders + 1):
            worker = OrderWorker(order_id)
            worker.signals.finished.connect(self.add_result)
            self.threadpool.start(worker)

    @pyqtSlot(str)
    def add_result(self, result):
        item = QListWidgetItem(result)
        self.resultList.addItem(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrderProcessingSimulator()
    window.show()
    sys.exit(app.exec())
