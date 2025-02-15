# logs_analysis.py
import sys, time, random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QLabel
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot, Qt

class WorkerSignals(QObject):
    finished = pyqtSignal(str)

class LogFileWorker(QRunnable):
    """
    Simula el procesamiento de un archivo de log.
    Cuenta aleatoriamente líneas de error y devuelve un resultado.
    """
    def __init__(self, log_filename):
        super().__init__()
        self.log_filename = log_filename
        self.signals = WorkerSignals()
    
    @pyqtSlot()
    def run(self):
        # Simula tiempo de procesamiento (1-3 segundos)
        time.sleep(random.uniform(1, 3))
        # Simula un recuento de errores
        error_count = random.randint(0, 50)
        result = f"{self.log_filename}: {error_count} error(s)"
        self.signals.finished.emit(result)

class LogsAnalysisExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logs Analysis")
        self.resize(500, 400)
        layout = QVBoxLayout(self)
        
        self.instructions = QLabel("Click 'Process Logs' to simulate log analysis.", self)
        self.instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.instructions)
        
        self.processButton = QPushButton("Process Logs", self)
        layout.addWidget(self.processButton)
        self.processButton.clicked.connect(self.start_processing)
        
        self.resultList = QListWidget(self)
        layout.addWidget(self.resultList)
        
        # Lista simulada de archivos de logs
        self.log_files = [f"log_{i}.txt" for i in range(1, 11)]
        
        self.threadpool = QThreadPool()

    def start_processing(self):
        self.resultList.clear()
        for filename in self.log_files:
            worker = LogFileWorker(filename)
            worker.signals.finished.connect(self.add_result)
            self.threadpool.start(worker)
    
    @pyqtSlot(str)
    def add_result(self, result):
        self.resultList.addItem(QListWidgetItem(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogsAnalysisExample()
    window.show()
    sys.exit(app.exec())
