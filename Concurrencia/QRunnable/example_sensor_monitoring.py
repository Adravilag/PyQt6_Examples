import sys, random, time
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QProgressBar, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot, Qt, QRect

def process_sensor_block(data_block):
    # Simula un retardo en el procesamiento
    time.sleep(0.5)
    avg = sum(data_block) / len(data_block)
    maximum = max(data_block)
    minimum = min(data_block)
    return avg, maximum, minimum

class WorkerSignals(QObject):
    # No usaremos la señal 'progress' enviada por cada worker.
    result = pyqtSignal(tuple)

class SensorWorker(QRunnable):
    def __init__(self, data_block, block_index, total_blocks):
        super().__init__()
        self.data_block = data_block
        self.block_index = block_index
        self.total_blocks = total_blocks
        self.signals = WorkerSignals()
    
    @pyqtSlot()
    def run(self):
        result = process_sensor_block(self.data_block)
        self.signals.result.emit(result)
        # Ya no emitimos progreso desde aquí

class SensorMonitoringExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sensor Monitoring Simulator")
        self.resize(500, 400)
        layout = QVBoxLayout(self)
        
        self.progressBar = QProgressBar(self)
        self.progressBar.setRange(0, 100)
        layout.addWidget(self.progressBar)
        
        self.resultList = QListWidget(self)
        layout.addWidget(self.resultList)
        
        self.startButton = QPushButton("Start Processing", self)
        layout.addWidget(self.startButton)
        self.startButton.clicked.connect(self.start_processing)
        
        self.threadpool = QThreadPool()
        self.sensor_data = self.generate_sensor_data(1000)
        self.results = []
        self.completed_blocks = 0

    def generate_sensor_data(self, total):
        # Simula lecturas de sensores en el rango de 10 a 50 (por ejemplo, temperatura)
        return [random.uniform(10.0, 50.0) for _ in range(total)]
    
    def start_processing(self):
        self.resultList.clear()
        self.results = []
        self.completed_blocks = 0
        
        block_size = 100
        blocks = [self.sensor_data[i:i+block_size] for i in range(0, len(self.sensor_data), block_size)]
        self.total_blocks = len(blocks)
        
        for idx, block in enumerate(blocks):
            worker = SensorWorker(block, idx, self.total_blocks)
            worker.signals.result.connect(self.collect_result)
            self.threadpool.start(worker)
    
    @pyqtSlot(tuple)
    def collect_result(self, result):
        self.results.append(result)
        self.completed_blocks += 1
        # Actualizar el progreso global basado en el número de bloques completados
        progress = int((self.completed_blocks / self.total_blocks) * 100)
        self.progressBar.setValue(progress)
        # Agregar resultado a la lista (opcional)
        self.resultList.addItem(QListWidgetItem(f"Block {self.completed_blocks}: {result}"))
        # Cuando todos los bloques se han procesado, calcular estadísticas globales
        if self.completed_blocks == self.total_blocks:
            self.compute_global_statistics()
    
    def compute_global_statistics(self):
        avgs = [r[0] for r in self.results]
        maxs = [r[1] for r in self.results]
        mins = [r[2] for r in self.results]
        global_avg = sum(avgs) / len(avgs)
        global_max = max(maxs)
        global_min = min(mins)
        summary = f"Global Average: {global_avg:.2f}, Max: {global_max:.2f}, Min: {global_min:.2f}"
        self.resultList.addItem(QListWidgetItem(summary))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SensorMonitoringExample()
    window.show()
    sys.exit(app.exec())
