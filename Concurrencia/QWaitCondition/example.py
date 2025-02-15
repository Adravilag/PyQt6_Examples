import sys, time, random
from PyQt6.QtCore import QThread, QMutex, QWaitCondition, pyqtSignal, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem

# Recurso compartido: cola de datos simulados de sensores.
sensor_queue = []
# Mutex para proteger el acceso a la cola.
mutex = QMutex()
# QWaitCondition para notificar al consumidor cuando hay nuevos datos.
condition = QWaitCondition()

class SensorProducer(QThread):
    """
    Hilo productor que simula la generación de datos de un sensor.
    Genera datos (simulados) y los añade a la cola.
    """
    produced = pyqtSignal(str)
    
    def __init__(self, sensor_id, iterations=10, parent=None):
        super().__init__(parent)
        self.sensor_id = sensor_id
        self.iterations = iterations

    def run(self):
        global sensor_queue
        for i in range(self.iterations):
            # Simula el retardo de la lectura del sensor.
            time.sleep(random.uniform(0.2, 0.5))
            # Simula un dato: por ejemplo, una lectura de temperatura.
            data = f"Sensor {self.sensor_id}: {random.uniform(20, 30):.2f} °C"
            # Bloquear el mutex para modificar la cola de forma segura.
            mutex.lock()
            sensor_queue.append(data)
            print(f"Produced: {data}")
            condition.wakeAll()  # Despierta al consumidor si está esperando.
            mutex.unlock()
            self.produced.emit(f"Produced: {data}")

class SensorConsumer(QThread):
    """
    Hilo consumidor que procesa datos de la cola.
    Si la cola está vacía, se bloquea hasta que se le notifique que hay datos.
    """
    consumed = pyqtSignal(str)
    
    def __init__(self, total_items=20, parent=None):
        super().__init__(parent)
        self.total_items = total_items  # Número total de datos a consumir.

    def run(self):
        global sensor_queue
        count = 0
        while count < self.total_items:
            mutex.lock()
            while not sensor_queue:
                # Si la cola está vacía, espera hasta que se despierte.
                condition.wait(mutex)
            # Extrae el primer elemento de la cola.
            data = sensor_queue.pop(0)
            mutex.unlock()
            # Simula el procesamiento del dato.
            time.sleep(0.3)
            count += 1
            print(f"Consumed: {data} (Total consumed: {count})")
            self.consumed.emit(f"Consumed: {data} (Total: {count})")

class SensorDataQueueSimulator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensor Data Queue Simulator (QWaitCondition)")
        self.resize(500, 300)
        layout = QVBoxLayout(self)
        
        self.logList = QListWidget(self)
        layout.addWidget(self.logList)
        
        self.startButton = QPushButton("Start Simulation", self)
        layout.addWidget(self.startButton)
        self.startButton.clicked.connect(self.start_simulation)
        
        # Almacenará las referencias a los hilos para evitar que se recolecten.
        self.producers = []
        self.consumer = None

    @pyqtSlot()
    def start_simulation(self):
        self.logList.clear()
        # Reinicia la cola de datos
        global sensor_queue
        sensor_queue = []
        
        # Crear dos hilos productores (simulando 2 sensores) que generen 10 datos cada uno.
        self.producers = [SensorProducer(sensor_id=i, iterations=10) for i in range(1, 3)]
        for prod in self.producers:
            prod.produced.connect(self.log_message)
            prod.start()
        
        # Crear un hilo consumidor que consumirá 20 datos (en total, 10 de cada sensor).
        self.consumer = SensorConsumer(total_items=20)
        self.consumer.consumed.connect(self.log_message)
        self.consumer.start()

    @pyqtSlot(str)
    def log_message(self, msg):
        self.logList.addItem(QListWidgetItem(msg))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SensorDataQueueSimulator()
    window.show()
    sys.exit(app.exec())
