# basic_qthread.py
import sys, time
from PyQt6.QtCore import QThread, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class WorkerThread(QThread):
    def run(self):
        # Tarea: incrementar un contador y dormir para simular trabajo
        self.result = 0
        for i in range(1, 10001):
            self.result += i
            time.sleep(0.0001)  # Simula trabajo

class BasicQThreadExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QThread Example")
        self.resize(300, 150)
        
        layout = QVBoxLayout(self)
        self.label = QLabel("Press button to start thread", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Task", self)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.start_worker)
    
    @pyqtSlot()
    def start_worker(self):
        self.label.setText("Working...")
        self.thread = WorkerThread()
        self.thread.finished.connect(self.on_finished)
        self.thread.start()
    
    @pyqtSlot()
    def on_finished(self):
        self.label.setText(f"Result: {self.thread.result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicQThreadExample()
    window.show()
    sys.exit(app.exec())
