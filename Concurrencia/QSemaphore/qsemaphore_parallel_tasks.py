# qsemaphore_parallel_tasks.py
import sys, time
from PyQt6.QtCore import QThread, QSemaphore, QMutexLocker, pyqtSignal, QObject, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt

# Limitar a 3 tareas concurrentes
max_concurrent_tasks = 3
semaphore = QSemaphore(max_concurrent_tasks)

class TaskThread(QThread):
    taskFinished = pyqtSignal(str)
    
    def __init__(self, task_id, parent=None):
        super().__init__(parent)
        self.task_id = task_id

    def run(self):
        semaphore.acquire()  # Solo permitir un máximo de tareas concurrentes
        print(f"Task {self.task_id} started.")
        time.sleep(2)  # Simula una tarea que tarda 2 segundos
        print(f"Task {self.task_id} finished.")
        semaphore.release()
        self.taskFinished.emit(f"Task {self.task_id} finished.")

class ParallelTasksExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSemaphore Parallel Tasks")
        self.resize(400, 200)
        layout = QVBoxLayout(self)
        self.label = QLabel("Tasks: []", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        self.button = QPushButton("Start Tasks", self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.start_tasks)
        self.tasks_results = []

    @pyqtSlot()
    def start_tasks(self):
        self.tasks_results = []
        self.label.setText("Tasks: []")
        self.threads = []
        # Lanzar 6 tareas; solo 3 podrán ejecutarse concurrentemente
        for i in range(6):
            thread = TaskThread(i)
            thread.taskFinished.connect(self.update_label)
            self.threads.append(thread)
            thread.start()

    @pyqtSlot(str)
    def update_label(self, result):
        self.tasks_results.append(result)
        self.label.setText("Tasks: " + ", ".join(self.tasks_results))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ParallelTasksExample()
    window.show()
    sys.exit(app.exec())
