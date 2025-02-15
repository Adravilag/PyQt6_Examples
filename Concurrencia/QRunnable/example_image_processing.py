# image_processing.py
import sys, time, random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QListWidgetItem, QLabel
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal, QObject, pyqtSlot, Qt

class WorkerSignals(QObject):
    finished = pyqtSignal(str)

class ImageProcessorWorker(QRunnable):
    """
    Simula el procesamiento de una imagen.
    Se "procesa" la imagen y se devuelve un resultado simulado.
    """
    def __init__(self, image_name):
        super().__init__()
        self.image_name = image_name
        self.signals = WorkerSignals()
    
    @pyqtSlot()
    def run(self):
        # Simula un retardo en el procesamiento (2-4 segundos)
        time.sleep(random.uniform(2, 4))
        # Simula la detección de características (aleatoria)
        features = random.randint(50, 300)
        result = f"{self.image_name}: {features} features detected"
        self.signals.finished.emit(result)

class ImageProcessingExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processing Simulator")
        self.resize(500, 400)
        layout = QVBoxLayout(self)
        
        self.instructions = QLabel("Click 'Process Images' to simulate image processing.", self)
        self.instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.instructions)
        
        self.processButton = QPushButton("Process Images", self)
        layout.addWidget(self.processButton)
        self.processButton.clicked.connect(self.start_processing)
        
        self.resultList = QListWidget(self)
        layout.addWidget(self.resultList)
        
        # Lista simulada de imágenes
        self.image_files = [f"image_{i}.jpg" for i in range(1, 11)]
        self.threadpool = QThreadPool()

    def start_processing(self):
        self.resultList.clear()
        for img in self.image_files:
            worker = ImageProcessorWorker(img)
            worker.signals.finished.connect(self.add_result)
            self.threadpool.start(worker)
    
    @pyqtSlot(str)
    def add_result(self, result):
        self.resultList.addItem(QListWidgetItem(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageProcessingExample()
    window.show()
    sys.exit(app.exec())
