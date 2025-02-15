# intermediate_qthread.py
import sys, time
from PyQt6.QtCore import QThread, pyqtSignal, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class WorkerThread(QThread):
    progressChanged = pyqtSignal(int)
    finishedResult = pyqtSignal(int)
    
    def run(self):
        total = 0
        iterations = 100
        for i in range(1, iterations+1):
            total += i * i
            # Emite el progreso
            progress = int((i / iterations) * 100)
            self.progressChanged.emit(progress)
            time.sleep(0.05)
        self.finishedResult.emit(total)

class IntermediateQThreadExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intermediate QThread Example")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        self.label = QLabel("Progress: 0%", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Task", self)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.start_worker)
    
    @pyqtSlot()
    def start_worker(self):
        self.label.setText("Starting...")
        self.thread = WorkerThread()
        self.thread.progressChanged.connect(lambda p: self.label.setText(f"Progress: {p}%"))
        self.thread.finishedResult.connect(lambda res: self.label.setText(f"Result: {res}"))
        self.thread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = IntermediateQThreadExample()
    window.show()
    sys.exit(app.exec())
