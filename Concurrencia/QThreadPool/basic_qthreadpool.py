# basic_qthreadpool.py
import sys
import time
from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSlot, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

class PrintTask(QRunnable):
    def __init__(self, message, delay):
        super().__init__()
        self.message = message
        self.delay = delay

    @pyqtSlot()
    def run(self):
        time.sleep(self.delay)
        print(self.message)

class BasicThreadPoolExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Basic QThreadPool Example")
        self.resize(300, 150)
        layout = QVBoxLayout(self)
        self.label = QLabel("Click the button to run tasks", self)
        layout.addWidget(self.label)
        self.button = QPushButton("Run Tasks", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.run_tasks)
        self.threadpool = QThreadPool()

    def run_tasks(self):
        for i in range(5):
            task = PrintTask(f"Task {i} finished", delay=1)
            self.threadpool.start(task)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BasicThreadPoolExample()
    window.show()
    sys.exit(app.exec())
