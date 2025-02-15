# advanced_qthread.py
import sys, time
from PyQt6.QtCore import QObject, QThread, pyqtSignal, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class Worker(QObject):
    progressChanged = pyqtSignal(int)
    finishedResult = pyqtSignal(int)
    
    @pyqtSlot()
    def process(self):
        total = 0
        iterations = 100
        for i in range(1, iterations+1):
            total += i * i
            progress = int((i / iterations) * 100)
            self.progressChanged.emit(progress)
            time.sleep(0.05)
        self.finishedResult.emit(total)

class AdvancedQThreadExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced QThread Example (Worker Object)")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("Progress: 0%", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Task", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_worker)
        
        # Crear un QThread y un Worker
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        
        # Conectar señales: Cuando el thread se inicia, se ejecuta la tarea del worker.
        self.thread.started.connect(self.worker.process)
        self.worker.progressChanged.connect(self.update_progress)
        self.worker.finishedResult.connect(self.task_finished)
        # Cuando la tarea termina, se detiene el thread.
        self.worker.finishedResult.connect(self.thread.quit)
        # Opcionalmente, se elimina el worker al terminar
        self.thread.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
    
    @pyqtSlot()
    def start_worker(self):
        self.label.setText("Starting...")
        self.thread.start()
    
    @pyqtSlot(int)
    def update_progress(self, progress):
        self.label.setText(f"Progress: {progress}%")
    
    @pyqtSlot(int)
    def task_finished(self, result):
        self.label.setText(f"Result: {result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdvancedQThreadExample()
    window.show()
    sys.exit(app.exec())
