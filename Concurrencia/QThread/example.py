import sys, time, random
from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QListWidget

class OrderProcessor(QThread):
    """
    Simula el procesamiento de un pedido.
    Cada pedido tarda entre 1 y 3 segundos en procesarse.
    """
    orderProcessed = pyqtSignal(str)
    
    def __init__(self, order_id, parent=None):
        super().__init__(parent)
        self.order_id = order_id
    
    def run(self):
        processing_time = random.uniform(1, 3)
        time.sleep(processing_time)
        result = f"Order {self.order_id} processed in {processing_time:.1f} s"
        self.orderProcessed.emit(result)

class OrderProcessingSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Order Processing Simulator")
        self.resize(400, 300)
        layout = QVBoxLayout(self)
        
        self.infoLabel = QLabel("Press the button to process orders concurrently.", self)
        self.infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.infoLabel)
        
        self.startButton = QPushButton("Process Orders", self)
        layout.addWidget(self.startButton)
        self.startButton.clicked.connect(self.process_orders)
        
        self.resultsList = QListWidget(self)
        layout.addWidget(self.resultsList)
        
        self.threads = []
    
    @pyqtSlot()
    def process_orders(self):
        self.resultsList.clear()
        self.infoLabel.setText("Processing orders...")
        number_of_orders = 10
        self.threads = []
        for order_id in range(1, number_of_orders + 1):
            thread = OrderProcessor(order_id)
            thread.orderProcessed.connect(self.display_result)
            self.threads.append(thread)
            thread.start()
    
    @pyqtSlot(str)
    def display_result(self, result):
        self.resultsList.addItem(result)
        # Cuando se hayan procesado todos, actualizamos la etiqueta
        if self.resultsList.count() == 10:
            self.infoLabel.setText("All orders processed.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OrderProcessingSimulator()
    window.show()
    sys.exit(app.exec())
